# -*- coding: utf-8 -*-

import datas as datas
import numpy as np
from random import randint

class Adaline:
    
    def __init__(self):
        self.etas = []
        self.T = 0
    
    def __adaline (self, base, eta):
        t=0
        nbElem = len(base[0]) - 1
        w0 = 0.0
        w = np.zeros(nbElem)
        while (t<self.T):
            i = randint(0, len(base)-1)
            prodScal = np.dot(w, base[i][:-1])
            
            w0 = w0 + eta * (base[i][-1] - prodScal - w0)
            for j in range(nbElem):
                w[j] = w[j] + eta * (base[i][-1] - prodScal - w0) * base[i][j]
            t = t+1

        return (w0, w)
    
    def __testPoids(self, base, w0, w):
        perf = 0
        for i in range(len(base)):
            y = base[i][-1]
            x = base[i][:-1]
                    
            if (y * np.dot(w, x) + w0) > 0 :
                perf = perf + 1
        return perf/float(len(base))


    # on divise base A et on fait une cross validation
    def __erreurMoyenne(self, eta, baseA):
        erreur = 0
        for k in range(1):
            (baseEntrainement, baseValidation) = datas.splitBase(baseA, k+1, 5)
            (w0 ,w) = self.__adaline(baseEntrainement, eta)
            erreur = erreur + self.__testPoids(baseValidation, w0, w)
        return (erreur/1)
    

    def __choixEta(self, baseA):
        erreur = 0
        meilleurEta = 0
        for e in self.etas:
            erreurCur = self.__erreurMoyenne(e, baseA)
            if (erreurCur >= erreur):
                erreur = erreurCur
                meilleurEta = e
        return meilleurEta
    
    def run(self, t, T, etas, donnes):
        self.etas = etas
        self.t = t
        self.T = T

        erreur = 0

        for i in range(t):
            if (donnes == 'ionosphere'):    
                base = datas.getDataIonosphere()
            elif (donnes == 'iris'):
                base = datas.getDataIris()
            elif (donnes == 'spam'):
                base = datas.getDataSpambase()
            elif (donnes == 'cancer'):
                base = datas.getDataCancer()
            else:
                break
            (baseT, baseA) = datas.splitBase(base, 1, 4)
            
            e = self.__choixEta(baseA)
            
            (w0 ,w) = self.__adaline(baseA, e)
            erreur = erreur + self.__testPoids(baseT, w0, w)
            
        erreur = erreur / t
            
        print (erreur)
        
        
        
        