""""
Auteur: GAUCHER L.
creation: 04/11/2024 09:00
"""

def exponentiation_iterative(n: int,x:int):
    result = 1
    for _ in range(x):
        result = result*n
    return result


def exponentiation_recursive(n: int,x:int):
    if x == 0:
        return 1
    else:
        return n * exponentiation_recursive(n, x-1)

if __name__ == "__main__":
    import random
    for i in range(100):
        n = random.randint(1, 100)
        x = random.randint(1, 100)
        assert exponentiation_iterative(n,x) == exponentiation_recursive(n,x) == n**x
        
def fibonacci_recursive(n: int):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
def syracuse_recursive(a: int, n: int):
    if n <= 0:
        return a
    elif a % 2 == 0:
        return syracuse_recursive(a//2, n-1)
    else:
        return syracuse_recursive(3*a+1, n-1)
    
def somme_carre(n):
    if n <= 0:
        return 0
    else:
        return n**2 + somme_carre(n-1)

def chercher(liste:list, element):
    n = len(liste)
    if n == 0:
        return False
    elif n == 1:
        return liste[0]==element
    else:
        return liste[n-1]==element or chercher(liste[:n-1], element)
    
def recherche_dichotomique(liste: list, element):
    if len(liste) == 1:
        return liste[0]==element
    else:
        milieu = len(liste) // 2
        if liste[milieu] == element:
            return True
        elif liste[milieu] < element:
            return chercher(liste[milieu+1:], element)
        else:
            return chercher(liste[:milieu], element)


def exponentiation_rapide(n: int,x:int):
    if x == 0:
        return 1
    elif x == 1:
        return n
    elif x % 2 == 0:
        return exponentiation_rapide(n**2, x//2)
    else:
        return n * exponentiation_rapide(n, x-1)

    
if __name__ == "__main__":
    import random
    for i in range(100):
        n = random.randint(1, 100)
        x = random.randint(1, 100)
        assert exponentiation_rapide(n,x) == n**x
        
def faire_hanoi(n, source, target, auxiliary):
    """Déplace les disques de la tour source à la tour cible en utilisant une tour auxiliaire."""
    if n == 1:
        print('Déplacer le disque 1 de la tour',source, 'vers la tour',target)
    else:
        # Déplacer les n-1 disques de la source vers la tour auxiliaire
        faire_hanoi(n - 1, source, auxiliary, target)
        
        # Déplacer le disque n de la source vers la cible
        print('Déplacer le disque',n, 'de la tour',source, 'vers la tour',target)
        
        # Déplacer les n-1 disques de la tour auxiliaire vers la cible
        faire_hanoi(n - 1, auxiliary, target, source)

if __name__ == "__main__":
    # Exécution de l'algorithme pour n disques
    n = 3  # Nombre de disques
    faire_hanoi(n, 'A', 'C', 'B')
    
def tri_a_bulles(liste : list):
    """
    Tri par bulles d'une liste en ordre croissant.
    """
    n = len(liste)
    pas_trie = True
    k =  0
    while pas_trie:
        pas_trie = False
        for j in range(0, n-k-1):
            if liste[j] > liste[j+1] :
                pas_trie = True
                liste[j], liste[j+1] = liste[j+1], liste[j]
        k += 1
    return liste

if __name__ == "__main__":
    from random import randint
    liste = [randint(0, 300) for i in range(50)]
    print(liste)
    tri_a_bulles(liste)
    print(liste)
