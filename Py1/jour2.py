""""
Auteur: GAUCHER L.
creation: 30/09/2024 15:15
"""
def multiplication(a: int, b: int):
    somme = 0
    for i in range(b):
        somme += a
    return somme

assert multiplication(3, 5) == 3*5

def stars(nb:int):
    for i in range(nb, -1, -1):
        print("*" * i)
        
#stars(5)

def stars2(nb:int):
    for i in range(nb):
        print(' '*(nb-i) + "*" * (i) + "*" * (i-1))

#stars2(5)

#4 Tables de multiplication exotiques
def table1(n: int):
    for i in range(1, n+1):
        nb = str(int('1'*i))
        print(nb + '*' + nb + '=' + str(int(nb)**2))

#table1(9)


def table2(n: int):
    var=''
    for i in range(1, n+1):
        var+=str(i)
        print('9 *', var + str(i+1) + ' = ' +'1'*(i+1))
#table2(9)
def table3(n: int):
    var=''
    for i in range(1, n+1):
        var+=str(i)
        print('8 *', var + str(i) + ' = ' + str(8*int(var)+i))
#table3(9)
def table4(n: int):
    var=''
    for i in range(1, n+1):
        var+=str(n-i+1)
        print('9 *', var +' + ' +  str(8-i) + ' = ' + str(9*int(var)+(8-i)))

#table4(9)

def fido(n: int):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        liste = [1,1]
        for i in range(2,n):
            liste.append(liste[i-1] + liste[i-2])
    return liste[n-1]
            
results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
for i in range(len(results)):
    assert fido(i) == results[i]
    
def Syracuse(n : int, a : int):
    for i in range(n):
        if a%2 == 0:
            a = a/2
        else:
           a = 3*a+1
    return a




def nombre_parfait(n: int):
    liste_parfaits = [] 
    for i in range(2, n):
        liste = [1]
        for u in range(2, i):
            if i % u == 0:
                liste.append(u)
        if sum(liste) == i:  # Check if the sum of divisors equals the number itself
            liste_parfaits.append(i)  # If so, it's a perfect number
    return liste_parfaits

#print(nombre_parfait(10*1000))

from random import randint
def jeu_de_nim(n: int, joueur: int):
    print(f'Il reste {n} allumettes :\n' + n * '|')
    joueurs=['joueur', 'bot']
    joueur-=1
    while n > 0:
        print(joueurs[joueur],': choisissez une allumette (1 à 3)')
        if joueur== 0:
            choix = int(input())
        else:
            choix = randint(1, 3)
            print(choix)
        while choix < 1 or choix > 3:
            print('Choix invalide. Choisissez une allumette (1 à 3)')
            choix = int(input())
        n -= choix
        print('\n\nIl reste ',n,' allumettes :\n' + n * '|')
        choix=0
        joueur = 1 if joueur == 0 else 0
    if n == 0:
        print(f'Le joueur {joueurs[joueur-1]} a gagné!')

# Initialisation du jeu
nb = 0
while nb % 2 == 0 or nb <= 1:
    nb = int(input("Saisissez un nombre impair d'allumettes (supérieur à 1) : "))

j = 0
while j not in [1, 2]:
    j = int(input("Voulez-vous commencer (1) ou que l'ordinateur commence (2) : "))

# Lancer le jeu avec le nombre d'allumettes et le joueur choisi
jeu_de_nim(nb, j)
