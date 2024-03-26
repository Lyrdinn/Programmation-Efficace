
def parse(path) :
    fd = open(path, "r")
    lines = fd.readlines()

    #On initialise le nombre de bouttons et la longueur de la frequence initiale.
    line1_tab = lines[0].rstrip().split()
    nb_buttons = line1_tab[0]
    long_freq_init = line1_tab[1]

    #On initialise le tableau d'entiers qui definissent les frequences.
    line2_tab = lines[1].rstrip().split()
    tab_freq_init = [int(x) for x in line2_tab]

    first_coup = []
    for i in range(2, len(lines)) :
        current_line = lines[i].rstrip()
        current_line_tab = current_line.split()
        
        for i in range (len(current_line_tab)) :
            first_coup.append(int(current_line_tab[i]))

    return tab_freq_init, first_coup
