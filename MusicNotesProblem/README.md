Groupe.5_TP.5
================

## Les données


## L'algorithme
A partir de la partition donné et de facon recurcive :
- On ajoute a la partition la note jouable qui a été joué le moins de fois
- - Si il n'y a pas de note jouable on renvoie la taille de l'extention de la partition.
- - Si on repere un motif infini on renvoit infini.

Le motif infini est de taille M = (Somme des a(i)). Pour le reperer on regarde si dans la partition il y a une chaine de taille 2M tel que dans cette chaine le caractere a la position i est le meme que celui a la position i+M