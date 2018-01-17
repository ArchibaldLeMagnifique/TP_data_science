# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:22:39 2018

@author: Moulisse
"""

import numpy as np;

def perceptron (X, Y, eta, T):
    t=0
    
    #initialisation du vecteur poid
    w = np.zeros(X.size)
    
    while (t<T):
        
        t = t+1
