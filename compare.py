import os
import json
import re
import shutil

def get_answer(file, method1, method2):
    if not os.path.exists(os.path.join(f'results_{method1}', file)):
        print(f'File not found in results_{method1}:', file)
        return 0.5
    correct1 = 0
    correct2 = 0
    with open(os.path.join(f'results_{method1}', file), 'r') as f:
        content = f.read()
        answer = re.search(r'\nAnswer: (.+)', content)
        answer1=answer
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
            correct1 = 1
        else:
            correct1 = 0
    if not os.path.exists(os.path.join(f'results_{method2}', file)):
        return
    with open(os.path.join(f'results_{method2}', file), 'r') as f:
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
            correct2 = 1
        else:
            correct2 = 0
    if correct1 == 0 and correct2 == 1:
        print('fail', question, answer1)
    if correct1 == 1 and correct2 == 0:
        print('success', question)

def main():
    method1 = 'vidagent_gpt_vidqa_ssparser'
    method2 = 'vidagent_gpt_vidqa_tvp_base'
    results = os.listdir(f'results_{method1}')
    for result in results:
        get_answer(result, method1, method2)

main()