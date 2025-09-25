class Animal ():
    def __init__(self, type, nom, cri, nourriture_preferee):
        self.type = type
        self.nom = nom
        self.cri = cri
        self.nourriture_preferee = nourriture_preferee

    def crier(self):
        """Comportement dépendant du type d’animal"""
        if self.type == "chien":
            print(f"{self.nom} aboie : {self.cri}")
        elif self.type == "chat":
            print(f"{self.nom} miaule : {self.cri}")
        elif self.type == "oiseau":
            print(f"{self.nom} chante : {self.cri}")
        else:
            print(f"{self.nom} fait un bruit étrange...")  


    def nourrir(self, nourriture):
        """Accès direct à la nourriture préférée"""
        if nourriture == self.nourriture_preferee:
            print(f"{self.nom} mange {nourriture} avec plaisir 😋")
        else:
            print(f"{self.nom} mange {nourriture}, " \
                + f"mais préfère {self.nourriture_preferee}...")
            

    def deplacer(self, lieu):
        print(f"{self.nom} se déplace vers {lieu}.") 

my_dog = Animal ("chien", "Rex", "wouf", "un os" )
my_cat = Animal ("chat", "Minou", "Miaou", "des croquettes")
my_bird = Animal ("oiseau", "Coco", "Cui cui !", "des graines")



if __name__ == "__main__":
    animaux = [
        my_dog,
        my_cat,
        my_bird
    ]

    # Polymorphisme : même fonction, comportement différent
    for animal in animaux:
        animal.crier()
        animal.nourrir("un os")

 
