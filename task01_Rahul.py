#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import csv
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from random import *


# In[2]:


with open("./breast-cancer.data") as file:
    rd=csv.reader(file)
    data=list(rd)
length=len(data)
i=0
while i<length:
    if '?' in data[i]:
        data.remove(data[i])
        length=length-1
        i=i-1
    i=i+1



# In[3]:


for i in data:
	if i[0]=='no-recurrence-events':
		i[0]=0
	else:
		i[0]=1

 	if i[2]=='lt40':
		i[2]=0
	elif i[2]=='ge40':
		i[2]=1
	else:
		i[2]=2
	if i[5]=='yes':
		i[5]=1
	else:
		i[5]=0
	
	if i[7]=='left':
		i[7]=0
	else:
		i[7]=1
	
	if i[8]=='left_up':
		i[8]=0
	elif i[8]=='left_low':
		i[8]=1
	elif i[8]=='right_up':
		i[8]=2
	elif i[8]=='right_low':
		i[8]=3
	elif i[8]=='central':
		i[8]=4
	
	
	if i[9]=='yes':
		i[9]=1
	else:
		i[9]=0
		


# In[4]:



with open("./breast-cancer_prepared.csv","w+") as file:
    wr = csv.writer(file)
    for i in data:
        wr.writerow(i)
df=pd.read_csv("./breast-cancer_prepared.csv",prefix="A",header=None)
df['A1']=df.groupby('A1').transform(lambda x: (x - x.mean()) / x.std())
df['A3']=df.groupby('A3').transform(lambda y: (y - y.mean()) / y.std())
df['A4']=df.groupby('A4').transform(lambda z: (z - z.mean()) / z.std())
df.to_csv("./breast-cancer_prepared.csv",index=False,header=False)
df.fillna(0,inplace=True)


# In[5]:



X=df.drop('A0',axis=1)
y=df.A0
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

train_acc=0.0
test_acc=0.0
for i in range (100):
	print("Test{}".format(i))
	X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=randint(1,100),test_size=0.3)
	knn = KNeighborsClassifier(n_neighbors=91,p=2)
	p = knn.fit(X_train,y_train)
	training_score = knn.score(X_train,y_train)
	train_acc=train_acc+training_score
	testing_score = knn.score(X_test,y_test)
	test_acc=test_acc+testing_score
	print("Training_score: {:.4f}%".format(training_score*100))
	print("Testing_score: {:.4f}%".format(testing_score*100))
train_acc=train_acc
test_acc=test_acc
print ("\n\nAverage Training Accuracy : {}\nAverage Testing Accuracy : {}".format(train_acc,test_acc))

