# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:22:39 2018

@author: Moulisse
"""

import perceptron
import adaline
import logistique
import exp

etas = [0.001, 0.01, 0.1, 1, 10]
t = 20  # nb dessais totaux


print ('Base Iris :')
T = 200 # nb dessais de lalgorithme dapprentissage
base = 'iris'

perceptron.Perceptron().run(t, T, etas, base)
adaline.Adaline().run(t, T, etas, base)
logistique.Logistique().run(t, T, etas, base)
exp.Exponentiel().run(t, T, etas, base)



print ('\nBase Ionosphere :')
T = 200
base = 'ionosphere'

perceptron.Perceptron().run(t, T, etas, base)
adaline.Adaline().run(t, T, etas, base)
logistique.Logistique().run(t, T, etas, base)
exp.Exponentiel().run(t, T, etas, base)



print ('\nBase Cancer :')
T = 200
base = 'cancer'

perceptron.Perceptron().run(t, T, etas, base)
adaline.Adaline().run(t, T, etas, base)
logistique.Logistique().run(t, T, etas, base)
exp.Exponentiel().run(t, T, etas, base)



print ('\nBase Spam :')
T = 200
base = 'spam'

perceptron.Perceptron().run(t, T, etas, base)
adaline.Adaline().run(t, T, etas, base)
logistique.Logistique().run(t, T, etas, base)
exp.Exponentiel().run(t, T, etas, base)

del base