

def verifie (tableau) :
    for n in range (len(tableau)-1):
        if len(tableau) ==1:
            return
        if tableau[n] >= tableau [n+1]:
            return False
        else :
            return True
        

print(verifie([0, 5, 8, 8, 9]))