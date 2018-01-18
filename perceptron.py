# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:22:39 2018

@author: Moulisse
"""

import numpy as np
from random import randint

def parseAndNormalize (set):
    length = len(set[0].strip("\n").split(','))-1
    
    res = [[] for _ in range(len(set))]
    
    for k in range(length):
        vmax = float(set[0].strip("\n").split(',')[k])
        vmin = vmax
        for i in range(len(set)):
            vmax = max(vmax, float(set[i].strip("\n").split(',')[k]))
            vmin = min(vmin, float(set[i].strip("\n").split(',')[k]))
        for i in range(len(set)):
            res[i].append((float(set[i].strip("\n").split(',')[k]) - vmin)/(vmax - vmin))
    for i in range(len(set)):
        res[i].append(set[i].strip("\n").split(',')[-1])
    return res

def getDataIris ():
    file = open("./dataset/iris.data", "r")
    lines = parseAndNormalize(file.readlines())
    base = []
    
    for k in range(len(lines)):
        strline = lines[k]
        line = list(map(float, strline[:-1]))
        if (strline[-1] == "Iris-setosa"):
            base.append(line + [1.0])
        else:
            base.append(line + [-1.0])
    return base

# k ieme partition de la base decoupe en K, et le reste
def splitBase(base, k, K):
    base1 = []
    base2 = []
    for i in range(len(base)):
        if (i>((k-1)/K*len(base)) and i<(k/K*len(base))):
            base1.append(base[i])
        else:
            base1.append(base[i])
    return (base, base2)

def perceptron (base, eta, T):
    t=0
    
    nbElem = len(base[0]) - 1
    w0 = 0.0
    w = np.zeros(nbElem)
    while (t<T):
        i = randint(0, len(base)-1)
        prodScal = w0 + np.dot(w, base[i][:-1])

        if (base[i][-1] * prodScal <= 0):
            w0 = w0 + eta * base[i][-1]
            for j in range(nbElem):
                w[j] = w[j] + eta * base[i][-1] * base[i][j]
        t = t+1
    return (w0, w)


def testPoids(base, w0, w):
    perf = 0
    for i in range(len(base)):
        y = base[i][-1]
        x = base[i][:-1]
                
        if (y * np.dot(w, x) + w0) > 0 :
            perf = perf + 1
    return perf/float(len(base))


# on divise base A et on fait une cross validation
def erreurMoyenne(eta, T, baseA):
    erreur = 0
    for k in range(K):        
        (baseEntrainement, baseValidation) = splitEV(base, k, K)
        (w0 ,w) = perceptron(baseA, eta, T)
        erreur = erreur + testPoids(baseA, w0, w)
    return (erreur/K)
    

# 
def choixEta(etas, T, baseA):
    1

etas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
T = 10
K = 5
base = getDataIris()

