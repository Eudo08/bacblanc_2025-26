# gateaux = {
#     "nom" : "gateau au chocolat",
#     "ingrédients" : "oeufs, farine, chocolat, sucre", 
#     "temps de cuisson" : "18 min"
#     }


# def pres_gateau (dico) :
#     return (f"Je suis le {dico["nom"]} et je suis constitué d'{dico["ingrédients"]}.")

# def cuire (dico) :
#     return (f"Le gateau cuit à 180°C pendant {dico["temps de cuisson"]}.")

# print (pres_gateau (gateaux))
# print (cuire(gateaux))



class Gateau  () :
    def __init__(self, nom, ingréditents, temps_cuisson):
        self.nom = nom
        self.ingrédients = ingréditents
        self.temps_cuisson = temps_cuisson

    def presenter_gateau (self) :
        texte = f"\nJe suis le {self.nom}.\n" \
            + f"je suis constitué d'{self.ingrédients}.\n" \
            + f"Le gateau cuit à 180°C pendant {self.temps_cuisson}.\n"
        print (texte)
   
    def cuire (self) :
        texte = f"\nCuisson spéciale pour le {self.nom} :" \
            + f" - Enfourner à 180°C pendant {self.temps_cuisson} minutes\n"
        
my_cake = Gateau ("marbré", ["beurre", "oeufs", "sucre", "chocolat"], 35)
my_cake.presenter_gateau ()
my_cake.cuire ()

class Gateau_anniversaire (Gateau):
    def __init__ (self, nom, ingrédients, temps_cuisson, nbre_bougies) :
        super ().__init__ (nom, ingrédients, temps_cuisson)
        self.nbre_bougie = nbre_bougies
    
    def presenter_bis (self) :
        self.presenter_gateau ()
        print ("JOYEUX ANNIVERSAIRE !!")

    def cuire (self, alpha) :
        texte = f"\nCuisson spéciale pour le {self.nom} :" \
            + f" - Enfourner à 200°C pendant {self.temps_cuisson} minutes" + f"le paramètre est {alpha}"
        print (texte)
my_birth_cake = Gateau_anniversaire ("tarte à l'orange", \
                                     ["farine", "oeufs", "sucre", "orange"], \
                                        50, 55)
my_birth_cake.presenter_bis()