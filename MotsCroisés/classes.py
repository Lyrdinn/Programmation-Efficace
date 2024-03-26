class Mot :
	def __init__(self, mot, score) :
		self.mot = mot
		self.len = len(mot)
		self.score = score
	def to_pretty_String(self) :
		return "Mon mot est ["+self.mot+"] avec un score de ["+self.score+"]"

def sort_list_Mot(list_mot) :
	list_mot.sort(reverse = True, key = sort_condition)

def sort_condition(mot) :
	return mot.score		

class Mot_places :
    def __init__(self, mot, coordonnes, orientation) :
        self.mot = mot
        self.coordonnes = coordonnes
        self.orientation = orientation