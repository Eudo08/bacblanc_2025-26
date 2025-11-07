# On commence par dérire un arbre à l'aide de dictionnaires python.
# Pour cela on utilise la fonction node définie comme ci-après:
def make_node (root, left=None, right=None):
    return {"root": root, "left": left, "right" : right}

a = make_node (0)
b = make_node (4)
c = make_node (3, a, b)
d = make_node (6)
e = make_node (9)
f = make_node (10, e, None)
g = make_node (7, d, f)
h = make_node (5, c, g)
i = make_node (17)
j = make_node (21)
k = make_node (19, i, j)
A = make_node (15, h, k)
# Définir un arbre à l'aide de dictionnaires imbriqués

# Ecrire une fonction récursive qui calcule la hauteur d'un arbre binaire

# def height (tree) :
#     if tree == {} or tree == None:
#         return "C'EST VIDEEEEEEEEE"
#     else :
#         return 1 + max (height(tree ["left"]), \
#                                height (tree ["right"]))

# print (height (A))


# Ecrire une fonction récursive qui décrit le parcours PREFIXE d'un arbre binaire

def prefixe (tree) :
    if tree == {} or tree == None :
        return []
    else :
        return [tree["root"]] \
            + prefixe (tree["left"]) \
            + prefixe (tree["right"])

print (prefixe(A))







# Ecrire une fonction récursive qui décrit le parcours INFIXE d'un arbre binaire
def infixe (tree) :
    if tree == {} or tree == None :
        return []
    else :
        return infixe(tree["left"]) \
            + [tree["root"]] \
            + infixe (tree["right"])

print (infixe(A))

# Ecrire une fonction récursive qui décrit le parcours SUFFIXE d'un arbre binaire
def suffixe (tree) :
    if tree == {} or tree == None :
        return []
    else :
        return suffixe(tree["left"]) \
            + suffixe (tree["right"]) \
            + [tree["root"]]
 
            
print (suffixe(A))

# Ecrire une fonction récursive qui décrit le parcours EN LARGEUR d'un arbre binaire

# Ecrire une fonction récursive qui dit si une valeur est dans un arbre binaire
# def value_in_binary_tree (value, tree) :
#     if tree == None :
#         return False
#     else :
#         return tree ["root"] == value \
#             or value_in_binary_tree (value, tree ["left"]) \
#             or value_in_binary_tree (value,tree["right"])

# print (value_in_binary_tree(2, A))        
# Ecrire une fonction récursive qui dit si un arbre binaire est un de recherche

def binary_search (tree, check_roots) :
    if tree == None :
        return True
    elif tree ["left"] == None and tree ["right"] == None  :
        return True
    else :
        if tree ["left"] == None and tree ["right"] != None :
            check_roots = tree ["root"] <= tree ["right"]["root"]
        elif tree ["left"] != None and tree ["right"] == None :
            check_roots = tree ["left"]["root"] <= tree ["root"]
        else :
            check_roots = \
                    tree ["left"]["root"] \
                    <= tree ["root"] \
                    <= tree ["right"]["root"]
        return check_roots \
            and binary_search (tree ["left"], check_roots) \
            and binary_search (tree ["left"], check_roots)


print (binary_search(A, True))