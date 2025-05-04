import openai
def judge(results, question, show_analysis=False):
    prompt = f"""Caption: {results['caption']}\n\nThink step by step. From the information provided in the caption, can we know the answer to the question "{question}"? You should analyze the question, analyze the caption, and give me the answer. Note that you cannot assume things that are not mentioned in the caption."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    analysis = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(analysis)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": analysis
            },
            {
                "role": "user",
                "content": f"Question: {question}\nLLM visual agent's answer: \"{results['agent']['answer']}\"\n\nFollow the instructions below to give me the answer.\n- If we got an answer from the caption in the previous analysis, then give me the answer inferred from the caption.\n- If the previous analysis says the caption lacks essential information to get the answer, then give me the answer \"{results['agent']['answer']}\", which is the LLM\'s result.\n\nThink step by step. You should strictly follow the above steps and provide your chain of thought."
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    analysis2 = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(analysis2)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": analysis
            },
            {
                "role": "user",
                "content": f"Question: {question}\nLLM visual agent's answer: \"{results['agent']['answer']}\"\n\nFollow the instructions below to give me the answer.\n- If we got an answer from the caption in the previous analysis, then give me the answer inferred from the caption.\n- If the previous analysis says the caption lacks essential information to get the answer, then give me the answer \"{results['agent']['answer']}\", which is the LLM\'s result.\n\nThink step by step. You should strictly follow the above steps and provide your chain of thought."
            },
            {
                "role": "assistant",
                "content": analysis2
            },
            {
                "role": "user",
                "content": f'Based on all the information, give me the answer to question "{question}". Only give me the answer and do not include additional words. You must give me a definite answer and cannot say the answer is not determined. In case the answer cannot be determined from the caption, your answer should be the LLM\'s result, which is "{results["agent"]["answer"]}". Your answer:'
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    return response['choices'][0]['message']['content'].strip()