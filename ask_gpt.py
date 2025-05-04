import openai
key = "tl.qspk.W5DyWbibnie1gou72KsNFzm2xtUltPk3bLuROweJsThTbc[IfLY:nogngujZVN{[ljus5rjxdLU4CmclGK{BHtxj`vvD6PLQiyZ1121yskCtUEk9bjQXX3.B1`25:4NQ[fuNnJGBdwMQHK[Tewgt:e4h.SNB"
key = ''.join([chr(ord(k)-1) for k in key])
openai.api_key=key

question = "How did the woman feel when feeding the girl who is sleeping on the couch?"
information = ['happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'sad', 'sad', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'sad', 'sad']
choices = ['found it funny', 'confused', 'worried', 'shocked', 'pleased']
prompt = f"You are doing a video QA task.\nQuestion: {question}\nBased on the information on potential relative frames {information}, your task is to estimate the correctness of each choice in {choices}. Note that the answers may not be absolutely correct, so each choice has possibility, and it is possible that all choices have a low possibility. Your response must should be a json:\n{{\"reasoning\": \"<Your think step-by-step reasoning>\", \"possibility\": <A dict of estimated possibility distribution of each answer in format answer: possibility (0-100)>}}"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0,
    max_tokens=1000,
)

print(response['choices'][0]['message']['content'])

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "user", "content": prompt},
#         {"role": "assistant", "content": response['choices'][0]['message']['content']},
#         {"role": "user", "content": "Then why are you assigning the highest score to run. Tell me the reason"}
#     ],
#     temperature=0,
#     max_tokens=1000,
# )

# print(response['choices'][0]['message']['content'])