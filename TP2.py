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
    
    
    
        
    #La meilleure visualization reste la visualisation avec les variables 0 et 2 vu q'elle donne une bonne séparation de groupes



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
    
    
    


if __name__ == "__main__":
    # execute only if run as a script
    d()

