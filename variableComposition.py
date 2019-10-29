#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:26:36 2019

@author: BouzidMed
""" 
from sklearn import *
import matplotlib.pyplot as plt
from sklearn.preprocessing import *
import numpy as np


    
def C():
    
    iris = datasets.load_iris() 
    
    plot.title('first combo')
    plot.scatter(iris.data[: , 0], iris.data[: , 1] , marker = 'o' , c = iris.target, s=100, edgecolor='k')
    plot.xlabel("x label")
    plot.ylabel("y-label")
    plot.title("titre")
    plot.show()
    
    plot.title('second combo')
    plot.scatter(iris.data[: , 0], iris.data[: , 2] , marker = 'o' , c = iris.target, s=100, edgecolor='k')
    plot.xlabel("x label")
    plot.ylabel("y-label")
    plot.title("titre")
    plot.show()
    
    
    plot.title('third combo')
    plot.scatter(iris.data[: , 0], iris.data[: , 3] , marker = 'o' , c = iris.target, s=100, edgecolor='k')
    plot.xlabel("x label")
    plot.ylabel("y-label")
    plot.title("titre")
    plot.show()
    
    plot.title('fourth combo')
    plot.scatter(iris.data[: , 1], iris.data[: , 2] , marker = 'o' , c = iris.target, s=100, edgecolor='k') 
    plot.xlabel("x label")
    plot.ylabel("y-label")
    plot.title("titre")
    plot.show()
    
    
    plot.title('fifth combo')
    plot.scatter(iris.data[: , 1], iris.data[: , 3] , marker = 'o' , c = iris.target, s=100, edgecolor='k')
    plot.xlabel("x label")
    plot.ylabel("y-label")
    plot.title("titre")
    plot.show()
    
    plot.title('sixth combo')
    plot.scatter(iris.data[: , 2], iris.data[: , 3] , marker = 'o' , c = iris.target, s=100, edgecolor='k')
    plot.xlabel("x label")
    plot.ylabel("y-label")
    plot.title("titre")
    plot.show()
    
    
    
    #The best visualisation is the one that combines the variables 0 and 3 due to the distinguishment between the group 1 and 2 against group 3.             
    #La meilleure visualization reste la visualisation avec les variables 2 et 3 vu q'elle donne une bonne séparation de groupes
    
    
    