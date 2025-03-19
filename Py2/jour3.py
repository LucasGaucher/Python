"""
Author: L. GAUCHER
Creation Date: 05/11/2024 11:02
"""

import math

class Circle:
    
    PI = 3.14159
    
    def __init__(self, radius=1, x_center=0, y_center=0):
        self._radius = abs(radius)
        self._x_center = x_center
        self._y_center = y_center
    

    def get_radius(self):
        return self._radius
    
    def get_x_center(self):
        return self._x_center
    
    def get_y_center(self):
        return self._y_center
    

    def set_radius(self, radius):
        self._radius = abs(radius)
    
    def set_x_center(self, x_center):
        self._x_center = x_center
    
    def set_y_center(self, y_center):
        self._y_center = y_center
    

    def area(self):
        return Circle.PI * self._radius ** 2
    

    def perimeter(self):
        return 2 * Circle.PI * self._radius
    

    def display(self):
        print(f"Centre: ({self._x_center}, {self._y_center}), Rayon: {self._radius}")
    

    def is_point_inside(self, x, y):
        distance = (x - self._x_center) ** 2 + (y - self._y_center) ** 2
        return distance <= self._radius**2
    

    def translate(self, dx, dy):
        self._x_center += dx
        self._y_center += dy
    

    def scale(self, factor):
        self._radius *= factor

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    

    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y
    

    def translate(self, dx, dy):
        self._x += dx
        self._y += dy

class Circle:
    PI = 3.14159
    
    def __init__(self, radius=1, center=None):
        self._radius = abs(radius)
        self._center = center if center else Point(0, 0)
    
    
    def get_radius(self):
        return self._radius
    
    def get_center(self):
        return self._center
    

    def set_radius(self, radius):
        self._radius = abs(radius)
    
    def set_center(self, center):
        self._center = center
    

    def area(self):
        return Circle.PI * self._radius ** 2
    

    def perimeter(self):
        return 2 * Circle.PI * self._radius
    

    def display(self):
        print(f"Centre: ({self._center.get_x()}, {self._center.get_y()}), Rayon: {self._radius}")
    

    def is_point_inside(self, x, y):
        distance = math.sqrt((x - self._center.get_x()) ** 2 + (y - self._center.get_y()) ** 2)
        return distance <= self._radius
    

    def translate(self, dx, dy):
        self._center.translate(dx, dy)
    

    def scale(self, factor):
        self._radius *= factor

from PIL import Image
import random

class AutomateCellulaire:
    def __init__(self, largeur, generations, regle, aleatoire=True):
        self.__largeur = largeur
        self.__generations = generations
        self.__regle = self.convertir_regle_en_binaire(regle)
        self.__image = Image.new("1", (largeur, generations), color=1) 
        self.__rangee = self.initialiser_rangee(aleatoire)

    def convertir_regle_en_binaire(self, regle):
        """
        Convertit un entier (0 à 255) en une liste de 8 bits representant la regle de l'automate.
        """
        return [int(x) for x in f"{regle:08b}"]

    def initialiser_rangee(self, aleatoire):
        """
        Initialise la rangee soit de façon aleatoire, soit avec une cellule centrale à 1 et le reste à 0.
        """
        if aleatoire:
            return [random.randint(0, 1) for _ in range(self.__largeur)]
        else:
            rangee = [0] * self.__largeur
            rangee[self.__largeur // 2] = 1
            return rangee

    def _mettre_a_jour_rangee(self):
        """
        Met à jour l'etat de la rangee en appliquant la regle de l'automate cellulaire.
        """
        nouvelle_rangee = [0] * self.__largeur
        for i in range(self.__largeur):
            gauche = self.__rangee[(i - 1) % self.__largeur]
            centre = self.__rangee[i]
            droite = self.__rangee[(i + 1) % self.__largeur]
            
            configuration = (gauche << 2) | (centre << 1) | droite
            nouvelle_rangee[i] = self.__regle[7 - configuration]
        self.__rangee = nouvelle_rangee

    def generer_image(self):
        """
        Genere l'image en appliquant la regle sur toutes les generations.
        """
        for generation in range(self.__generations):
            for x in range(self.__largeur):
                couleur = 1 - self.__rangee[x]
                self.__image.putpixel((x, generation), couleur)
            self._mettre_a_jour_rangee()

    def sauvegarder_image(self, nom_fichier="automate.png"):
        """
        Sauvegarde l'image generee au format PNG.
        """
        self.__image.save(nom_fichier)


if False:
    for regle in range(62, 256):
        automate = AutomateCellulaire(5120, 3200, regle, aleatoire=False)
        automate.generer_image()
        automate.sauvegarder_image("automate_cellulaire_"+str(regle)+"_4K.png")
        print("automate_cellulaire_"+str(regle)+".png fini")

#182 style
automate = AutomateCellulaire(10000, 10000, 182, aleatoire=False)
automate.generer_image()
automate.sauvegarder_image("automate_cellulaire_"+str(182)+"_100M.png")
print("automate_cellulaire_"+str(182)+".png fini")