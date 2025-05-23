import os
import json
import re
import shutil

def get_answer(file, method1):
    if not os.path.exists(os.path.join(f'results_{method1}', file)):
        print(f'File not found in results_{method1}:', file)
        return 0.5
    correct = 0
    type = ''
    imageId = file.split('_')[-1].split('.')[0]
    with open(os.path.join(f'results_{method1}', file), 'r') as f:
        content = f.read()
        answer = re.search(r'\nAnswer: (.+)', content)
        try:
            answer = answer.group(1)
        except:
            print('answer not found in', file)
            return 0.5
        if 'error' in answer:
            print(answer)
            print('error found in', file)
            return 0.5
        question = re.search(r'Question: (.+)', content)
        question = question.group(1).strip()
        reference = re.search(r'Reference Answer: (.+)', content)
        reference = reference.group(1)
        # split reference by non-alphanumeric characters
        reference = re.sub(r'\W+', ' ', reference)
        if answer == reference:
            correct = 1
        else:
            correct = 0
    return correct

def main():
    method = 'vidagent_gpt_vqa_cap_ssparser'
    results = os.listdir(f'results_{method}')
    correct = 0
    total = 0
    for result in results:
        correctness = get_answer(result, method)
        if correctness == 0.5:
            continue
        correct += correctness
        total += 1
        
    print(f'Correct_{method}: {correct}/{total}')
    print(f'Accuracy_{method}: {correct/total}')

main()