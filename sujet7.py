def fusion (tab1, tab2) :
    tab_final = []
    while tab1 != [] and tab2 != [] :
        if min(tab1) > min(tab2) :
            tab_final.append (min(tab2))
            tab2.remove (min(tab2))
        elif min(tab1) == min(tab2) :
            tab_final.append(min(tab2))
            tab_final.append(min(tab1))
            tab2.remove(min(tab2))
            tab1.remove(min(tab1))
        else :
            tab_final.append (min(tab1))
            tab1.remove (min(tab1))
    return tab_final

a = [-2, 4]
b = [-3, 5, 10]
print (fusion(a, b))

def fusion1 (tab1, tab2) :
    return

print( fusion([-2, 4], [-3, 5, 10]))