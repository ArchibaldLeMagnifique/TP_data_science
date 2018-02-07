
# TP Science des Données

## Intro :

Dans ce TP, nous avons testé et comparé differents algorithmes d'apprentissage supervisé.
Après les avoir fait tourner suffisamment, nous avons pu en déduire leurs scores représentés par un pourcentage de réussite.

Les paramètres choisis sont les suivants:
* t = 100 (nombre de boucles totales)
* T = 200 (nombre de pick aléatoires pour l'apprentissage)
* eta = [0.001, 0.01, 0.1, 1, 10]

## Comparaison des algorithmes :

Algorithme \ Base | Iris | Ionosphere | Cancer du sein | Spam
--- | :---: | :---: | :---: | :---:
Perceptron | 99.91 | 67.22 | **98.74** | 97.72
Adaline | 83 | 64.08 | 77.48 | 77.82
Logistique | 88.59 | **71.17** | 87.61 | 78.74
Exponentiel | **100** | 70.11 | 97.29 | **99.15**

Finalement, deux d'entre eux sont à retenir : le perceptron et l'exponentiel, les deux autres étant légerement en dessous.

## Avancement du TP :

Nous avons réussi à aller jusqu'au bout, ce qui comprend :
* la gestion des fichiers d'entrés
* les quatres algorithmes
* le choix de eta
* la validation croisée

Pour tester nos programmes, un exemple d'utilisation ce trouve dans le main.py.
