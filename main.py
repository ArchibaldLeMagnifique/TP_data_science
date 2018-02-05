# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:22:39 2018

@author: Moulisse
"""

import perceptron
import adaline

etas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
t = 10  # nb dessais totaux


print ('Base Iris avec T=5')
T = 2 # nb dessais de lalgorithme dapprentissage
base = 'iris' # donnes a utiliser

perceptron.Perceptron().run(t, T, etas, base)
adaline.Adaline().run(t, T, etas, base)

#

print ('\nBase Ionosphere avec T=20')
T = 10
base = 'ionosphere'

perceptron.Perceptron().run(t, T, etas, base)
adaline.Adaline().run(t, T, etas, base)

#

print ('\nBase Spam avec T=100')
T = 100
base = 'spam'

perceptron.Perceptron().run(t, T, etas, base)
adaline.Adaline().run(t, T, etas, base)