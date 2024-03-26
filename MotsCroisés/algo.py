def create_grille(len) :
    return [len * len][len * len]

def algo(liste_mot) :
    grille = create_grille(liste_mot[0].len)
    put_h(grille, liste_mot[0], (0,0))
    liste_mot.pop()

    

def put_h(grille, mot, coordoonnes) :
    x = coordoonnes[0]
    y = coordoonnes[1]
    len_t = 0
    if (y + mot.len >= len(grille[x])) :
        len_t = (y + mot.len - len(grille[x])) + 1
    if (len_t > 0) :
        for i in range(len(grille)) :
            for j in range(0, len_t) :
                grille[i].append("")
    for i in range(mot.len) : 
        grille[x][y] = mot.mot[i]
        y += 1
    return grille

def put_v(grille, mot, coordoonnes) :
    x = coordoonnes[0]
    y = coordoonnes[1]
    len_t = 0
    if (x + mot.len >= len(grille)) :
        len_t = (x + mot.len - len(grille[x])) + 1
    if (len_t > 0) :
        for i in range(len_t) :
            grille.append([""]*len(grille[0]))
    for i in range(mot.len) :
        grille[x][y] = mot.mot[i]
        x += 1
    return grille

def can_add_word(word, coordonnees, orientation, grille) :
    if (coordonnees[0] >= len(grille)) :
        return False
    elif (coordonnees[1] >= len(grille[0])) :
        return False
    else :
        if (orientation == "H") :
            for i in range(0, len(grille)) :
                if grille[i][coordonnees[1]] != "" :
                    return False
        else :
            for j in range(0, len(grille[coordonnees[0]])) :
                if grille[coordonnees[0]][j] != "" :
                    return False
        return True