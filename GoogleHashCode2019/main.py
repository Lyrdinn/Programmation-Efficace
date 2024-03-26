import sys
import re
from parse import *
from photo import *
from algo import *

def main(ficher_test, ficher_sol) :
    out = ficher_sol + ".out"
    lines = get_tab_parsed(ficher_test)

    #On a un tableau de photo verticales, un tableau de slides horizontales.
    photo_v = []
    slide_h_list = []

    id = 0

    for i in range(1, len(lines)) :
        line = lines[i].rstrip()
        line_tab = line.split(" ")

        #On créé la liste de tags.
        list_tag = []
        for  j in range(2, len(line_tab)) :
            list_tag.append(line_tab[j])

        #On ajoute au tableau horizontal ou vertical.
        if (line_tab[0] == "H") :
            slide_h_list.append(Slide([id], int(line_tab[1]), list_tag))
        else :
            photo_v.append(Photo(id, int(line_tab[1]), list_tag))

        id += 1

    diapo = []

    # diapo = creation_diapositive_meilleur_algo(photo_v, slide_h_list, diapo)
    # post_out(out, diapo)
    test = get_best_couplage_vert(photo_v)
    # sort_ll_vert(test)
    print_tag(test)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])