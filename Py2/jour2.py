""""
Auteur: GAUCHER L.
creation: 04/11/2024 10:25
"""
def Tri_par_selection(liste:list):
    """
    Cette fonction prend une liste en entrée et renvoie une nouvelle liste triée selon le principe du tri par sélection.
    """
    n = len(liste)
    for i in range(n):
        indice = i
        for j in range(i+1, n):
            if liste[j] < liste[indice]:
                indice = j
        liste[i], liste[indice] = liste[indice], liste[i]
    return liste

def Tri_par_insertion(liste:list):
    """
    Cette fonction prend une liste en entrée et renvoie une nouvelle liste triée selon le principe du tri par insertion.
    """
    for i in range(1, len(liste)):
        temp = liste[i]
        j = i - 1
        while j >= 0 and temp < liste[j] :
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = temp
    return liste

def fusion(gauche,droite):
    result = []
    gauche_index = 0
    droite_index = 0
    while gauche_index < len(gauche) and droite_index < len(droite):
        if gauche[gauche_index] >= droite[droite_index]:
            result.append(droite[droite_index])
            droite_index+=1
        else:
            result.append(gauche[gauche_index])
            gauche_index+=1
    
    while gauche_index < len(gauche):
        result.append(gauche[gauche_index])
        gauche_index+=1
    while droite_index < len(droite):
        result.append(droite[droite_index])
        droite_index+=1
    return result

def tri_fusion_recursive(liste:list, gauche_index:int, droite_index:int):
    if len(liste) == 0: 
        return None
    elif len(liste) == 1:
        return liste
    else:
        milieu = len(liste) // 2
        gauche = tri_fusion_recursive(liste,  gauche_index, milieu)
        droite = tri_fusion_recursive(liste, milieu+1, droite_index)
        return fusion(gauche, droite)

def Tri_fusion(liste:list):
    """
    Cette fonction prend une liste en entrée et renvoie une nouvelle liste triée selon le principe du tri fusion.
    """
    return tri_fusion_recursive(liste, 0, len(liste))
    
def trie_rapide(liste:list):
    """
    Cette fonction prend une liste en entrée et renvoie une nouvelle liste triée selon le principe du tri rapide du cour.
    """
    if len(liste) <= 1:
        return liste
    pivot = liste[0]
    left = [x for x in liste[1:] if x <= pivot]
    right = [x for x in liste[1:] if x > pivot]
    return trie_rapide(left) + [pivot] + trie_rapide(right)

def est_Permute(liste:list):
    """
    retourne True ou False selon qu'une liste L soit une permutation de l'ensemble {1, 2, ..., n}, où n est égal à la longueur de L
    """
    return set(liste) == set(range(1, len(liste) + 1))

def est_pangramme(chaine):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    lettres_chaine = set(chaine.lower())
    return alphabet.issubset(lettres_chaine)

if __name__ == "__main__":
    scrabbleT = ( (1, "EAINORSTUL"), (2, "DMG"), (3, "BCP"), (4, "FHV"), (8, "JQ"), (10, "KWXYZ") )

    points_lettres = {}

    for points, lettres in scrabbleT:
        for lettre in lettres:
            points_lettres[lettre] = points


import random

def creer_fichier_aleatoire(n, nom_fichier):
    """Crée un fichier texte avec `n` lignes, chacune contenant un entier aléatoire entre 1 et 100."""
    with open(nom_fichier, 'w') as fichier:
        for _ in range(n):
            fichier.write(f"{random.randint(1, 100)}\n")
    print(f"Fichier '{nom_fichier}' créé avec {n} lignes.")

import random

def creer_fichier_aleatoire(n, nom_fichier):
    """Crée un fichier texte avec `n` lignes, chacune contenant un entier aléatoire entre 1 et 100."""
    with open(nom_fichier, 'w') as fichier:
        for _ in range(n):
            fichier.write(f"{random.randint(1, 100)}\n")
    print(f"Fichier '{nom_fichier}' créé avec {n} lignes.")

def fizz_buzz_fichier(nom_fichier):
    """Lit un fichier contenant des entiers et remplace chaque ligne par le résultat du jeu Fizz Buzz."""
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
    
    # Traitement FizzBuzz de chaque ligne
    with open(nom_fichier, 'w') as fichier:
        for ligne in lignes:
            nombre = int(ligne.strip())
            if nombre % 3 == 0 and nombre % 5 == 0:
                fichier.write("FizzBuzz\n")
            elif nombre % 3 == 0:
                fichier.write("Fizz\n")
            elif nombre % 5 == 0:
                fichier.write("Buzz\n")
            else:
                fichier.write(f"{nombre}\n")
    print(f"Fichier '{nom_fichier}' modifié avec les règles de FizzBuzz.")

def text_to_dico(texte:str):
    dict = {}
    for i in texte:
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz':
            if i.lower() in dict:
                dict[i.lower()] += 1
            else:
                dict[i.lower()] = 1
    return dict

def romain_to_arabe(nb: str):
    """Convertit un nombre romain en nombre arabe."""
    val = 0
    i = 0
    dict = {
         'I' : 1,
         'V' : 5,
         'X' : 10, 
         'L' : 50, 
         'C' : 100, 
         'D' : 500, 
         'M' : 1000
    }
    while i < len(nb):
        if i+1 < len(nb) and dict[nb[i]] >= dict[nb[i+1]] or i+1 == len(nb):
            val = val + dict[nb[i]]
        elif i+1 < len(nb) and dict[nb[i]] < dict[nb[i+1]]:
            val = val + dict[nb[i+1]] - dict[nb[i]]
            i+=1
        i+=1
    return val

def trouve_anagrammes(mots: str):
    if len(mots) == 1:
        return [mots]
    tout_anagrammes = []
    for i in range(len(mots)):
        anagrame_actuelle = mots[i]
        reste_mots = mots[:i] + mots[i+1:]
        for anagrame in trouve_anagrammes(reste_mots):
             tout_anagrammes.append(anagrame_actuelle + anagrame)
    return tout_anagrammes

def anagrammes(mots: str):
    liste_anagramme = trouve_anagrammes(mots)
    resultat = []
    for i in liste_anagramme:
        if not i in resultat:
            resultat.append(i)
    return resultat