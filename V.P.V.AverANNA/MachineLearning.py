#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 
from sklearn.neural_network import MLPClassifier


# In[22]:


math_words = ['plu','equal','minus','subtraction','multiplication','radical','sinus'
              ,'cosine','integral','identical','math']
weather_words = ['weather','air','wind','rain','snow','sun','cloud','water']
clock_words = ['time','clock','alarm','stopwatch','timer']
email_words = ['email','send','gmail','yahoo']
anna_words = ['anna']
search_words = ['search','find','meaning']
browse_words = ['browse','url']
open_words = ['open','firefox','chrome','calculator','powerpoint','excel','word','office']


# In[23]:


datasheet = pd.DataFrame()


# In[24]:


rows = []


# In[25]:


ml_model = MLPClassifier(hidden_layer_sizes=(2))


# In[26]:


column_names = math_words+weather_words+clock_words+email_words+anna_words
column_names += search_words+browse_words+open_words+['target']


# In[27]:


def TxtToRows ():
    global rows
    file=open('sample-sentences.txt','r')
    lines = file.readlines()
    for i in range (len(lines)-1):
        line = lines[i].split(',')
        rows.append([line[0],int(line[1][:-1])])
    file.close()
    return


# In[28]:


def RowsToTxt ():
    global rows
    file = open('sample-sentences.txt','w')
    for i in range (len(rows)):
        file.write(rows[i][0]+','+str(rows[i][1])+'\n')
    file.close()
    return


# In[29]:


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
    


# In[30]:


def add_sample (sentence_list,sentence,target):
    global datasheet,column_names
    data=[0]*len(column_names)
    for i in range(len(column_names)-1):
        if column_names[i] in sentence_list:
            data[i]=1
    data[-1]=target
    datasheet.loc[sentence]=data
    return datasheet


# In[31]:


def make_sample (sentence_list,sentence):
    global column_names
    data=[0]*(len(column_names)-1)
    for i in range(len(column_names)-1):
        if column_names[i] in sentence_list:
            data[i]=1
    return data


# In[32]:


def predict_mode (sentence):
    global ml_model
    function_list = ['math','clock','weather','email','anna','search','browse','open','other']
    predict = ml_model.predict([make_sample(preprocessing(sentence),sentence)])
    return (function_list[int(predict)-1],int(predict))


# In[33]:


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


# In[34]:


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


# In[35]:


def FirstCou_Machine ():
    global math_words,weather_words,clock_words,datasheet,rows,ml_model,column_names
    TxtToRows()
    ps = PorterStemmer()
    for i in range (len(column_names)):
        column_names[i]=ps.stem(column_names[i])
        datasheet[column_names[i]]=[0]
    datasheet.drop(0,axis=0,inplace=True)
    for i in range (len(rows)):
        datasheet = add_sample(preprocessing(rows[i][0]),rows[i][0],rows[i][1])
    ml_model.fit(datasheet.drop('target',axis=1),datasheet['target'])
    return


# In[36]:


def UpdateML (sentence,target):
    global rows,datasheet
    rows += [[sentence,target]]
    for i in range (len(rows)):
        datasheet = add_sample(preprocessing(rows[i][0]),rows[i][0],rows[i][1])
    ml_model.fit(datasheet.drop('target',axis=1),datasheet['target'])
    return


# In[37]:


def MachineLearning (sentence,cou):
    if cou==1:
        FirstCou_Machine()
        (predSen,predNum)=predict_mode(sentence)
        UpdateML(sentence,predNum)
        print(predSen)
    else :
        (predSen,predNum)=predict_mode(sentence)
        UpdateML(sentence,predNum)
        print(predSen)
    RowsToTxt()
    return


# In[38]:


def Train_MachineLearning (sentence,cou,TrueTarget):
    # math=1 , clock=2 , weather=3 , email=4 , anna=5 , search=6 , browse=7 , open=8 , other=9
    if cou==1:
        FirstCou_Machine()
        (predSen,predNum)=predict_mode(sentence)
        print(predNum==TrueTarget)
        UpdateML(sentence,TrueTarget)
        print(predSen)
    else :
        (predSen,predNum)=predict_mode(sentence)
        print(predNum==TrueTarget)
        UpdateML(sentence,TrueTarget)
        print(predSen)
    RowsToTxt()
    return


# In[39]:


Train_MachineLearning("how's The Weather?",1,3)


# In[40]:


print("math=1 , clock=2 , weather=3 , email=4 , anna=5 , search=6 , browse=7 , open=8 , other=9")
for i in range (2,10):
    Train_MachineLearning(input("train sentence = "),i,int(input("target of this sentence = ")))


# In[41]:


print("math=1 , clock=2 , weather=3 , email=4 , anna=5 , search=6 , browse=7 , open=8 , other=9")
for i in range (10,20):
    Train_MachineLearning(input("train sentence = "),i,int(input("target of this sentence = ")))

