
def calcul_score_tab(mot_croises, mot_places) :
    T = 0
    P = 0
    
    for i in range(0, mot_places) :
        partage = mot_places[i][1]
        P += mot_places[i].score * partage
    
    for i in range(0, len(mot_croises)) :
        for j in range(0, len(mot_croises[i])) :
            if (mot_croises[i][j] == "") :
                T += 1

    if (P - T <= 0) :
        return 0
    
    return P - T