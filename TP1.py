#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:10:22 2019

@author: 11813288
""Mohamed Bouzid"""

from sklearn import *  #1
from numpy import *
import matplotlib.pyplot as plot
    

iris = datasets.load_iris() #2

def B():
    
    print("données",iris.data)
    print("feature_names",iris.feature_names)
    print("nom des classes",iris.target_names)

    targetNames =iris.target_names
    data = iris.data
    Features= iris.feature_names

    print(targetNames[iris.target]) #3
  
    print("la moyenne de chaque variable",iris.data.mean(0))
    print("l'écart type de chaque variable",iris.data.std(0))
    print("le max de chaque variable",iris.data.max(0))
    print("le min de chaque variable",iris.data.min(0))
    #5
    print("nombre de Classe",targetNames.size)
    print("taille Total des donnees",iris.data.size)
    print("Taille de donnees par Colonne",iris.data.shape[0])
    print("Nombre de variable",iris.data.shape[1])



def D():
    x,y= datasets.make_blobs(n_samples=1000, n_features=2, centers=4)
    plot.scatter(x[: , 0], x[: , 1] , marker = 'o' , c = y, s=100, edgecolor='k')
    plot.xlim(-15,15)
    plot.ylim(-15,15)
    plot.xlabel("x label")
    plot.ylabel("y-label")
    plot.title("titre")
    plot.show()
    


if __name__ == "__main__":
    # execute only if run as a script
    D()


    