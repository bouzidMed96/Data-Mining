#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:23:26 2019

@author: BouzidMed
"""

import numpy as np
import matplotlib.pyplot as plot
import sklearn.preprocessing as sk
from sklearn.preprocessing import MinMaxScaler
from sklearn import *  
from sklearn.decomposition import PCA 
from sklearn.lda import LDA 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis




def A():
    X= np.matrix('1 -1 2; 2 0 0; 0 1 -1')
    moyenne = X.mean()
    variance = X.var()
    
    print("moyenne de la matrice ",moyenne)
    print("variance de la matrice ",variance)
    
    Xnorm = sk.scale(X)
    moyenneNorm = Xnorm.mean()
    varianceNorm = Xnorm.var()
    print("la moyenne de la matrice nromalise est ",moyenneNorm)
    print("la variance de la matrice nromalisee est ",varianceNorm)


def B():
    X2= np.matrix('1 -1 2; 2 0 0; 0 1 -1')
    moyenneX2 = X2.mean(axis =0 )
    print("moyenne de la matrice X2 ",moyenneX2)
    X2norm = MinMaxScaler().fit(X2[[0, 1]]).transform(X2[[0,1]])
    print("normalisation de X2 dans l'intervalle [0,1] ",X2norm)
    moyenneX2 = X2norm.mean(axis =0 )
    print("la moyenne des donnees normalises nromalisee est ",moyenneX2)