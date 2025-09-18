open_parenthesis = "("
closing_parenthesis = ")"

def creer_pile ():
    pile = []
    return pile

def empiler (elt, pile):
    pile.append (elt)
    return pile


def depiler (pile):
    pile.pop ()
    return pile

def tete (pile):
    return pile [len((pile) -1)]

pile = list("(3+(7*3-5))")

def pile_vide (pile):
    return pile == []

def pile_non_vide (pile ) :
    return not (pile_vide(pile))
    
def head_of_pile_is_an_open_parentheses (pile):
    return tete (pile) == open_parenthesis

def head_of_pile_is_a_closing_parentheses (pile) :
    return tete(pile == closing_parenthesis)

def check_parentheses_coherence (pile) :
    open_parenthese = 0
    closing_parenthese = 0
    while pile_non_vide :
        if head_of_pile_is_an_open_parentheses (pile):
            open_parenthese += 1
        elif head_of_pile_is_a_closing_parentheses (pile) :
            closing_parenthese += 1
        else :
            pass
        depiler (pile)
    return open_parenthese == closing_parenthese


v= [9, 8, 2, 14]

print (check_parentheses_coherence(pile))