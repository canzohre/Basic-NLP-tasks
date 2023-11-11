import spacy
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg
import warnings
warnings.filterwarnings("ignore")
nlp=spacy.load('en_core_web_lg')
text=gutenberg.raw("bible-kjv.txt")
tokens=sent_tokenize(text)
sentence=input('enter a sentence:')
maxi=0
for token in tokens:
    token=nlp(token)
    sentence=nlp(sentence)
    similarity_degree=sentence.similarity(token)
    if similarity_degree>maxi:
        maxi=similarity_degree
        most_similar_sentence=token
print("most similar sentence in corpus is: ", most_similar_sentence)


