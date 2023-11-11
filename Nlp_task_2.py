import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import enchant
import numpy
import pandas




f=open('ince_memed_1.txt','r',encoding='UTF8')
text=f.read()
tokenizer = RegexpTokenizer(r'\w+')
tokens=tokenizer.tokenize(text)
stop_words=set(stopwords.words('turkish')
low_freqlist = []  
highfreqlist = []    
            
               
def removestopwords(words):
    temp=[]
    for token in words:
       if token not in stop_words:
           temp.append(token)
    words=temp    

    
def get_unigram(words):
    global low_freqlist
    global high_freqlist
     threshold=5
     unigram_freq=nltk.FreqDist(words)
   for token in unigram_freq.keys():
     if unigram_freq[token]>=threshold:
         high_freqlist.append(token)
     else:
         low_freqlist.append(token)
         
def similarity_matrix(list1,list2):
 similarity_list=[]   
 for i in range(len(list1)):
     similarity_list[i].append(list1[i])
     minimum=100
     index=0
     for j in range(len(list2)): ],list2[j])moves=enchant.utils.levenshtein(list1[i])
       if moves<minimum:
           minimum=moves
           index=j
     similarity_list[i].append(list2[index])  
     
 return similarity_list  
           
         


