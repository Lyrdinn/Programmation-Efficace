import sys
from parseur import *
from classes import *
from algo import *

def main(path):
    out = path[:-3] + ".out"
    liste_de_mot_jolis = parse(path)
    sort_list_Mot(liste_de_mot_jolis)
    for i in range(len(liste_de_mot_jolis)) :
        print(liste_de_mot_jolis[i].to_pretty_String())

    # appel de notre algo

    # écriture dans la sortie

 
if __name__ == "__main__":
    main(sys.argv[1])