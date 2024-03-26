class Photo:
    def __init__(self, id, nb_tag, tag):
        self.id = id
        self.nb_tag = nb_tag
        self.tag = tag

class Slide :
    def __init__(self, id_tab, nb_tag, tag):
        self.id_tab = id_tab
        self.nb_tag = nb_tag
        self.tag = tag

def score_page_album(tag_p1, tag_p2) :
    common_tags = 0
    tag_p1_not_p2 = 0
    tag_p2_not_p1 = 0
    for tag in tag_p1 :
        if tag in tag_p2 :
            common_tags += 1
        else :
            tag_p1_not_p2 += 1
    
    for tag in tag_p1 :
        if tag not in tag_p2 :
            tag_p2_not_p1 += 1

    return min(common_tags, tag_p1_not_p2, tag_p2_not_p1)