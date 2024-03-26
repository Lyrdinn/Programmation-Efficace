import sys
from parse import *
from frequence import *
from grammaire import *

def main(path):
    out = path[:-3] + ".out"
    freq_glob, first_coup = parse(path)
    freq = initFreq(freq_glob, first_coup)
    correct = 1
    while (guess_seq_len(freq.jouer) == 1 and isFinish(freq, first_coup) == 0 and correct == 1):
        freq, correct = joueTour(freq, bouton_a_jouer(freq), first_coup)
    if (guess_seq_len(freq.jouer) == 1.0):
        print(end(freq, first_coup))
    else:
        print("inf")

 
if __name__ == "__main__":
    main(sys.argv[1])