## chaine -> liste de notes
## M -> taille de la chaine inifni si elle existe ( = Somme des a(i) )
## return -1 si infini 0 sinon
def find_motif(chaine, M) :
    size = len(chaine)

    for i in range (0,size-M) :
        if chaine[i] == chaine[i+M] :
            ## On regarde si on a trouver une chaine infinie
            test = True
            for j in (i,i+M) :
                if chaine[j] != chaine[j+M] :
                    test = False
                    break
            if test :
                return -1
            
    return 0

def guess_seq_len(seq):
    guess = 1
    max_len = len(seq) / 2
    for x in range(2, int(max_len)):
        if seq[0:x] == seq[x:2*x] :
            return x
    return guess