""""
Auteur: GAUCHER L.
creation: 30/09/2024 09:05
"""

def calcule_total_HT():
    HT = int(input("saisissez un prix unitaire HT : "))
    TVA= float(input(" un taux de TVA:"))
    nb = int(input("un nombre de produit : "))
    TVA= HT*(1+TVA)*nb
    return TVA

def echange_1(nb1,nb2):
    #En utilisant une affectation multiple
    nb1, nb2 = nb2, nb1
    return nb1, nb2
    
def echange_2(nb1,nb2):
    #Sans utiliser d’affectation multiple
    nb3 = nb1
    nb1 = nb2
    nb2 = nb3
    return nb1, nb2
    
def echange_3(nb1:int,nb2:int):
    #En utilisant les opérateurs + et – 
    nb1=nb1+nb2
    nb2=nb1-nb2
    nb1=nb1-nb2
    return nb1, nb2

    
for i in range(10):
    assert echange_1(i, i+1) == echange_2(i, i+1) == echange_3(i, i+1)
    
def echange_3_obj(obj1, obj2, obj3):
    obj1, obj2, obj3  =  obj2, obj3, obj1
    return obj1, obj2, obj3

def  Thomas_O_Beirne(annee: int):
    assert 1900<=annee<=2099, 'annee non comprise entre 1900 et 2099'
    n = annee-1900
    a = n % 19 # a = (annee-1900) % 19
    b = (7 * a + 1) // 19 # b = (7 * ((annee-1900) % 19) + 1) // 19
    c = (11 * a - b + 4) % 29 # c = (11 * ((annee-1900) % 19) - ((7 * ((annee-1900) % 19) + 1) // 19) + 4) % 29
    d = n // 4 # d = (annee-1900) // 4
    e = (n - c + d + 31) % 7 # e = ((annee-1900) - ((11 * ((annee-1900) % 19) - ((7 * ((annee-1900) % 19) + 1) // 19) + 4) % 29) + (annee-1900) // 4 + 31) % 7
    
    jour = 25 - (11 * ((annee-1900) % 19) - ((7 * ((annee-1900) % 19) + 1) // 19) + 4) % 29 - ((annee-1900) - ((11 * ((annee-1900) % 19) - ((7 * ((annee-1900) % 19) + 1) // 19) + 4) % 29) + (annee-1900) // 4 + 31) % 7
    if 25-c-e >0:
        return  str(25-c-e) + " avril"
    else:
        j = str(25-c-e+31)
        return  j+" mars"


def maximum(n1:int, n2:int):
    if n1 < n2:
        return n2
    else:
        return n1

def minimum(n1:int, n2:int):
    if n1 < n2:
        return n1
    else:
        return n2

def reduction(prix: int):
    if 500 >= prix >100:
        return prix - (prix * 0.05)
    elif prix>500:
        return prix - (prix * 0.08)
    
def verif_trie(nb1:int, nb2:int, nb3:int):
    return nb1 <= nb2 <= nb3

def tri_3nb(nb1:int, nb2:int, nb3:int):
    if not verif_trie(nb1, nb2, nb3):
        if nb1 > nb2:
            nb1, nb2 = nb2, nb1
        if nb1 > nb3:
            nb1, nb3 = nb3, nb1
        if nb2 > nb3:
            nb2, nb3 = nb3, nb2
    return nb1, nb2, nb3

def nega_pos(nb1:int, nb2:int):
    """
    return True si nb1 et nb2 muluplie donne un nb posistiif
    """
    return nb1*nb2 < 0
    
def compte(n):
    somme = 0
    for i in range(1, n+1):
        somme += i
    return somme

def compte2():
    demande = int(input("Saisissez un nombre : "))
    somme = demande
    while demande != 0:

        demande = int(input("Saisissez un nombre : "))
        somme+=demande
    return somme

def Somme_des_entiers_pairs_entre_a_et_b(a: int, b: int):
    somme = 0
    for i in range(a+1, b, 2):
        somme += i
    return somme