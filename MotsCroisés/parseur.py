from classes import *

def parse(file) :
	fd = open(file, "r")
	lines = fd.readlines()

	liste_de_mot_jolis = []

	for i in range(1, len(lines)) :
		current_line = lines[i].split()
		liste_de_mot_jolis.append(Mot(current_line[0], current_line[1]))

	return liste_de_mot_jolis

def write_to_file(file, mot_croises, liste_mots, mot_places) :
    fd = open(file, "w")
    fd.write(str(len(mot_places)))

    for mot in mot_places :
        index = liste_mots.index(mot)
        coordonnee_x = mot.coordonnees[0]
        coordonnee_y = mot.coordonnees[1]
        fd.write(str(index) + " " + str(coordonnee_x) + " " + str(coordonnee_y) + " " + mot.orientation)