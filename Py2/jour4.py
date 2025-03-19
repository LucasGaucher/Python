"""
Author: L. GAUCHER
Creation Date: 07/11/2024 10:36
"""
from random import randint
from time import sleep

class Arbre:
    def __init__(self, valeur=0):
        self.__etat = valeur
    
    def renvoi_etat_symbole(self):
        return ['.', 'A', 'F', 'C'][self.__etat]
    
    def get_etat(self):
        return self.__etat
    
    def set_etat(self, new_state):
        self.__etat = new_state
    
    def mise_a_jour(self, voisin_brule: bool):
        if self.__etat == 1 and voisin_brule:
            self.__etat = 2
        elif self.__etat == 2:
            self.__etat = 3

class Foret:
    def __init__(self, ligne: int, colonne: int, spawn_pourcentage:float):
        self.__lignes = ligne
        self.__colonnes = colonne
        self.__spawn_pourcentage = spawn_pourcentage
        self.__grille = [[Arbre() for _ in range(colonne)] for _ in range(ligne)]
        self.generer_foret(spawn_pourcentage)

    def generer_foret(self, spawn_pourcentage):
        for ligne in self.__grille:
            for arbre in ligne:
                if randint(0, 100) < spawn_pourcentage * 100:
                    arbre.set_etat(1)
        rand_ligne = randint(0, self.__lignes - 1)
        rand_colonne = randint(0, self.__colonnes - 1)
        self.__grille[rand_ligne][rand_colonne].set_etat(2)
    
    def calculer_proportion_darbre(self):
        return sum([[arbre.get_etat() for arbre in ligne].count(1) for ligne in self.__grille])/(self.__lignes *  self.__colonnes)
    
    def affichage(self):
        for ligne in self.__grille:
            for arbre in ligne:
                print(arbre.renvoi_etat_symbole(), end=' ')
            print()
        print("\nproportion d'arbre",self.calculer_proportion_darbre())

    def detecter_feu_proche(self, lvoisin, cvoisin):
        voisins = []
        for dl, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nl, nc = lvoisin + dl, cvoisin + dc
            if 0 <= nl < self.__lignes and 0 <= nc < self.__colonnes:
                voisins.append(self.__grille[nl][nc].get_etat() == 2)
        return any(voisins)

    def mise_a_jour(self):
        nouvelles_etats = []
        for i in range(self.__lignes):
            row_etats = []
            for j in range(self.__colonnes):
                voisin_brule = self.detecter_feu_proche(i, j)
                etat_avant = self.__grille[i][j].get_etat()
                arbre_temp = Arbre(etat_avant)
                arbre_temp.mise_a_jour(voisin_brule)
                row_etats.append(arbre_temp.get_etat())
            nouvelles_etats.append(row_etats)
        
        for i in range(self.__lignes):
            for j in range(self.__colonnes):
                self.__grille[i][j].set_etat(nouvelles_etats[i][j])

    def simulation(self, nb_generation: int, cooldown=5):
        for i in range(nb_generation):
            print("Generation" + str(i + 1))
            self.affichage()
            print()
            self.mise_a_jour()
            print()
            sleep(cooldown)

class Foret_torides(Foret):
    def __init__(self, ligne: int, colonne: int, spawn_pourcentage: float, proportion_arbre: float):
        Foret.__init__(self, ligne, colonne, spawn_pourcentage,  proportion_arbre)
        
    def detecter_feu_proche(self, lvoisin, cvoisin):
        voisins = []
        for dl, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nl, nc = (lvoisin + dl)%self._colonnes , (cvoisin + dc)%self._Foret__lignes
            voisins.append(self.__grille[nl][nc].get_etat() == 2)
        return any(voisins)

class Cellule:
    def __init__(self, etat=0):
        self.__etat = etat
    
    def renvoi_etat_symbole(self):
        return ['M', 'V'][self.__etat]
    
    def mise_a_jour(self, nb_voisin: int):
        if self.__etat == 0:#si il es mort
            if nb_voisin==3:
                self.__etat = 1
        else:#si il es vivant
            if nb_voisin in [2,3]:
                self.__etat = 1
            else:
                self.__etat = 0
    
    def est_vivant(self):
        return self.__etat == 1
    
    def get_etat(self):
        return self.__etat
    
    def set_etat(self, new_state):
        self.__etat = new_state


class JeuDeLaVie:
    def __init__(self, ligne: int, colonne: int, spawn_pourcentage: float):
        self.__lignes = ligne
        self.__colonnes = colonne
        self.__grille = [[Cellule() for _ in range(colonne)] for _ in range(ligne)]
        self.generer_ville(spawn_pourcentage)
        
    def generer_ville(self, spawn_pourcentage):
        for ligne in self.__grille:
            for habitant in ligne:
                if randint(0, 100) < spawn_pourcentage * 100:
                    habitant.set_etat(1)

    def calculer_proportion_dhabitant(self):
        return sum([[arbre._Cellule__etat for arbre in ligne].count(1) for ligne in self.__grille])/(self.__lignes *  self.__colonnes)

    def affichage(self):
        for ligne in self.__grille:
            for habitant in ligne:
                print(habitant.renvoi_etat_symbole(), end=' ')
            print()
        print("\nproportion d'habitant",self.calculer_proportion_dhabitant())
    
    def compter_voisin_vivant(self, lvoisin, cvoisin):
        voisins = 0
        for dl, dc in [(i, -1) for i in range(-1,2)] + [(i, 0) for i in range(-1,2,2)] + [(i, 1) for i in range(-1,2)]:
            nl, nc = lvoisin + dl, cvoisin + dc
            if 0 <= nl < self.__lignes and 0 <= nc < self.__colonnes:
                if self.__grille[nl][nc].est_vivant():
                    voisins += 1
        return voisins

    def mise_a_jour(self):
        nouvelles_etats = []
        for i in range(self.__lignes):
            row_etats = []
            for j in range(self.__colonnes):
                voisin_brule = self.detecter_feu_proche(i, j)
                etat_avant = self.__grille[i][j].get_etat()
                arbre_temp = Arbre(etat_avant)
                arbre_temp.mise_a_jour(voisin_brule)
                row_etats.append(arbre_temp.get_etat())
            nouvelles_etats.append(row_etats)
        
        self.__grille = nouvelles_etats

    def simulation(self, nb_generation: int, cooldown=5):
        for i in range(nb_generation):
            print("Generation" + str(i + 1))
            self.affichage()
            print()
            self.mise_a_jour()
            print()
            sleep(cooldown)
            
    def get_grille(self):
        return self.__grille

import random
from time import sleep

class Cellule:
    def __init__(self, etat=0):
        self.__etat = etat  # 0 pour morte, 1 pour vivante
    
    def renvoi_etat_symbole(self):
        return ['M', 'V'][self.__etat]  # 'M' pour mort, 'V' pour vivant
    
    def mise_a_jour(self, nb_voisin: int):
        # Si la cellule est morte et a 3 voisins vivants, elle prend vie.
        if self.__etat == 0:
            if nb_voisin == 3:
                self.__etat = 1
        else:
            # Si la cellule est vivante, elle reste vivante si elle a 2 ou 3 voisins vivants.
            if nb_voisin not in [2, 3]:
                self.__etat = 0
    
    def est_vivant(self):
        return self.__etat == 1
    
    def get_etat(self):
        return self.__etat
    
    def set_etat(self, new_state):
        self.__etat = new_state

class JeuDeLaVie:
    def __init__(self, ligne: int, colonne: int, spawn_pourcentage: float):
        self.__lignes = ligne
        self.__colonnes = colonne
        self.__grille = [[Cellule() for _ in range(colonne)] for _ in range(ligne)]
        self.generer_ville(spawn_pourcentage)
        
    def generer_ville(self, spawn_pourcentage):
        """Initialise la grille avec un pourcentage donné de cellules vivantes"""
        for ligne in self.__grille:
            for habitant in ligne:
                if random.randint(0, 100) < spawn_pourcentage * 100:
                    habitant.set_etat(1)

    def calculer_proportion_dhabitant(self):
        """Calcule la proportion de cellules vivantes dans la grille"""
        return sum([cell.get_etat() == 1 for ligne in self.__grille for cell in ligne]) / (self.__lignes * self.__colonnes)

    def affichage(self):
        """Affiche la grille et la proportion de cellules vivantes"""
        for ligne in self.__grille:
            for habitant in ligne:
                print(habitant.renvoi_etat_symbole(), end=' ')
            print()
        print("\nProportion d'habitants:", self.calculer_proportion_dhabitant())
    
    def compter_voisin_vivant(self, lvoisin, cvoisin):
        """Compte le nombre de voisins vivants d'une cellule donnée"""
        voisins = 0
        for dl, dc in [(i, -1) for i in range(-1, 2)] + [(i, 0) for i in range(-1, 2, 2)] + [(i, 1) for i in range(-1, 2)]:
            nl, nc = lvoisin + dl, cvoisin + dc
            if 0 <= nl < self.__lignes and 0 <= nc < self.__colonnes:
                if self.__grille[nl][nc].est_vivant():
                    voisins += 1
        return voisins

    def mise_a_jour(self):
        """Met à jour l'état de chaque cellule en fonction de ses voisins"""
        nouvelles_etats = []
        for i in range(self.__lignes):
            row_etats = []
            for j in range(self.__colonnes):
                nb_voisins = self.compter_voisin_vivant(i, j)
                etat_avant = self.__grille[i][j].get_etat()
                self.__grille[i][j].mise_a_jour(nb_voisins)
                row_etats.append(self.__grille[i][j].get_etat())
            nouvelles_etats.append(row_etats)
        
        # Mise à jour de la grille
        for i in range(self.__lignes):
            for j in range(self.__colonnes):
                self.__grille[i][j].set_etat(nouvelles_etats[i][j])

    def simulation(self, nb_generation: int, cooldown=5):
        """Simule plusieurs générations avec un délai entre chaque affichage"""
        for i in range(nb_generation):
            print(f"Generation {i + 1}")
            self.affichage()
            self.mise_a_jour()
            print()
            sleep(cooldown)
            
    def get_grille(self):
        """Retourne la grille actuelle"""
        return self.__grille
