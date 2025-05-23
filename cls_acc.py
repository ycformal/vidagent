import os
import json
import re
import shutil
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('dataset/NExTVideo/test.csv')

def get_answer(file, method1):
    if not os.path.exists(os.path.join(f'results_{method1}', file)):
        print(f'File not found in results_{method1}:', file)
        return 0.5, -1
    correct = 0
    type = ''
    videoId = file.split('_')[-1].split('.')[0]
    with open(os.path.join(f'results_{method1}', file), 'r') as f:
        content = f.read()
        answer = re.search(r'\nAnswer: (.+)', content)
        try:
            answer = answer.group(1)
        except:
            print('answer not found in', file)
            return 0.5, -1
        if 'error' in answer:
            print('answer not found in', file)
            return 0.5, -1
        question = re.search(r'Question: (.+)', content)
        question = question.group(1).strip()
        question = question[0].lower() + question[1:-1]
        row = dataset[dataset['question'] == question]
        if row.empty:
            print(f'Question not found in dataset: {question}')
            q_type = None
        else:
            q_type = row.iloc[0]['type']
        reference = re.search(r'Reference Answer: (.+)', content)
        reference = reference.group(1)
        # split reference by non-alphanumeric characters
        reference = re.sub(r'\W+', ' ', reference)
        if answer == reference:
            correct = 1, q_type
        else:
            correct = 0, q_type
    return correct

def main():
    method = 'vidagent_gpt_vidqa_ssparser'
    results = os.listdir(f'results_{method}')
    correct = 0
    total = 0
    correctness_per_type = dict()
    for result in results:
        correctness, q_type = get_answer(result, method)
        if correctness == 0.5:
            continue
        if q_type not in correctness_per_type:
            correctness_per_type[q_type] = [correctness]
        else:
            correctness_per_type[q_type].append(correctness)
    # Compute accuracy per type
    types = list(correctness_per_type.keys())
    accuracies = [sum(vals)/len(vals) for vals in correctness_per_type.values()]

    correctness_T = correctness_per_type['TC'] + correctness_per_type['TP'] + correctness_per_type['TN']
    print(sum(correctness_T) / len(correctness_T))

    correctness_C = correctness_per_type['CW'] + correctness_per_type['CH']
    print(sum(correctness_C) / len(correctness_C))

    # Plot
    plt.figure()
    plt.bar(types, accuracies)
    plt.xlabel('Question Type')
    plt.ylabel('Accuracy')
    plt.title('Accuracy per Question Type')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('acc_per_type.png')

main()