#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:43:54 2019

@author: 11813288
"""
import numpy as np
import matplotlib.pyplot as plot
import sklearn.preprocessing as sk
from sklearn.preprocessing import MinMaxScaler
from sklearn import *  
from sklearn.decomposition import PCA 
from sklearn.lda import LDA 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def d():
    iris = datasets.load_iris()
    pca = PCA(n_components=4)
    pcaIris = pca.fit(iris.data).transform(iris.data)
    lda = LinearDiscriminantAnalysis(n_components=4)
    ldaIris = lda.fit(iris.data, iris.target).transform(iris.data)
    plot.figure()
    colors = ['black', 'orange', 'green']
    lw = 2
    
    for color, i in zip(colors, [0, 1, 2]):
        plot.scatter(pcaIris[:, 0], pcaIris[:, 1], color=color, alpha=.8, lw=lw)
        
    
    plot.figure()
    for color, i in zip(colors, [0, 1, 2]):
        plot.scatter(ldaIris[:, 0], ldaIris[:, 1], alpha=.8, color=color)
    
    
    plot.show()