# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:22:39 2018

@author: Moulisse
"""

import numpy as np
from random import randint

def normalize (set):
    length = len(set[0].strip("\n").split(','))-1
    for k in range(length):
        for i in range(len(data)):
            1

def getDataIris (proportion):
    file = open("./dataset/iris.data", "r")
    
    lines = normalize(file.readlines())

    baseApprentissage = []
    baseTest = []
    
    for k in range(len(lines)):
        strline = lines[k].strip("\n").split(',')
        line = list(map(float, strline[:-1]))
        
        if (k < len(lines) * proportion):
            if (strline[-1] == "Iris-setosa"):
                baseApprentissage.append(line + [1.0])
            else:
                baseApprentissage.append(line + [-1.0])
        else:
            if (strline[-1] == "Iris-setosa"):
                baseTest.append(line + [1.0])
            else:
                baseTest.append(line + [-1.0])
    return (baseApprentissage, baseTest)


def perceptron (X, Y, eta, T):
    t=0
    nbElem = len(X[0])    
    w = np.zeros(nbElem)    
    while (t<T):
        i = randint(0, len(X)-1)  
        
        prodScal = 0
        for j in range(nbElem):
            prodScal = prodScal + w[j]*float(X[i][j])

        if (Y[i] * prodScal <= 0):
            w[0] = w[0] + eta * Y[i]
            for j in range(nbElem-1):
                w[j+1] = w[j] + eta * Y[i] * float(X[i][j])
        t = t+1
    return(w)

def testMethode(baseTest, w) :
    size_of_space = len(baseTest[0]) -1
    perf = 0.0
    for i in range(len(baseTest)) :
        yi = baseTest[i][size_of_space]
        xi = [1] + list(baseTest[i][0:size_of_space])
        if (yi * np.dot(w, xi)) > 0 :
            perf += 1.0
    return perf/float(len(baseTest))


eta = 0.2
T = 100

(baseApprentissage,baseTest) = getDataIris(1/3)

#w = perceptron(X, Y, eta, T)






