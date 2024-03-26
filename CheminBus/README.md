Groupe.5_TP.2
================

## Les donnees
Nous avons choisi de représenter les données recu en entrer sous forme d'objet :
 - NbBus -> pour chaque ville son nombre de bus (A, B, C)
 - Credits -> pour les credit associe a chaque bus
 - Chemin -> pour les arretes ponderees du graphe

## L'algorithme
Nous avons implementer un algorithme glouton :

 - On initialise les données avec un fichier donner en argument
 - On trouve les meilleurs villes de depart pour les bus
 - On fait un parcours de graphe a partir de ces meilleurs villes de depart
 - - A partir d'une ville on va chercher la prochaine ville la plus proche non visitee que l'on peut atteindre.
 - - On avance de maniere recurcive.
 - - On renvoie la concatenation en String du nom des villes traverser
 - On ecrit la solution dans un fichier