import random
from nltk import word_tokenize, pos_tag
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet as wn
import numpy as np
import string
from gensim.models import KeyedVectors
from sentence_transformers import SentenceTransformer, util

GQA_CURATED_EXAMPLES=[
"""Question: How many children are in the video?
Program:
ANSWERS0=VQA(video=VIDEO,question="How many children are there?")
ANSWER0=SELECT(question="How many children are in the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", # DC
"""Question: Why is the blue sweater guy looking at the shirtless men?
Program:
FRAME0=LOC(video=VIDEO,event="A blue sweater guy is looking at the shirtless men.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Why is the blue sweater guy looking at the shirtless men?")
ANSWER0=SELECT(question="Why is the blue sweater guy looking at the shirtless men?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", #CW
"""Question: Why does the man have to throw the plane first in the middle of the video?
Program:
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
ANSWERS0=VQA(video=VIDEO0,question="Why does the man have to throw the plane first?")
ANSWER2=SELECT(question="Why does the man have to throw the plane first in the middle of the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER2)
""", #CW
"""Question: What does the man in checkered do after walking onto the stage with microphone stands at the start?
Program:
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="The man in checkered has walked onto the stage with microphone stands.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man in checkered doing?")
ANSWER0=SELECT(question="What does the man in checkered do after walking onto the stage with microphone stands at the start?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", #TN
"""Question: What does the man do after grabbing the boy near the end?
Program:
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,event="The man has grabbed the boy.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man doing?")
ANSWER1=SELECT(question="What does the man do after grabbing the boy near the end?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER1)
""", #TN
"""Question: What does the man do after showing the pancake?
Program:
FRAME0=LOC(video=VIDEO,event="The man has shown the pancake.")
VIDEO1=CLIP_AFTER(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man doing?")
ANSWER0=SELECT(question="What does the man do after showing the pancake?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", #TN
"""Question: What does the man playing the drums do with his feet as he plays the drum?
Program:
FRAME0=LOC(video=VIDEO,event="A man is playing the drums.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the man playing the drums doing with his feet?")
ANSWER0=SELECT(question="What does the man playing the drums do with his feet as he plays the drum?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", #TC
"""Question: How is the man in grey plaid shirt feeling while talking at the start?
Program:
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="A man in grey plaid shirt is talking.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the man in grey plaid shirt feeling?")
ANSWER0=SELECT(question="How is the man in grey plaid shirt feeling while talking at the start?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", #TC
"""Question: How did the boy respond when he saw the girl dancing at the middle of the video?
Program:
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The boy is seeing the girl dancing.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the boy responding?")
ANSWER2=SELECT(question="How did the boy respond when he saw the girl dancing at the middle of the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER2)
""", #TC
"""Question: Where is this video taken?
Program:
ANSWERS0=VQA(video=VIDEO,question="Where is it?")
ANSWER0=SELECT(question="Where is this video taken?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", #DL
"""Question: Where did the man in grey rest his hand before he started walking forward?
Program:
FRAME0=LOC(video=VIDEO,event="The man in grey has started walking forward.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Where is the man in grey resting his hand?")
ANSWER0=SELECT(question="Where did the man in grey rest his hand before he started walking forward?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", #TP
"""Question: What did the baby do before she put the green long toy in her mouth at the middle of the video?
Program:
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The baby has put the green long toy in her mouth.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the baby doing?")
ANSWER2=SELECT(question="What did the baby do before she put the green long toy in her mouth at the middle of the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER2)
""", #TP
"""Question: What did the boy with green car do before he pushed his car the second time?
Program:
FRAME0=LOC(video=VIDEO,event="The boy with green car has pushed his car the second time.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the boy with green car doing?")
ANSWER0=SELECT(question="What did the boy with green car do before he pushed his car the second time?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", #TP
"""Question: How did the man ensure that he could see the baby clearly?
Program:
ANSWERS0=VQA(video=VIDEO,question="How is the man ensuring that he can see the baby clearly?")
ANSWER0=SELECT(question="How did the man ensure that he could see the baby clearly?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", #DO
"""Question: How did the lady in pink assist the bride in the activity at the beginning?
Program:
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="The lady in pink is assisting the bride in the activity.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the lady in pink assisting the bride in the activity?")
ANSWER0=SELECT(question="How did the lady in pink assist the bride in the activity at the beginning?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""", #CH
"""Question: How did the guy on the board managed to not fall off from the board at the start of the video?
Program:
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
ANSWERS0=VQA(video=VIDEO0,question="How is the guy on the board managing to not fall off from the board?")
ANSWER0=SELECT(question="How did the guy on the board managed to not fall off from the board at the start of the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""" #DO
]

questions = [line.split('\n')[0].split("Question: ")[-1].strip() for line in GQA_CURATED_EXAMPLES]

def is_temporal(word):
    """
    Return True if any WordNet synset for `word`
    has 'time' in its lexname or definition.
    """
    if word in ['as']:
        return True
    for ss in wn.synsets(word):
        if 'time' in ss.lexname() or 'time' in ss.definition().lower():
            return True
    return False

TEMPORAL_EQUIVALENCE_GROUPS = [
    {"before", "prior", "earlier"},
    {"after", "later", "subsequently"},
    {"while", "as", "when", "during"}
]

def normalize_temporal_token(word):
    for group in TEMPORAL_EQUIVALENCE_GROUPS:
        if word in group:
            return list(group)[0]  # pick one canonical form
    return ''


def boosted_similarity(query, example, boost_weight=0.1):
    # Embedding-based similarity
    emb_query = model.encode(query, normalize_embeddings=True)
    emb_example = model.encode(example, normalize_embeddings=True)
    base_sim = util.cos_sim(emb_query, emb_example).item()

    # Temporal word overlap with equivalence grouping
    t_query = extract_normalized_temporals(query)
    t_example = extract_normalized_temporals(example)
    print(example, t_example)
    overlap = t_query & t_example
    
    bonus = boost_weight * len(overlap)
    if len(overlap) == 0 and len(t_query) > 0 and len(t_example) > 0:
        bonus = -boost_weight / 1.5

    return base_sim + bonus


def extract_normalized_temporals(sentence):
    tokens = word_tokenize(sentence.lower())
    temporal_words = [normalize_temporal_token(w) for w in tokens]
    temporal_words = [w for w in temporal_words if w != '']
    return set(temporal_words)


def preprocess_sentence(sent, stemmer,
                        det_tags={'DT'},
                        preserve={'beginning', 'start', 'end', 'middle'}):
    """
    Tokenize, POS-tag, remove punctuation,
    drop determiners, drop adjectives/nouns/verbs (unless 'IN' is temporal),
    preserve listed words, stem everything else.
    Returns a list of tokens.
    """
    tokens = word_tokenize(sent.lower())
    tagged = pos_tag(tokens)
    mapped = []

    for word, tag in tagged:
        # # 1) skip punctuation
        # if word in string.punctuation:
        #     continue
        # # 2) preserve special tokens verbatim
        # if word in preserve:
        #     mapped.append(word)
        #     continue
        # # 3) drop determiners
        # if tag in det_tags or tag.startswith('JJ') or tag.startswith('NN') or tag.startswith('VB') or (tag == 'IN' and not is_temporal(word)) or tag.startswith('PRP'):
        #     continue
        # if is_temporal(word):
        #     mapped.extend([word] * 9)
        # if word in preserve:
        #     mapped.extend([word] * 4)
        # # 7) otherwise, stem the word
        mapped.append(word)

    return mapped

def sentence_vector(tokens, embeddings):
    """
    Average the embeddings for each token present
    in the pre-trained model. Falls back to zero vec.
    """
    vecs = [embeddings[w] for w in tokens if w in embeddings]
    if not vecs:
        return np.zeros(embeddings.vector_size, dtype=float)
    return np.mean(vecs, axis=0)

def cosine_sim(v1, v2):
    """Cosine similarity between two 1-D numpy arrays."""
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return np.dot(v1, v2) / (norm1 * norm2)

stemmer = PorterStemmer()

# # 1) Load your pre-trained word vectors
# #    Replace the path below with your actual .bin or .txt file
# embeddings = KeyedVectors.load_word2vec_format(
# 'GoogleNews-vectors-negative300.bin', binary=True
# )

# # 2) Preprocess & embed stored sentences
# stored_tokens = [preprocess_sentence(s, stemmer) for s in questions]
# stored_vecs   = np.vstack([
#     sentence_vector(toks, embeddings)
#     for toks in stored_tokens
# ])

def create_prompt(inputs,num_prompts=10):
    # 3) Query loop
    query = inputs['question']
    query_tokens = preprocess_sentence(query, stemmer)
    query_vec    = sentence_vector(query_tokens, embeddings)

    # 4) Compute cosine similarities
    sims = np.array([
        cosine_sim(query_vec, vec)
        for vec in stored_vecs
    ])

    # 5) Retrieve top-10
    top_idxs = np.argsort(sims)[::-1][:10]
    prompt_examples = [GQA_CURATED_EXAMPLES[idx] for idx in top_idxs]
    print("\nTop 10 most similar sentences:\n")
    for idx in top_idxs:
        print(f"{sims[idx]:.3f} — {questions[idx]}")

    prompt_examples = '\n'.join(prompt_examples)
    prompt_examples = f'Think step by step to answer the question.\n\n{prompt_examples}'


    return prompt_examples + "\nQuestion: {question}\nProgram:\n".format(**inputs)

# Load sentence embedding model (instructor-xl, mpnet, or any SBERT)
model = SentenceTransformer("hkunlp/instructor-xl")  # fast, accurate. Try "instructor-xl" for stronger

def sort_by_similarity_and_length(examples, scores):
    """
    examples: list of full example strings
    scores: list of similarity scores (higher = more similar)
    """
    return sorted(
        zip(examples, scores),
        key=lambda x: (-x[1], len(x[0].splitlines()))  # sort by descending sim, then ascending length
    )


def create_prompt(inputs, num_prompts=10):
    query = inputs['question']
    sims = [
        boosted_similarity(query, candidate_q)
        for candidate_q in questions
    ]
    top_idxs = np.argsort(sims)[::-1][:num_prompts]

    for idx in top_idxs:
        print(f"{sims[idx]:.3f} — {questions[idx]}")

    top_idxs = np.array(top_idxs, dtype=int)
    examples = [GQA_CURATED_EXAMPLES[i] for i in top_idxs]
    scores   = [sims[i] for i in top_idxs]
    sorted_examples = sort_by_similarity_and_length(examples, scores)
    prompt_block = '\n'.join(ex[0] for ex in sorted_examples)
    print(prompt_block)
    return f"Think step by step to answer the question.\n\n{prompt_block}\nQuestion: {query}\nProgram:\n"
