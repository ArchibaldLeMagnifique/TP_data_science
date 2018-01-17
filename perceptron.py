# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:22:39 2018

@author: Moulisse
"""

import numpy as np
from random import randint

def readData (path, nbApprentissage, prediction):
    file = open("./dataset/"+path, "r")
    
    X=[]
    Y=[]
    
    for k in range(nbApprentissage):
        line = file.readline().split(',')
        X.append(line[:-1])
        if (line[-1].rstrip() == prediction):
            Y.append(1)
        else:
            Y.append(-1)
    return (X,Y)

def perceptron (X, Y, eta, T):
    t=0
    nbElem = len(X[0])
    
    #initialisation du vecteur poid
    w = np.zeros(nbElem)
    
    while (t<T):
        i = randint(0, len(X))  
        
        prodScal = 0
        for j in range(nbElem):
            print(j,w[j]*X[i][j])
            prodScal = prodScal + w[j]*X[i][j]

        if (Y[i] * prodScal <= 0):
            w[0] = w[0] + eta * Y[i]
            for j in range(nbElem-1):
                w[j+1] = w[j+1] + eta * Y[i] * X[i][j]
        t = t+1


eta = 0.2
T = 100

(X,Y) = readData('iris.txt', 100, 'Iris-setosa')

perceptron(X, Y, eta, T)