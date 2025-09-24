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
        texte = f"\Je suis le {self.nom} et je suis constitué d'{self.ingrédients}." + f"Le gateau cuit à 180°C pendant {self.temps_cuisson}."
        print (texte)
   
    def cuire (self) :
        texte = f"\nCuisson spéciale pour le {self.nom} :" \
            + f" - Enfourner à 180°C pendant {self.temps_cuisson} minutes"
        
my_cake = Gateau ("marbré", ["beurre", "oeufs", "sucre", "chocolat"], 35)
my_cake.presenter ()
my_cake.cuire ()