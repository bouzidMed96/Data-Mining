#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:12:44 2019

@author: 11813288
""bouzidMed"""
from math import sqrt
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plot
import numpy as np
#from sklearn import cross_validation  
from sklearn import *
from array import array
  


#step 1: load the dataset
iris = datasets.load_iris() 
def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated
#step 2 important functions
def summarize_by_class(dataset):
	separated = separate_by_class(dataset)
	summaries = dict()
	for class_value, rows in separated.items():
		summaries[class_value] = manup(rows)
	return summaries
#function that computes the mean(average value) of set of data
def mean(x):
    return sum(x) / float(len(x))

#function that computes the standard deviation of a list     of numbers
def standardDev(x):
    moy = mean(x)
    sum = 0
    for i in x:
        sum+= (i-moy)**2
    variance = sum / float(len(x)-1)
    stdev = sqrt(variance)
    return stdev
 
#Compute the sum,var and lenght of each table of the dataSet and set them in a tuple
def manup(X):
    summaries = [(mean(i), standardDev(i), len(i)) for i in zip(*X)]
    return summaries

#step 3 summarize by class



tn = iris.target_names[iris.target]
zipped = zip(*iris.data)
s= manup(iris.data)
tab1=array('d')
tab2=[]
tab3=[]
#tab1.append(iris.data[0])

   
print(separate_by_class(iris.data))
#summarize the dataset
