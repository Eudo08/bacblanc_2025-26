def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat :
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == election[vainqueur]]
    return liste_finale

Urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'C']

print (depouille(Urne))
print (vainqueur(depouille(Urne)))