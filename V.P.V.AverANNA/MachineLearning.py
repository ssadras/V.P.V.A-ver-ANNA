#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 
from sklearn.neural_network import MLPClassifier


# In[41]:


def preprocessing (sentence):
    ps = PorterStemmer()
    process_sen = []
    sentence=word_tokenize(sentence)
    remove_words=['!','.','i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']
    for i in range(len(sentence)):
        if not(sentence[i] in remove_words):
            try:
                int(sentence[i])
            except:
                process_sen.append(ps.stem(sentence[i]))
    return (process_sen)
    


# In[42]:


math_words = ['plu','equal','minus','subtraction','multiplication','radical','sinus'
              ,'cosine','integral','identical','math']
weather_words = ['weather','air','wind','rain','snow','sun','cloud','water']
clock_words = ['time','clock','alarm','stopwatch','timer']


# In[43]:


datasheet = pd.DataFrame()


# In[44]:


def add_sample (sentence_list,sentence,target):
    global datasheet,column_names
    data=[0]*len(column_names)
    for i in range(len(column_names)-1):
        if column_names[i] in sentence_list:
            data[i]=1
    data[-1]=target
    datasheet.loc[sentence]=data
    return datasheet


# In[45]:


rows = [['2 plus 2 equals what',1],['what time is it ?',2]
        ,['how is the weather ?',3],['how are you ?',4]
       ,['4 multiplication 2 equals waht',1],['radical of 2',1]
        ,['sinus of 2 equals waht ?',1],['is it sunny ?',3],['is it cloudy ?',3],['is it rainy ?',3]
        ,['set an event from 8 o\'clock to 10 o\'clock',2],['start stopwatch.',2],['set a 5 minute timer',2]]


# In[46]:


ml_model = MLPClassifier(hidden_layer_sizes=(2))


# In[47]:


def make_sample (sentence_list,sentence):
    global column_names
    data=[0]*(len(column_names)-1)
    for i in range(len(column_names)-1):
        if column_names[i] in sentence_list:
            data[i]=1
    return data


# In[48]:


def predict_mode (sentence):
    global ml_model
    function_list = ['math','clock','weather','other']
    predict = ml_model.predict([make_sample(preprocessing(sentence),sentence)])
    for i in range (len(function_list)):
        if predict==i+1:
            return function_list[i]


# In[49]:


def radical_order (sentence):
    sentence_list=sentence.split()
    if 'order' in sentence_list:
        for i in range (len(sentence_list)):
            if sentence_list[i]=='order' and i+1<len(sentence_list):
                try :
                    int(sentence_list[i+1])
                    output='**(1 / '+sentence_list[i+1]+')'
                    sentence_list[i+1]='None'
                    return (output,sentence_list)
                except:
                    if i-1>=0:
                        try :
                            int(sentence_list[i-1])
                            output='**(1 / '+sentence_list[i-1]+')'
                            sentence_list[i-1]='None'
                            return (output,sentence_list)
                        except:
                            2+2
    else:
        return ("**0.5",sentence_list)


# In[50]:


def change_math_predict_mode (sentence):
    sentence_list=sentence.split()
    change_words = [['plus','+'],['equal','='],['radical','function']]
    output=''
    for i in range (len(sentence_list)):
        for j in range (len(change_words)):
            try :
                output+=str(int(sentence_list[i]))
                break
            except:
                if (change_words[j][0] in sentence_list[i]) and change_words[j][0]!='radical':
                    output+=change_words[j][1]
                    break
                if (change_words[j][0]==sentence_list[i]) and change_words[j][0]=='radical':
                    output+=sentence_list[i+1]
                    rad=radical_order(sentence)
                    output+=rad[0]
                    sentence_list=rad[1]
                    sentence_list[i+1]='None'
                    break
    return output


# In[51]:


def FirstCou_Machine ():
    global math_words,weather_words,clock_words,datasheet,rows,ml_model
    column_names = math_words+weather_words+clock_words+['target']
    ps = PorterStemmer()
    for i in range (len(column_names)):
        column_names[i]=ps.stem(column_names[i])
        datasheet[column_names[i]]=[0]
    datasheet.drop(0,axis=0,inplace=True)
    for i in range (len(rows)):
        datasheet = add_sample(preprocessing(rows[i][0]),rows[i][0],rows[i][1])
    ml_model.fit(datasheet.drop('target',axis=1),datasheet['target'])
    return


# In[52]:


def MachineLearning (sentence,cou):
    if cou==1:
        FirstCou_Machine()
        print(predict_mode(sentence))
    else :
        print(predict_mode(sentence))
    return


# In[ ]:





# In[ ]:




