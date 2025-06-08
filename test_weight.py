import os
os.environ["HF_HOME"] = "/home/hice1/yxu846/scratch/models"
import sys
import json
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
  sys.path.append(module_path)

import pandas as pd
from tqdm import tqdm
import ast, copy, math
import numpy as np

from sentence_transformers import SentenceTransformer, util

# Load the model once
_model = SentenceTransformer("hkunlp/instructor-xl")

dataset = pd.read_csv('dataset/NExTVideo/test.csv')

folder_name = f'results_vidagent_gpt_all_multi_question'

def is_same(arr):
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False

def analyze_distribution(prob_dist):
    total = sum(prob_dist.values())
    max_key = max(prob_dist, key=prob_dist.get)
    max_val = prob_dist[max_key]
    return max_key, max_val / total if total != 0 else 0

def vote(weights, ratios, keys, choices):
    """
    Args:
        weights (List[float]): [w1, w2, w3]
        ratios  (List[float]): [r1, r2, r3], e.g. max_prob/total_prob per source
        keys    (List[str]):   [key1, key2, key3], top candidates per source
        choices (List[str]):   Candidate answers to pick from

    Returns:
        int: index in `choices` closest (by cosine) to the selected key.
    """
    # 1) Compute weighted scores and select best key
    scores = [w * r for w, r in zip(weights, ratios)]
    best_source = max(range(len(scores)), key=lambda i: scores[i])
    selected_key = keys[best_source]

    # 2) Embed selected key and all choices
    key_emb = _model.encode(selected_key, convert_to_tensor=True)
    choice_embs = _model.encode(choices, convert_to_tensor=True)

    # 3) Compute cosine similarities and pick best
    sims = util.cos_sim(key_emb, choice_embs)[0]  # shape: (len(choices),)
    return int(sims.argmax())

def test_acc():
    correctness = []
    for idx, row in tqdm(dataset.iterrows()):
        # test my method
        question = row['question'].capitalize() + '?'
        video_id = row['video']
        answer = row['answer']
        choices = [row['a0'], row['a1'], row['a2'], row['a3'], row['a4']]
        with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','r') as f:
             content = f.read()

        try:
            Prob_VQA = ast.literal_eval(content.split('Prob_VQA: ')[1].split('\n')[0].strip())
            Prob_CAP = ast.literal_eval(content.split('Prob_CAP: ')[1].split('\n')[0].strip())
            Prob_VIDQA = ast.literal_eval(content.split('Prob_VIDQA: ')[1].split('\n')[0].strip())
        except:
            predicted = int(content.split('\nAnswer: ')[1].split('\n')[0].strip())
            with open(f'{folder_name}_modified/{question.replace(" ","_")}_{video_id}.md','w') as f:
                f.write(content)
            if answer == predicted:
                correctness.append(1)
            else:
                correctness.append(0)
            continue

        max_vqa_key, max_vqa_ratio = analyze_distribution(Prob_VQA)
        max_cap_key, max_cap_ratio = analyze_distribution(Prob_CAP)
        max_vidqa_key, max_vidqa_ratio = analyze_distribution(Prob_VIDQA)

        answer1 = vote([1], [max_vqa_ratio], [max_vqa_key], choices)
        answer2 = vote([1], [max_cap_ratio], [max_cap_key], choices)
        answer3 = vote([1], [max_vidqa_ratio], [max_vidqa_key], choices)
        answers = [answer1, answer2, answer3]

        total_prob = copy.deepcopy(Prob_VIDQA)
        for key in Prob_CAP.keys():
            if key in total_prob:
                total_prob[key] += Prob_CAP[key]
        for key in Prob_VQA.keys():
            if key in total_prob:
                total_prob[key] += Prob_VQA[key]

        max_tot_key, max_tot_ratio = analyze_distribution(total_prob)

        if Prob_VIDQA[max_vidqa_key] >= 40 and max_vidqa_ratio > 0.5:
            predicted = vote([1], [max_vidqa_ratio], [max_vidqa_key], choices)
        else:
            if max_cap_key != max_vidqa_key or is_same([Prob_VIDQA[key] for key in Prob_VIDQA.keys()]):
                predicted = vote([0.5,1,1], [max_vqa_ratio, max_cap_ratio, max_vidqa_ratio], [max_vqa_key, max_cap_key, max_vidqa_key], choices)
                # if max_vqa_ratio / 2 > max(max_cap_ratio, max_vidqa_ratio) and Prob_VQA[max_vqa_key] >= 80:
                #     predicted = vote([1], [max_vqa_ratio], [max_vqa_key], choices)
                # else:
                #     predicted = vote([0,1,1], [max_vqa_ratio, max_cap_ratio, max_vidqa_ratio], [max_vqa_key, max_cap_key, max_vidqa_key], choices)
            else:
                predicted = vote([1], [max_vidqa_ratio], [max_vidqa_key], choices)

        # predicted = vote([1], [max_cap_ratio], [max_cap_key], choices)


        # if Prob_VIDQA[max_vidqa_key] >= 85:
        #     predicted = vote([1], [max_vidqa_ratio], [max_vidqa_key], choices)
        # elif Prob_VQA[max_vqa_key] >= 90:
        #     predicted = vote([1], [max_cap_ratio], [max_vqa_key], choices)
        # elif Prob_CAP[max_cap_key] >= 90:
        #     predicted = vote([1], [max_cap_ratio], [max_cap_key], choices)
        # elif max_vqa_key == max_vidqa_key or max_cap_key == max_vidqa_key:
        #     predicted = vote([1], [max_vidqa_ratio], [max_vidqa_key], choices)
        # elif max_cap_key == max_vqa_key:
        #     predicted = vote([1], [max_cap_ratio], [max_cap_key], choices)
        # else:
        #     predicted = vote([1,1,1], [max_vqa_ratio, max_cap_ratio, max_vidqa_ratio], [max_vqa_key, max_cap_key, max_vidqa_key], choices)
        # predicted = None

        # if max_vidqa_key == max_cap_key:
        #     predicted = vote([1], [max_vidqa_ratio], [max_vidqa_key], choices)
        # elif max_cap_key == max_vqa_key:
        #     predicted = vote([1], [max_cap_ratio], [max_cap_key], choices)
        # elif max_vqa_key == max_vidqa_key:
        #     predicted = vote([1], [max_vidqa_ratio], [max_vidqa_key], choices)
        # else:
        #     predicted = vote([1,1,2], [max_vqa_ratio, max_cap_ratio, max_vidqa_ratio], [max_vqa_key, max_cap_key, max_vidqa_key], choices)
        # predicted = vote([1], [max_vidqa_ratio], [max_vidqa_key], choices)
        # predicted = vote([1,1,2], [max_vqa_ratio, max_cap_ratio, max_vidqa_ratio], [max_vqa_key, max_cap_key, max_vidqa_key], choices)

        # if Prob_VIDQA[max_vidqa_key] >= 50:
        #     predicted = vote([1], [max_vidqa_ratio], [max_vidqa_key], choices)
        # else:
        #     if max_vqa_key != max_vidqa_key and max_cap_key != max_vidqa_key:
        #         predicted = vote([1,1,1], [max_vqa_ratio, max_cap_ratio, max_vidqa_ratio], [max_vqa_key, max_cap_key, max_vidqa_key], choices)
        #     else:
        #         predicted = vote([1], [max_vidqa_ratio], [max_vidqa_key], choices)

        with open(f'{folder_name}_modified/{question.replace(" ","_")}_{video_id}.md','w') as f:
            original = int(content.split('\nAnswer: ')[1].split('\n')[0].strip())
            f.write(content.replace(f'\nAnswer: {original}', f'\nAnswer: {predicted}'))

        if answer == predicted:
            correctness.append(1)
        else:
            # if answer == answer1:
            #     print(Prob_VQA)
            #     print(Prob_CAP)
            #     print(Prob_VIDQA)
            #     print(answer, choices[answer])
            #     print('\n')
            correctness.append(0)
    print(len(correctness))
    return sum(correctness) / len(correctness)

print(test_acc())