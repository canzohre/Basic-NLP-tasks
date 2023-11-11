import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()
stop_words=set(stopwords.words("turkish"))
simple_dict={'boğaz':['Boynun ön bölümü ve bu bölümü oluşturan organlar, imik, kursak','İki dağ arasında dar geçit'],
             'pazar':['Satıcıların belirli günlerde mallarını satmak için sergiledikleri belirli geçici yer','Cumartesi ile pazartesi arasındaki gün']}

def remove_stopwords(tokens):
 _temp=tokens
 tokens=[]
 for token in _temp:
     if token not in stop_words:
         tokens.append(token)
 return tokens
         
         
boğaz_senses=simple_dict['boğaz']
pazar_senses=simple_dict['pazar']
tokens_boğaz1=word_tokenize(boğaz_senses[0])
tokens_boğaz2=word_tokenize(boğaz_senses[1])
tokens_pazar1=word_tokenize(pazar_senses[0])
tokens_pazar2=word_tokenize(pazar_senses[1])

remove_stopwords(tokens_boğaz1)
remove_stopwords(tokens_boğaz2)
remove_stopwords(tokens_pazar1)
remove_stopwords(tokens_pazar2)

words_boğaz1=[]
for token in tokens_boğaz1:
    word=ps.stem(token)
    words_boğaz1.append(word)
    
words_boğaz2=[]
for token in tokens_boğaz2:
   word= ps.stem(token)
   words_boğaz2.append(word)

words_pazar1=[]
for token in tokens_pazar1:
    word=ps.stem(token)
    words_pazar1.append(word)

words_pazar2=[]
for token in tokens_pazar2:
    word=ps.stem(token)
    words_pazar2.append(word)

boğaz1=set(words_boğaz1)
boğaz2=set(words_boğaz2)
pazar1=set(words_pazar1)
pazar2=set(words_pazar2)
final_dict={'boğaz':[boğaz1,boğaz2],'pazar':[pazar1,pazar2]}


 
def lesk(word,sentence):    
      
      max=0
      index=0
      
      for i in range(len(final_dict[word])):
       count=len(final_dict[word][i].intersection(sentence))
       if count>max:
        max=count
        index=i
      
      print('definition of the word for this sentence is:  ',simple_dict[word][index])
    
      
sample_sentence="pazar annemin en sevdiği gün"
sent=word_tokenize(sample_sentence)
sent=set(sent)
ambiguity=input("enter a word that create ambiguity ")
lesk(ambiguity,sent) 






 
    
    


    
    



           
   