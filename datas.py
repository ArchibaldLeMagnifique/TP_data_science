# -*- coding: utf-8 -*-

from random import shuffle

def parseAndNormalize (set):
    length = len(set)
    nbParam = len(set[0].strip("\n").split(','))-1
    
#    res = [[] for _ in range(len(set))]
    
    res = []
    
    for i in range(length):
        res.append(set[i].strip("\n").split(','))
    
    vmin = res[0][:-1]
    vmax = res[0][:-1]
    
    for k in range(nbParam):
        for i in range(length):
               vmin[k] = min(vmin[k], res[i][k])
               vmax[k] = max(vmax[k], res[i][k])
               
    for k in range(nbParam):
        for i in range(length):
            res[i][k] = res[i][k]

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
    shuffle(base)
    return (base)

def getDataIonosphere ():
    file = open("./dataset/ionosphere.data", "r")
    lines = parseAndNormalize(file.readlines())
    base = []
    
    for k in range(len(lines)):
        strline = lines[k]
        line = list(map(float, strline[:-1]))
        if (strline[-1] == "g"):
            base.append(line + [1.0])
        else:
            base.append(line + [-1.0])
    shuffle(base)
    return (base)

def getDataSpambase ():
    file = open("./dataset/spambase.data", "r")
    lines = parseAndNormalize(file.readlines())
    base = []
    
    for k in range(len(lines)):
        strline = lines[k]
        line = list(map(float, strline[:-1]))
        if (strline[-1] == "1"):
            base.append(line + [1.0])
        else:
            base.append(line + [-1.0])
    shuffle(base)
    return (base)

# k ieme partition de la base decoupe en K, et le reste
def splitBase(base, k, K):
    base1 = []
    base2 = []
    for i in range(len(base)):
        if (i>(k-1)/K*len(base) and i<k/K*len(base)):
            base1.append(base[i])
        else:
            base2.append(base[i])
    return (base1, base2)