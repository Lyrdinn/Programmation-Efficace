#Fonction qui lit le fichier passé en parametre et renvoie un tableau de string. 
def get_tab_parsed(path):
    f = open(path, "r")
    content = f.read()
    content = content.split("\n")
    f.close()
    return content

#Fonction qui écrit dans notre fichier solution.
def post_out(path, tabA, tabB, tabC):
    f = open(path, "w")
    for arg in tabA :
        f.write("###\nA")
        villes = arg.split(" ")
        for ville in villes :
            f.write("\n" + ville)
    for arg in tabB :
        f.write("###\nB")
        villes = arg.split(" ")
        for ville in villes :
            f.write("\n" + ville)
    for arg in tabC :
        f.write("###\nC")
        villes = arg.split(" ")
        for ville in villes :
            f.write("\n" + ville)