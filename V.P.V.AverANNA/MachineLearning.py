#!/usr/bin/env python
# coding: utf-8

# In[244]:


import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 
from sklearn.neural_network import MLPClassifier
import keras
import tensorflow
import keras


# In[245]:


math_words = ['plu','equal','minus','subtraction','multiplication','radical','sinus'
              ,'cosine','integral','identical','math']
physics_words = ["electronic","magnetics","speed","meter","second","velocity"]
chemistry_words = ['Balance','H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']
clock_words = ['time','clock','alarm','stopwatch','timer','minute','hour']
email_words = ['email','send','gmail','yahoo']
anna_words = ['anna']
browse_words = ['browse','url']
open_words = ['open','firefox','chrome','calculator','powerpoint','excel','word','office']


# In[246]:


datasheet = pd.DataFrame()


# In[247]:


rows = []


# In[248]:


ml_model = ''


# In[277]:


#ml_model = keras.models.Sequential()
#ml_model.add(keras.layers.Dense(128, input_dim=276, activation='relu'))
#ml_model.add(keras.layers.Dense(256, activation='relu'))
#ml_model.add(keras.layers.Dense(512, activation='sigmoid'))
#ml_model.add(keras.layers.Dense(10, activation='softmax'))
#ml_model.compile(optimizer=keras.optimizers.Adam(lr=0.002), loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# In[250]:


column_names = math_words+clock_words+email_words+anna_words+physics_words+chemistry_words
column_names += browse_words+open_words+['target']
len(column_names)


# In[251]:


def TxtToRows ():
    global rows
    file=open('sample-sentences.txt','r')
    lines = file.readlines()
    for i in range (len(lines)-2):
        line = lines[i].split(',')
        rows.append([line[0],int(line[1][:-1])])
    file.close()
    return


# In[252]:


def RowsToTxt ():
    global rows
    file = open('sample-sentences.txt','w')
    for i in range (len(rows)):
        file.write(rows[i][0]+','+str(rows[i][1])+'\n')
    file.close()
    return


# In[253]:


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
    


# In[254]:


def add_sample (sentence_list,sentence,target):
    global datasheet,column_names
    data=[0]*len(column_names)
    for i in range(len(column_names)-1):
        if column_names[i] in sentence_list:
            data[i]=1
    data[-1]=target
    datasheet.loc[sentence]=data
    return datasheet


# In[255]:


def make_sample (sentence_list,sentence):
    global column_names
    data=[0]*(len(column_names)-1)
    for i in range(len(column_names)-1):
        if column_names[i] in sentence_list:
            data[i]=1
    return data


# In[256]:


def predict_mode (sentence):
    global ml_model
    # math=1 , clock=2 , email=3 , anna=4 , search=5 , browse=6 , open=7 , physics=8 , chemistry = 9
    function_list = ['math','clock','email','anna','search','browse','open','physics','chemistry']
    pred = np.argmax(ml_model.predict(np.array([make_sample(preprocessing(sentence),sentence)]).reshape(1,-1)))
    print (pred)
    return (function_list[int(pred)-1],int(pred))


# In[257]:


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


# In[258]:


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


# In[259]:


def math_predicts (sentence):
    return


# In[260]:


def physic_predicts (sentence):
    return


# In[261]:


def chmistry_predicts (sentence):
    return


# In[262]:


# math=1 , clock=2 , email=3 , anna=4 , search=5 , browse=6 , open=7 , physics=8 , chemistry = 9 ,other=10


# In[263]:


def email_predicts (sentence):
    return


# In[264]:


def clock_predicts (sentence):
    return


# In[265]:


def anna_predicts (sentence):
    return


# In[266]:


def search_predicts (sentence):
    return


# In[267]:


def browse_predicts (sentence):
    return


# In[268]:


def open_predicts (sentence):
    return


# In[276]:


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
    ml_model = keras.models.load_model("MLModel")
    return


# In[275]:


#def FirstCou_Machine ():
#    global math_words,weather_words,clock_words,datasheet,rows,ml_model,column_names
#    TxtToRows()
#    ps = PorterStemmer()
#    for i in range (len(column_names)):
#        if column_names.count(column_names[i])>1:
#            print(column_names.count(column_names[i]),i)
#        column_names[i]=ps.stem(column_names[i])
#        datasheet[column_names[i]]=[0]
#    datasheet.drop(0,axis=0,inplace=True)
#    for i in range (len(rows)):
#        datasheet = add_sample(preprocessing(rows[i][0]),rows[i][0],rows[i][1])
#    ml_model.fit(datasheet.drop('target',axis=1),datasheet['target'],epochs=50, shuffle=True)
#    return


# In[271]:


def UpdateML (sentence,target):
    global rows,datasheet
    rows += [[sentence,target]]
    for i in range (len(rows)):
        datasheet = add_sample(preprocessing(rows[i][0]),rows[i][0],rows[i][1])
    ml_model.fit(datasheet.drop('target',axis=1),datasheet['target'],epochs=50,shuffle=True)
    ml_model.save("MLModel")
    return


# In[272]:


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
    ml_model.save('MLModel')
    return


# In[273]:


def Train_MachineLearning (sentence,cou,TrueTarget):
    # math=1 , clock=2 , email=3 , anna=4 , search=5 , browse=6 , open=7 , physics=8 , chemistry = 9
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
    ml_model.save('MLModel')
    return


# In[ ]:





# In[ ]:





# In[ ]:




