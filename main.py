# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:22:39 2018

@author: Moulisse
"""

import perceptron
import adaline

etas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

t = 20  # nb dessais totaux
T = 10 # nb dessais du perceptron


perceptron.Perceptron().run(t, T, etas)
adaline.Adaline().run(t, T, etas)


