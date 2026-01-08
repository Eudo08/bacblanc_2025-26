chaine = "tatati"

def nb_lettres (chaine):
    dico = {}
    for i in range(len(chaine)) :
        lettre = chaine[i]
        if lettre in dico :
            dico[lettre] = dico[lettre] + 1
        else :
            dico[lettre] = 1
    return dico    

print(nb_lettres (chaine))