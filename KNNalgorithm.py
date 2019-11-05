#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:12:44 2019

@author: 11813288
""bouzidMed"""

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plot
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import *  




iris = datasets.load_iris() 
X_iris = iris.data
Y_iris = iris.target
species= iris.target_names

plot.title("titre")
plot.scatter(iris.data[: , 0], iris.data[: , 1] , marker = 'o' , c = iris.target, s=100, edgecolor='k')
plot.xlabel("x-label")
plot.ylabel("y-label")
plot.show()


def PVV1(X,Y):#K = 1
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y) 
    classifer = neighbors.KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    classifer.fit(X_train,Y_train)
    prediction = classifer.predict(X_test)
    accurancy = classifer.score(X_test,Y_test)
    erreur_prediction = 1 - accurancy
    print(erreur_prediction)
    
def PVV3(X,Y):#K = 3
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y) 
    classifer = neighbors.KNeighborsClassifier(n_neighbors=3, metric='euclidean')
    classifer.fit(X_train,Y_train)
    prediction = classifer.predict(X_test)
    accurancy = classifer.score(X_test,Y_test)
    erreur_prediction = 1 - accurancy
    print(erreur_prediction)
    
if __name__ == "__main__":
    # execute only if run as a script
    PVV1(X_iris,Y_iris)
    PVV3(X_iris,Y_iris)
