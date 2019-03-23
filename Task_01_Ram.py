#importing the libraries
import numpy as np
import pandas as pd

#importing the dataset (the file is in the form of .csv and saved in the same folder as this file)
dataset=pd.read_csv('breast-cancer.csv',names=['A','B','C','D','E','F','G','H','I','J'])

#creating the independent variable matrix (including the more relevant attributes and not all of them)
X=dataset.iloc[:,[0,1,2,3,4,6,7,8]].values

#creating the dependent variable matrix 
Y=dataset.iloc[:,9:10].values

#handling the categorical data
from sklearn.preprocessing import LabelEncoder,Imputer
label_encoder=LabelEncoder()
X[:,0]=label_encoder.fit_transform(X[:,0])
X[:,1]=label_encoder.fit_transform(X[:,1])
X[:,2]=label_encoder.fit_transform(X[:,2])
X[:,3]=label_encoder.fit_transform(X[:,3])
X[:,4]=label_encoder.fit_transform(X[:,4])
X[:,6]=label_encoder.fit_transform(X[:,6])
X[:,7]=label_encoder.fit_transform(X[:,7])

#creating training and testing sets
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

#importing the KNN classifier
from sklearn.neighbors import KNeighborsClassifier

#creating KNN object named classifier and training it
classifier=KNeighborsClassifier(n_neighbors=1)
classifier.fit(X_train,Y_train)

#evaluating the performance
training_score=classifier.score(X_train,Y_train)
testing_score=classifier.score(X_test,Y_test)

#printing the results
print("Training Score is {:f}%".format(training_score*100))
print("Testing Score is {:f}%".format(testing_score*100))
