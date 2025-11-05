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



# print (matrice_vers_dico(matrice))

def dico_to_matrice (dico):
	matrix = []
	for key in dico.keys ():
		matrix.append(len(dico.keys())*[0])
		for elmt in dico[key]:
			matrix [key][elmt]=1
	return matrix

print (dico_to_matrice(matrice_vers_dico(matrice)))
