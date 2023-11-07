import nltk
from nltk.tokenize import word_tokenize ,sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from operator import itemgetter

f=open('1984_summary.txt','r',encoding='UTF-8')
text=f.read()
tokenizer = RegexpTokenizer(r'\w+')
sentences=sent_tokenize(text)
tokens=tokenizer.tokenize(text)
stop_words=set(stopwords.words("english"))
temp=[]
for token in tokens:
    if token not in stop_words:
        temp.append(token)
tokens=temp


word_freq=nltk.FreqDist(tokens)
keys_list= list(word_freq.keys())
length=int(len(keys_list)*0.1)
most_freq_words = dict(sorted(word_freq.items(), key = itemgetter(1), reverse = True)[:length])
words=list(most_freq_words.keys())

text_summary=[]
for word in words:
  for sentence in sentences:
    if word in sentence:
        if sentence in text_summary:
            pass
        else:
            text_summary.append(sentence)
            
print(','.join(text_summary))
        

    
    





    



