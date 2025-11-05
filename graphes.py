matrice = [[0,1,1,0,0,0],
		   [1,0,1,1,0,0],
		   [1,1,0,1,0,0],
		   [0,1,1,0,0,0],
		   [0,0,0,0,0,1],
		   [0,0,0,0,1,0]]

def matrice_vers_dico (matrice):
	dico = {}
	i = 0
	for liste in matrice :
		listee = []
		for e in range(len(liste)) :

			if liste[e] == 1 :
				listee.append(e)
		dico[i] = listee
		i += 1

	return dico



print (matrice_vers_dico(matrice))