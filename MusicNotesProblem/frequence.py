import math


class Freq:
    def __init__(self, globale, temp, jouable, jouer, compter, frequency):
        self.globale = globale
        self.temp = temp
        self.jouable = jouable
        self.jouer = jouer
        self.compter = compter
        self.frequency = frequency

def tour(tab):
    for i in range (0, len(tab)):
        tab[i] = tab[i] - 1
    return tab

def jouables(jouable, temp, globale):
    for i in range (0, len(globale)):
        if (temp[i] == 0):
            jouable[i] = jouable[i] + 1
            temp[i] = globale[i]
    return jouable, temp

def correct(freq):
    for i in range(0, len(freq.compter)):
        inf = (len(freq.jouer) + 1) * freq.frequency[i] - 1
        if (freq.compter[i] - inf <= 0):
            return -1
    return 0

def isFinish(freq, first_coup):
    for i in range(0, len(freq.compter)):
        inf = len(freq.jouer) * freq.frequency[i] - 1
        if (freq.compter[i] - inf <= 0):
            return -1
    for i in range(0, len(freq.jouable)):
        if (freq.jouable[i] < 0):
            return (len(freq.jouer) - len(first_coup))
    return 0

def end(freq, first_coup):
    return (len(freq.jouer) - len(first_coup))

def joueTour(freq, index, firstCoup):
    if (index == -1):
        return freq, 0
    freq.compter[index] += 1
    if (correct(freq) != 0):
        return freq, 0
    freq.jouable[index] -= 1
    freq.temp = tour(freq.temp)
    freq.jouable, freq.temp = jouables(freq.jouable, freq.temp, freq.globale)
    if isFinish(freq, firstCoup) == 0 :
        freq.jouer.append(index + 1)
        return freq, 1
    else:
        return freq, 0

def sommeAi(freq):
    moy = 0
    for i in range(0, len(freq.globale)):
        moy = moy + freq.globale[i]
    return moy

def initFreq(freq_glob, first_coup):
    globale = list()
    jouable = [1] * len(freq_glob)
    compter = [0] * len(freq_glob)
    jouer = list()
    frequency = list()
    moy = 0
    for i in range(0, len(freq_glob)):
        moy = moy + freq_glob[i]
    for i in range(0,len(freq_glob)):
        rank = freq_glob[i] / moy
        frequency.append(rank)
        j = 1
        while (rank * j < 1):
            j += 1
        globale.append(j)
    temp = globale.copy()
    for i in range(0, len(first_coup)):
        compter[first_coup[i] - 1] += 1
        jouer.append(first_coup[i])
        jouable[first_coup[i] - 1] = jouable[first_coup[i] - 1] - 1
        temp = tour(temp)
        jouable, temp = jouables(jouable, temp, globale)
    return Freq(globale, temp, jouable, jouer, compter, frequency)

def bouton_a_jouer(freq) :
    #On prend la liste de boutons que l'on peut jouer.
    peut_jouer = [i for i in range(len(freq.jouable)) if freq.jouable[i] > 0]
    #On cherche la meilleure frequence parmis ceux que l'on peut jouer.
    meilleure_freq = 0
    for i in range(len(peut_jouer)) :
        if (freq.globale[peut_jouer[i]] > meilleure_freq) :
            meilleure_freq = freq.globale[peut_jouer[i]]
    
    jouable = list()
    for i in range(len(peut_jouer)) :
        if (freq.globale[peut_jouer[i]] == meilleure_freq):
            jouable.append(peut_jouer[i])
    meilleur_bouton = -1
    if (len(jouable) > 0) : 
        borne_inf = len(freq.jouer) * freq.frequency[jouable[0]] - 1
        inf = math.inf
        for i in range(len(jouable)) :
            if (borne_inf >= freq.compter[jouable[i]]):
                return -1
            if (freq.compter[jouable[i]] - borne_inf < inf) :
                inf = freq.compter[jouable[i]] - borne_inf
                if (inf < 0):
                    return -1
                meilleur_bouton = jouable[i]
        return meilleur_bouton
    else : 
        return -1