#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import csv 
import os


# In[3]:


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# In[4]:


with open("breast-cancer.data") as file:
    rd=csv.reader(file)
    data=list(rd)


# In[5]:


data


# In[6]:


data[:10]


# In[8]:


for i in data:
    print (i[1])


# In[9]:


for i in data:
    if(i[0]=="no-recurrence-events"):
        i[0]=0
    elif(i[0]=="recurrence-events"):
        i[0]=1


# In[10]:


data


# In[11]:


for i in data:
    if(i[1]=="10-19"):
        i[1]=15
    elif(i[1]=="20-29"):
        i[1]=25
    elif(i[1]=="30-39"):
        i[1]=35
    elif(i[1]=="40-49"):
        i[1]=45
    elif(i[1]=="50-59"):
        i[1]=55
    elif(i[1]=="60-69"):
        i[1]=65
    elif(i[1]=="70-79"):
        i[1]=75
    elif(i[1]=="80-89"):
        i[1]=85
    elif(i[1]=="90-99"):
        i[1]=95


# In[12]:


data


# In[13]:


for i in data:
    if(i[2]=="lt40"):
        i[2]=0
    elif(i[2]=="ge40"):
        i[2]=1
    elif(i[2]=="premeno"):
        i[2]=2


# In[14]:


data


# In[15]:


for i in data:
    if(i[3]=="0-4"):
        i[3]=2
    elif(i[3]=="5-9"):
        i[3]=7
    elif(i[3]=="10-14"):
        i[3]=12
    elif(i[3]=="15-19"):
        i[3]=17
    elif(i[3]=="20-24"):
        i[3]=22
    elif(i[3]=="25-29"):
        i[3]=27
    elif(i[3]=="30-34"):
        i[3]=32
    elif(i[3]=="35-39"):
        i[3]=37
    elif(i[3]=="40-44"):
        i[3]=42
    elif(i[3]=="45-49"):
        i[3]=47
    elif(i[3]=="50-54"):
        i[3]=52
    elif(i[3]=="55-59"):
        i[3]=57


# In[16]:


data


# In[17]:


for i in data:
    if(i[4]=="0-2"):
        i[4]=1
    elif(i[4]=="3-5"):
        i[4]=4
    elif(i[4]=="6-8"):
        i[4]=7
    elif(i[4]=="9-11"):
        i[4]=10
    elif(i[4]=="12-14"):
        i[4]=13
    elif(i[4]=="15-17"):
        i[4]=16
    elif(i[4]=="18-20"):
        i[4]=19
    elif(i[4]=="21-23"):
        i[4]=22
    elif(i[4]=="24-26"):
        i[4]=25
    elif(i[4]=="27-29"):
        i[4]=28
    elif(i[4]=="30-32"):
        i[4]=31
    elif(i[4]=="33-35"):
        i[4]=34
    elif(i[4]=="36-39"):
        i[4]=37


# In[18]:


data


# In[19]:


for i in data:
    if(i[5]=="yes"):
        i[5]=1
    elif(i[5]=="no"):
        i[5]=0


# In[20]:


data


# In[21]:


for i in data:
    if(i[7]=="left"):
        i[7]=1
    elif(i[7]=="right"):
        i[7]=0


# In[22]:


data


# In[23]:


for i in data:
    if(i[8]=="left_low"):
        i[8]=0
    elif(i[8]=="left_up"):
        i[8]=1
    elif(i[8]=="right_low"):
        i[8]=2
    elif(i[8]=="right_up"):
        i[8]=3
    elif(i[8]=="central"):
        i[8]=4


# In[24]:


data


# In[25]:


for i in data:
    if(i[9]=="yes"):
        i[9]=1
    elif(i[9]=="no"):
        i[9]=0


# In[26]:


data


# In[27]:


for i in data:
    i[1]=(i[1]-55)/80


# In[28]:


data


# In[29]:


for i in data:
    i[3]=(i[3]-29.5)/55


# In[30]:


for i in data:
    i[4]=(i[4]-19)/36


# In[31]:


data


# In[32]:


with open("breast_cancer_prepared.csv","w+") as file:
    wr=csv.writer(file)
    for i in range(len(data)):
        wr.writerow(data[i])


# In[33]:


data=pd.read_csv("breast_cancer_prepared.csv",names=["A","B","C","D","E","F","G","H","I","J"])


# In[34]:


data.drop(data.F=='?')


# In[35]:


data.drop("F"=='?')


# In[36]:


data


# In[37]:


data.F


# In[62]:


i=data[(data.F=='?')].index


# In[63]:


i


# In[64]:


data=data.drop(i)


# In[65]:


i=data[(data.I=='?')].index


# In[66]:


i


# In[67]:


data.iloc[[206]]


# In[69]:


data.drop(206)


# In[74]:


data


# In[71]:


X=data.drop("A",axis=1)


# In[72]:


y=data.A


# In[73]:


X.head


# In[75]:


X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=32)


# In[76]:


knn=KNeighborsClassifier(n_neighbors=20)


# In[77]:


p=knn.fit(X_train,y_train)


# In[78]:


training_score=knn.score(X_train,y_train)


# In[79]:


training_score


# In[80]:


test_score=knn.score(X_test,y_test)


# In[81]:


test_score


# In[ ]:




