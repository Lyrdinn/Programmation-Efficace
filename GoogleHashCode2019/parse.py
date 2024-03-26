#Fonction qui lit le fichier passé en parametre et renvoie un tableau de string. 
def get_tab_parsed(path):
    f = open(path, "r")
    content = f.read()
    content = content.split("\n")
    f.close()
    return content

#Fonction qui écrit dans notre fichier solution.
def post_out(path, result):
    f = open(path, "w")

    nb_photo = len(result)
    f.write(str(nb_photo) + "\n")

    index = 1
    for slide in result :        
        if len(slide.id_tab) == 1 :
            f.write(str(slide.id_tab[0]) + "\n")
        else :
            f.write(str(slide.id_tab[0]) + " " + str(slide.id_tab[1]) + "\n")
        index += 1

    f.close()
