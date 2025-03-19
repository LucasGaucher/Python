""""
Auteur: GAUCHER L.
creation: 01/10/2024 10:49
"""
def affiche():
    l = (-2, 3, 11)

    for x in l:
        print(x**2)

    for i in range(len(l)):
        print("élément n°", i+1, ":", l[i]**2)

    for i, x in enumerate(l):
        print("élément n°", i+1, ":", x**2)

    m = 'Keith'
    for x, y in zip(l,m):
        print(x, y)
    
def occurences(l: list,e):
    compteur = 0
    for i in l:
        if i == e:
            compteur += 1
    return compteur
def teste_occurences():
    from random import randint
    l = [chr(randint(97, 97+26)) for _ in range(26*4)]
    for i in range(97, 97+26):
        print("Occurrences de", chr(i), "dans la liste:", occurences(l, chr(i)))

def appartient(l: list,e):
    trouve = False, -1
    for i in range(len(l)):
        if l[i] == e:
            trouve = True, i
    return trouve

def teste_appartient():
    l = [3, 1, 8, 4, 5, 9, 2, 6, 7, 10]
    print("Appartient 3 dans la liste:", appartient(l, 3))
    print("Appartient 15 dans la liste:", appartient(l, 15))
    
def minimum(l: list):
    min_val = l[0]
    for x in l:
        if x < min_val:
            min_val = x
    return min_val

def teste_minimum():
    assert(minimum([-2, 3, 11]) == -2)
    print("Minimum de la liste [-2, 3, 11]:", minimum([-2, 3, 11]))
    assert(minimum([10, 5, 1, 8, 2]) == 1)
    print("Minimum de la liste [10, 5, 1, 8, 2]:", minimum([10, 5, 1, 8, 2]))
    
def minimum_index(l: list, e):
    min_val = l[0], 0
    for i in range(len(l)):
        if l[i] < min_val:
            min_val = l[i], i
    return min_val

def teste_minimum_index():
    assert(minimum([-2, 3, 11]) == (-2, 0))
    print("Minimum de la liste [-2, 3, 11]:", minimum([-2, 3, 11]))
    assert(minimum([10, 5, 1, 8, 2]) == (1, 2))
    print("Minimum de la liste [10, 5, 1, 8, 2]:", minimum([10, 5, 1, 8, 2]))
    
def invertion(l: list):
    #return l[::-1]
    #return [l[i] for i in range(len(l)-1, -1, -1)]
    l2 = []
    for i in range(len(l)-1, -1, -1):
        l2.append(l[i])
    return l2
    
#Carre magique
def sumTotal(square: list, n: int):  
    return sum(square[i][j] for i in range(n) for j in range(n))

def checkRow(square: list, n: int, i: int, x):  
    return sum(square[i][j] for j in range(n)) == x

def checkColumn(square: list, n: int, j: int, x):  
    return sum(square[i][j] for i in range(n)) == x

def checkDiagonal(square: list, n: int, d: int, x):
    if d == 0:
        return sum(square[i][i] for i in range(n)) == x
    else: 
        return sum(square[i][n-i-1] for i in range(n)) == x

def magic(square: list):
    print( (sumTotal(square, len(square)) % len(square) == 0 ,
            all(checkRow(square, len(square), i, sumTotal(square, len(square))) for i in range(len(square))) ,
            all(checkColumn(square, len(square), i, sumTotal(square, len(square))) for i in range(len(square))) ,
            all(checkDiagonal(square, len(square), i, sumTotal(square, len(square))) for i in range(0, len(square), len(square)-1))))
    
    return (sumTotal(square, len(square)) % len(square) == 0 and
            all(checkRow(square, len(square), i, sumTotal(square, len(square))) for i in range(len(square))) and
            all(checkColumn(square, len(square), i, sumTotal(square, len(square))) for i in range(len(square))) and
            all(checkDiagonal(square, len(square), i, sumTotal(square, len(square))) for i in range(0, len(square), len(square)-1)))

def magicNormal(square: list):
    if magic(square):
        return all(1 <= square[i][j] <= len(square)**2 for i in range(len(square)) for j in range(len(square)))
    return False


def trie(l: list):
    l2 = []
    for i in l:
        if i == 1:
            l2.append(i)
    for i in l:
        if i == 2:
            l2.append(i)
    for i in l:
        if i == 3:
            l2.append(i)
    return l2
assert trie([3, 2, 1, 2 ,3, 1, 1, 3]) == [1, 1, 1, 2, 2, 3, 3, 3]

def trie2(l: list):
    l2 = []
    count = 0
    for i in range(1, len(l)+1):
        for j in range(len(l)):
            count += 1
            if l[j] == i:
                l2.append(i)
    return l2
print(trie2([3, 2, 1, 2 ,3, 1, 1, 3]))

def trie3(l: list):
    nb =[0, 0, 0]
    for i in l:
        if i == 1:
            nb[0] += 1
        elif i == 2:
            nb[1] += 1
        else:
            nb[2] += 1
    return [1]*nb[0] + [2]*nb[1] + [3]*nb[2]
