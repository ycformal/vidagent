import nltk
from nltk import word_tokenize, pos_tag
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet as wn
import numpy as np
import string
from gensim.models import KeyedVectors

# If you haven’t already, run these once:
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

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

def preprocess_sentence(sent, stemmer,
                        det_tags={'DT'},
                        preserve={'beginning', 'end', 'middle'}):
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
        # 1) skip punctuation
        if word in string.punctuation:
            continue
        # 2) preserve special tokens verbatim
        if word in preserve:
            mapped.append(word)
            continue
        # 3) drop determiners
        if tag in det_tags:
            continue
        # 4) drop adjectives
        if tag.startswith('JJ'):
            continue
        # 5) drop nouns
        if tag.startswith('NN'):
            continue
        # 6) drop verbs & non-temporal prepositions
        if tag.startswith('VB') or (tag == 'IN' and not is_temporal(word)):
            continue
        if is_temporal(word):
            mapped.append(stemmer.stem(word))
            mapped.append(stemmer.stem(word))
        # 7) otherwise, stem the word
        mapped.append(stemmer.stem(word))

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

def main():
    # Your 16 sentences
    sentences = [
        "How many children are in the video?",
        "Why is the blue sweater guy looking at the shirtless men?",
        "Why does the man have to throw the plane first in the middle of the video?",
        "What does the man in checkered do after walking onto the stage with microphone stands at the start?",
        "What does the man do after grabbing the boy near the end?",
        "What does the man do after showing the pancake?",
        "What does the man playing the drums do with his feet as he plays the drum?",
        "How is the man in grey plaid shirt feeling while talking at the start?",
        "How did the boy respond when he saw the girl dancing at the middle of the video?",
        "Where is this video taken?",
        "Where did the man in grey rest his hand before he started walking forward?",
        "What did the baby do before she put the green long toy in her mouth at the middle of the video?",
        "What did the boy with green car do before he pushed his car the second time?",
        "How did the man ensure that he could see the baby clearly?",
        "How did the lady in pink assist the bride in the activity at the beginning?",
        "How did the guy on the board manage to not fall off from the board at the start of the video?"
    ]

    stemmer = PorterStemmer()

    # 1) Load your pre-trained word vectors
    #    Replace the path below with your actual .bin or .txt file
    embeddings = KeyedVectors.load_word2vec_format(
        'GoogleNews-vectors-negative300.bin', binary=True
    )

    # 2) Preprocess & embed stored sentences
    stored_tokens = [preprocess_sentence(s, stemmer) for s in sentences]
    stored_vecs   = np.vstack([
        sentence_vector(toks, embeddings)
        for toks in stored_tokens
    ])

    # 3) Query loop
    query = input("Enter a sentence: ").strip()
    query_tokens = preprocess_sentence(query, stemmer)
    query_vec    = sentence_vector(query_tokens, embeddings)

    # 4) Compute cosine similarities
    sims = np.array([
        cosine_sim(query_vec, vec)
        for vec in stored_vecs
    ])

    # 5) Retrieve top-8
    top_idxs = np.argsort(sims)[::-1][:8]
    print("\nTop 8 most similar sentences:\n")
    for idx in top_idxs:
        print(f"{sims[idx]:.3f} — {sentences[idx]}")

if __name__ == "__main__":
    main()
