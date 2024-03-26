from photo import *

""" 
Complexite en temps : O( (n**3)*(m**2) ) avec :
 n = nombre de photo
 m = nombre de tag
"""

def creation_diapositive_meilleur_algo(photo_v, slides_h_list, diapo) :
    #On trie par nombre de tags les photos verticales.
    photo_v = sorted(photo_v, key = lambda x: x.nb_tag)
    slides_v_list = []

    #On regroupe les photos verticales dans les slides avec les plus grandes et les plus petites 
    #ce qui fait qu'on a un nombre de tags homogene.
    for i in range(0, len(photo_v)//2) :
        U_tag = list(set(photo_v[i].tag + photo_v[len(photo_v) - i - 1].tag))
        slides_v_list.append(Slide([photo_v[i].id, photo_v[len(photo_v) - i - 1].id], len(U_tag), U_tag))
    #On retrie pour que ce soit parfait.
    slides_v_list = sorted(slides_v_list, key = lambda x : x.nb_tag)
    
    #On trie par nombre de tags les photos horizontales.
    slides_h_list = sorted(slides_h_list, key = lambda x : x.nb_tag)

    diapo = []

    #On renvoie les slides horizontales ou verticales si on en a qu'un seul type.
    if len(slides_h_list) == 0 :
        return slides_v_list
    elif len(slides_v_list) == 0 :
        return slides_h_list
    
    #Sinon on peut appliquer l'algo, dans notre cas nous choisissons la première slide horizontale.
    diapo.append(slides_h_list.pop())
    
    while(len(slides_h_list) > 0 and len(slides_v_list) > 0) :
        tag_diapo_last_slide = diapo[len(diapo) - 1].tag
        tag_slides_h = slides_h_list[0].tag
        tag_slides_v = slides_v_list[0].tag

        score_v = score_page_album(tag_diapo_last_slide, tag_slides_v)
        score_h = score_page_album(tag_diapo_last_slide, tag_slides_h)
        
        #On regarde qui a le plus grand score entre les slides verticales et horizontales et on pop pour
        #ajouter à notre diapo.
        if (score_v > score_h) :
            diapo.append(slides_v_list.pop())
        elif (score_h > score_h) :
            diapo.append(slides_h_list.pop())
        else :
            diapo.append(slides_h_list.pop())

    #On ajoute les dernières photos à notre slides.
    while(len(slides_h_list) > 0) :
        diapo.append(slides_h_list.pop())
    while(len(slides_v_list) > 0) :
        diapo.append(slides_v_list.pop())

    return diapo



k = 2
def get_best_couplage_vert(photo_v_list) :
    biggest_tag = get_biggest_tag(photo_v_list)
    ll = [[]] * ((biggest_tag // k) + 1)

    for i in range(0, len(photo_v_list)) :
        print(i)
        phot = photo_v_list[i]
        nTag = phot.nb_tag
        print("tag :" + str(nTag))
        index = (nTag - 1) // k
        print("index in ll =" + str(index))
        ll[index].append(photo_v_list[i])
    return ll

def get_biggest_tag(photo_v_list) :
    maxTag = 0
    for i in range(0, len(photo_v_list)) :
        if (photo_v_list[i].nb_tag > maxTag) :
            maxTag = photo_v_list[i].nb_tag
    return maxTag

def sort_ll_vert(ll) :
    for i in range(0, len(ll)) :
        ll[i].sort(key=lambda x: x.nb_tag)

def print_tag(ll) :
    print("Len ll = "+str(len(ll)))
    for i in range(0, len(ll)) :
        print("Len ll["+str(i)+"] = "+str(len(ll[i])))
        print("========")
        for j in range(0, len(ll[i])) :
            print(ll[i][j].nb_tag)
        print("--------")