#Renvoie vrai si ll contient un element de st.
def double_list_contains(ll, st) :
    for l in ll :
        for s in l :
            if (s == st) :
                return True

#Renvoie la liste des priorité pour chaque villes
def get_priority_list(nb_bus, a, b, c) :
    prioriry_list = [""] * nb_bus.nb_ville
    for i in range(0, nb_bus.nb_ville) :
        if (a[i][1] > b[i][1] and a[i][1] > c[i][1]) :
            prioriry_list[i] += 'a'
            if (b[i][1] > c[i][1]) :
                prioriry_list[i] += 'b'
                prioriry_list[i] += 'c'
            else :
                prioriry_list[i] += 'c'
                prioriry_list[i] += 'b'
        elif (b[i][1] > a[i][1] and b[i][1] > c[i][1]) :
            prioriry_list[i] += 'b'
            if (a[i][1] > c[i][1]) :
                prioriry_list[i] += 'a'
                prioriry_list[i] += 'c'
            else :
                prioriry_list[i] += 'c'
                prioriry_list[i] += 'a'
        else :
            prioriry_list[i] += 'c'
            if (a[i][1] > b[i][1]) :
                prioriry_list[i] += 'a'
                prioriry_list[i] += 'b'
            else :
                prioriry_list[i] += 'b'
                prioriry_list[i] += 'a'
    return prioriry_list

#Retourne la meilleure ville de départ pour un dictionnaire de villes et un nombre de bus.
def get_best_depart(dic_ville, nb_bus) :
    liste_ville_depart = [[], [], []]
    liste_a = []
    liste_b = []
    liste_c = []
    for nom_ville, credit in dic_ville.items() :
        liste_a.append((nom_ville, credit.credit_a))
        liste_b.append((nom_ville,credit.credit_b))
        liste_c.append((nom_ville,credit.credit_c))

    liste_a.sort(key = lambda tup: tup[1], reverse = True)
    liste_b.sort(key = lambda tup: tup[1], reverse = True)
    liste_c.sort(key = lambda tup: tup[1], reverse = True)
    i, lim = 0, nb_bus.nb_bus_a
    while (i < lim) :
        if (not double_list_contains(liste_ville_depart, liste_a[i][0])) :
            liste_ville_depart[0].append(liste_a[i][0])
        else :
            lim += 1
        i += 1
    i, lim = 0, nb_bus.nb_bus_b
    while (i < lim) :
        if (not double_list_contains(liste_ville_depart, liste_b[i][0])) :
            liste_ville_depart[1].append(liste_b[i][0])
        else :
            lim += 1
        i += 1
    i, lim = 0, nb_bus.nb_bus_c
    while (i < lim) :
        if (not double_list_contains(liste_ville_depart, liste_c[i][0])) :
            liste_ville_depart[2].append(liste_c[i][0])
        else :
            lim += 1
        i += 1        
    return liste_ville_depart

def explorer(marquage, dic_chemin, credit_ptr, ville_courante) :
    marquage[ville_courante] = True

    #Si on notre dictionaire de chemin est vide on renvoie la chaine vide.
    if len(dic_chemin[ville_courante]) < 1 :
        return ""

    #On trie tout par distance.
    l_chemin = dic_chemin[ville_courante]
    l_chemin.sort(key = lambda x: x.dist)

    #Si la distance la plus petite est supérieure à notre crédit alors on ne peux plus avancer et on renvoie.
    dist_min = l_chemin[0].dist
    if credit_ptr[0] - dist_min < 0 :
        credit_ptr[0] = 0
        return ""

    #On parcours la liste de tous les voisins du noeud.
    index = 0
    while (index < len(l_chemin)) :
        chemin = l_chemin[index]
        #Si la ville est marquée fausse on l'explore.
        if (marquage[chemin.arrivee] == False and credit_ptr[0] - chemin.dist >= 0) :
            credit_ptr[0] -= chemin.dist
            return chemin.arrivee + " " + explorer(marquage, dic_chemin, credit_ptr, chemin.arrivee)
        index += 1

    return ""

def parcours_profondeur (marquage, dic_chemin, credit, ville_courante) :
    str = ville_courante + " "
    
    #Si la ville que l'on explore est déjà marquée alors on renvoie "".
    if (marquage[ville_courante] == True ) :
        return ""
    
    credit_ptr = [credit]

    #TODO : pour l'instant explore le 1er chemin, il faut que ça compare des chemins pour voir lequel est le meilleur.
    for chemin in dic_chemin[ville_courante] :
        if credit_ptr[0] <= 0 :
            return ""
        
        if marquage[chemin.arrivee] == False :
            return str + explorer(marquage, dic_chemin, credit_ptr, ville_courante)
    
    #Si on avait déjà visité toute les villes dans une autre ligne de bus on renvoie rien.
    return ""