import sys
import math
from parcours_graphe import *
from parseur import *

"""
    INITIALISE LES OBJETS POUR NOTRE PROGRAMME
"""

class NbBus :
    def __init__(self, v,a,b,c):
        self.nb_ville = v
        self.nb_bus_a = a
        self.nb_bus_b = b
        self.nb_bus_c = c

class Credits :
    def __init__(self, a, b, c):
        self.credit_a = a
        self.credit_b = b
        self.credit_c = c

class Chemin :
    def __init__(self, d, a, di):
        self.depart = d
        self.arrivee = a
        self.dist = di

nb_bus = NbBus(0, 0, 0, 0)
dic_ville = {}
dic_chemin = {}

#Fonction d'initialisation des objets tels que le conteneur des nombre de bus, le dictionnaire des villes
#ainsi que de leurs crédits, et le dictionaire des chemins entre 2 villes et leurs distance.
def intialise(lines) :
    global nb_bus
    global dic_ville
    global dic_chemin
    
    nb_bus = NbBus(int(lines[0]), int(lines[1]), int(lines[2]), int(lines[3]))

    i = 4
    line = lines[i].split()

    #Ajout des villes et leurs crédits.
    while i < len(lines) and len(line) == 4 :
        #Ville et son crédits
        ville = line[0]
        credit = Credits(int(line[1]), int(line[2]), int(line[3]))

        #On initialise dic_ville et dic_chemin avec pour clé la ville
        dic_ville[ville] = credit
        dic_chemin[ville] = []

        i += 1
        line = lines[i].split()

    #Ajout des chemins de A vers B et leur distance
    while i < len(lines) - 1:
        endroit = Chemin( line[0], line[1], int(line[2]))
        envers = Chemin( line[1], line[0], int(line[2]))

        dic_chemin[line[0]].append(endroit)
        dic_chemin[line[1]].append(envers)

        i += 1
        if (i < len(lines)) :
            line = lines[i].split()
    
    for k in dic_chemin.keys() :
        dic_chemin[k] = sorted(dic_chemin[k], key = lambda chemin: chemin.dist)
        

"""
    MAIN
"""

def main(path):
    out = path[:-3] + ".out"
    tab = get_tab_parsed(path)

    #On initialise nos variables et on recupere les meilleurs villes de départ pour chaque tableau.
    intialise(tab)
    ll = get_best_depart(dic_ville, nb_bus)
    tabA = []
    tabB = []
    tabC = []

    Marquage = {n : False for n in dic_ville.keys()}

    #Pour tout le nombre de bus a que l'on a
    for i in range(nb_bus.nb_bus_a) :
        ville_depart = ll[0][i]
        credit_depart = dic_ville[ville_depart].credit_a
        str = parcours_profondeur(Marquage, dic_chemin, credit_depart, ville_depart)
        if str != "" :
            tabA.append(str)
    
    for i in range(nb_bus.nb_bus_b) :
        ville_depart = ll[1][i]
        credit_depart = dic_ville[ville_depart].credit_b
        str = parcours_profondeur(Marquage, dic_chemin, credit_depart, ville_depart)
        if str != "" :
            tabB.append(str)
    
    for i in range(nb_bus.nb_bus_c) :
        ville_depart = ll[2][i]
        credit_depart = dic_ville[ville_depart].credit_c
        str = parcours_profondeur(Marquage, dic_chemin, credit_depart, ville_depart)
        if str != "" :
            tabC.append(str)

    post_out(out, tabA, tabB, tabC)    

if __name__ == "__main__":
    main(sys.argv[1])