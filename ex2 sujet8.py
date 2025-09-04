dico = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}

def max_dico (dico) :
    nmax = 0
    if dico == {} :
        pass
    else :
        for pseudo in dico :
            if dico[pseudo] > nmax :
                nmax = dico[pseudo]
                famous_pseudo = pseudo
                famous_speudo_likes = nmax
        return (famous_pseudo, famous_speudo_likes)
    

print (max_dico(dico))