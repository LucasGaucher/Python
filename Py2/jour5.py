"""
Author: L. GAUCHER
Creation Date: 07/11/1524 14:12
"""
from time import*
from tkinter import *
from random import randint
from jour4 import *

class ForestGUI:
    
    def __init__(self, ligne, colonne, spawn_pourcentage, PXCASE):
        self.__foret = Foret(ligne, colonne, spawn_pourcentage)
       
        self.__PXCASE = PXCASE
        self.__root = Tk()
        self.__root.title("Forest Fire Simulation")
        self.__put_state = None #l'état quand on pose une foret/ du feu / de l'eau 
        self.__generation = 0
        self.__running = False
        self.fps_list = []

        # Canvas to display the forest
        self.__canvas = Canvas(self.__root, width=colonne * self.__PXCASE, height=ligne * self.__PXCASE, bg="white")
        self.__canvas.grid(row=0, column=0, rowspan=6)


        self.__start_button = Button(self.__root, text="Start", command=self.start)
        self.__start_button.grid(row=0, column=1)
        
        self.__stop_button = Button(self.__root, text="Stop", command=self.stop)
        self.__stop_button.grid(row=1, column=1)
        
        self.__next_button = Button(self.__root, text="Next", command=self.next_generation)
        self.__next_button.grid(row=2, column=1)
        
        #CheckButtons
        self.__key = IntVar()
        self.__put_fire_button = Checkbutton(self.__root, text="Put Fire", variable=self.__key, command=self.put_fire_or_not)
        self.__put_fire_button.grid(row=0, column=2)
        
        self.__put_tree_button = Checkbutton(self.__root, text="Put tree", variable=self.__key, command=self.put_tree_or_not)
        self.__put_tree_button.grid(row=1, column=2)
        
        self.__put_water_button = Checkbutton(self.__root, text="Put Water", variable=self.__key, command=self.put_water_or_not)
        self.__put_water_button.grid(row=2, column=2)
        
        self.__canvas.bind('<Button-1>',self.put_actual_state)
        
        #random Buton 
        self.__random_fire_button = Button(self.__root, text="Random Fire", command=self.random_fire)
        self.__random_fire_button.grid(row=0, column=3)
        
        self.__random_tree_button = Button(self.__root, text="Random tree", command=self.random_tree_generation)
        self.__random_tree_button.grid(row=1, column=3)
        
        self.__random_water_button = Button(self.__root, text="Random water", command=self.random_water)
        self.__random_water_button.grid(row=2, column=3)
        
        #novelle foret/gen infinie
        self.__new_forest = Button(self.__root, text="Nouvelle Foret", command=self.nouvelle_foret)
        self.__new_forest.grid(row=0, column=4)
        
        self.__run_simulation_infini_button = Button(self.__root, text="Simulation infini", command=self.run_simulation_infini)
        self.__run_simulation_infini_button.grid(row=1, column=4)
        
        #information tiers
        self.__generation_label = Label(self.__root, text="Generation: 0")
        self.__generation_label.grid(row=5, column=1)
        
        self.__state_to_put_label = Label(self.__root,text="vous posez actulelemnt " + self.know_put_state())
        self.__state_to_put_label.grid(row=5, column=2)

        self.__proportion_label = Label(self.__root, text="Proportion of Trees: {:.2f}".format(self.__foret.calculer_proportion_darbre()))
        self.__proportion_label.grid(row=5, column=3)
        
        self.__fps_label = Label(self.__root, text="temps pour faire une génération: {:.2f}".format(self.calculer_fps_moyens()))
        self.__fps_label.grid(row=5, column=4)

        self.update_canvas()
        self.__root.mainloop()

    def start(self):
        self.__running = True
        self.run_simulation()

    def stop(self):
        self.__running = False

    def know_put_state(self):
        if self.__put_state == 'fire':
            return "du feu"
        elif self.__put_state == 'tree':
            return "des Arbres"
        elif self.__put_state == 'water':
            return "de l'eau"
        else:
            return "rien"

    def calculer_fps_moyens(self):
        return sum(self.fps_list)/len(self.fps_list) if len(self.fps_list)>0 else 0

    def next_generation(self):
        self.start()
        self.stop()

    def nouvelle_foret(self):
        self.stop()
        self.__generation = 0
        self.__foret = Foret(self.__foret._Foret__lignes, self.__foret._Foret__colonnes, self.__foret._Foret__spawn_pourcentage)
        self.update_canvas()
        
    def arbre_vivant(self):
        arbre_vivant = []
        for i in range(len(self.__foret._Foret__grille)):
            for j in range(len(self.__foret._Foret__grille[i])):
                if self.__foret._Foret__grille[i][j].get_etat() == 1:
                    arbre_vivant.append((i,j))
        return arbre_vivant
    
    def put_actual_state(self, event):
        if self.__key.get()==1 and self.__put_state is not None:
            arbre_vivant = self.arbre_vivant()
            if not arbre_vivant == []:
                stat_to_int={
                    'fire': 2,
                    'tree': 1,
                    'water': 0
                }
                ligne = event.y//self.__PXCASE
                colonne = event.x//self.__PXCASE
                self.__foret._Foret__grille[ligne][colonne].set_etat(stat_to_int[self.__put_state])
            self.update_canvas()
    
    def put_fire_or_not(self):
        if self.__key.get()==1:
            self.__put_state = 'fire'
            self.__canvas.focus_set()
        else:
            self.__root.focus_set()
            self.__put_state = None
        self.update_canvas()
    
    def put_tree_or_not(self):
        if self.__key.get()==1:
            self.__put_state='tree'
            self.__canvas.focus_set()
        else:
            self.__root.focus_set()
            self.__put_state = None
        self.update_canvas()
    
    def put_water_or_not(self):
        if self.__key.get()==1:
            self.__put_state='water'
            self.__canvas.focus_set()
        else:
            self.__root.focus_set()
            self.__put_state = None
        self.update_canvas()
    
    def random_fire(self):
        arbre_vivant = self.arbre_vivant()
        if not arbre_vivant == []:
            arbre_random = randint(0,len(arbre_vivant)-1)
            ligne = arbre_vivant[arbre_random][0]
            colonne = arbre_vivant[arbre_random][1]
            self.__foret._Foret__grille[ligne][colonne].set_etat(2)
        self.update_canvas()

    def random_tree_generation(self):
        arbre_pas_vivant = []
        for i in range(len(self.__foret._Foret__grille)):
            for j in range(len(self.__foret._Foret__grille[i])):
                if not(self.__foret._Foret__grille[i][j].get_etat() == 1):
                    arbre_pas_vivant.append((i,j))
        if not arbre_pas_vivant == []:
            arbre_random = randint(0,len(arbre_pas_vivant)-1)
            ligne = arbre_pas_vivant[arbre_random][0]
            colonne = arbre_pas_vivant[arbre_random][1]
            self.__foret._Foret__grille[ligne][colonne].set_etat(1)
        self.update_canvas()

    def random_water(self):
        arbre_pas_vivant = []
        for i in range(len(self.__foret._Foret__grille)):
            for j in range(len(self.__foret._Foret__grille[i])):
                if not(self.__foret._Foret__grille[i][j].get_etat() == 0):
                    arbre_pas_vivant.append((i,j))
        if not arbre_pas_vivant == []:
            arbre_random = randint(0,len(arbre_pas_vivant)-1)
            ligne = arbre_pas_vivant[arbre_random][0]
            colonne = arbre_pas_vivant[arbre_random][1]
            self.__foret._Foret__grille[ligne][colonne].set_etat(0)
        self.update_canvas()

    def update_canvas(self):
        self.__canvas.delete("all")
        for i, ligne in enumerate(self.__foret._Foret__grille):
            for j, arbre in enumerate(ligne):
                color = self.get_color(arbre.get_etat())
                x0, y0 = j * self.__PXCASE, i * self.__PXCASE
                x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE
                self.__canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
        self.__generation_label.config(text=f"Generation: {self.__generation}")
        self.__proportion_label.config(text="Proportion of Trees: {:.2f}".format(self.__foret.calculer_proportion_darbre()))
        self.__state_to_put_label.config(text="vous posez actulelemnt " + self.know_put_state())
        self.__fps_label.config(text="temps pour faire une génération:" + str(self.calculer_fps_moyens())[:5] +'sec')   
        
    def get_color(self, etat):
        return ["blue", "green", "red", "grey"][etat]
    
    def is_there_fire(self):
        return any(cell._Arbre__etat == 2 for row in self.__foret._Foret__grille for cell in row)

    def is_there_life(self):
        return any(cell._Arbre__etat == 1 for row in self.__foret._Foret__grille for cell in row)
    
    def run_simulation(self):
        if self.__running and self.is_there_fire():
            t1 = time()
            self.__foret.mise_a_jour()
            self.__generation += 1
            self.update_canvas()
            t2 = time()
            self.fps_list += [t2-t1]
            self.__root.after(5, self.run_simulation)
    
    def run_simulation_infini(self):
        if self.is_there_life() and not(self.is_there_fire()):
            self.random_fire()      
        elif not(self.is_there_fire()) and not(self.is_there_life()):
            self.nouvelle_foret()
        else:
            self.__foret.mise_a_jour()
            self.__generation += 1
            self.update_canvas()
        self.__root.after(50, self.run_simulation_infini)
        


class JeuDeLaVieGUI:   
    def __init__(self, ligne, colonne, spawn_pourcentage, PXCASE):
        self.__cell = JeuDeLaVie(ligne, colonne, spawn_pourcentage)
        self.__nb_cases = ligne * colonne
        self.__PXCASE = PXCASE
        self.__put_state = None
        self.fps_list = []
        self.__root = Tk()
        self.__root.title("Jeu de la vie Simulation")

        self.__generation = 0
        self.__running = False

        # Canvas to display the forest
        self.__canvas = Canvas(self.__root, width=colonne * self.__PXCASE, height=ligne * self.__PXCASE, bg="white")
        self.__canvas.grid(row=0, column=0, rowspan=8)

        #start/stop/next generation
        self.__start_button = Button(self.__root, text="Start", command=self.start)
        self.__start_button.grid(row=0, column=1)
        
        self.__stop_button = Button(self.__root, text="Stop", command=self.stop)
        self.__stop_button.grid(row=1, column=1)
        
        self.__next_button = Button(self.__root, text="Next", command=self.next_generation)
        self.__next_button.grid(row=2, column=1)
        
        
        #modifier vie aléatoirement
        self.__random_life_button = Button(self.__root, text="Créer la vie aléatoirement", command=self.random_life)
        self.__random_life_button.grid(row=0, column=2)
        
        self.__10_random_life_button = Button(self.__root, text="10% de vie", command=self.random_10_life)
        self.__10_random_life_button.grid(row=1, column=2)
        
        self.__random_dead_button = Button(self.__root, text="Créer la mort aléatoirement", command=self.random_dead)
        self.__random_dead_button.grid(row=2, column=2)
        
        self.__10_random_dead_button = Button(self.__root, text="10% de mort", command=self.random_10_dead)
        self.__10_random_dead_button.grid(row=3, column=2)
        
        
        #modifier vie manuelement
        self.__key = IntVar()
        self.__put_fire_button = Checkbutton(self.__root, text="Born a new person", variable=self.__key, command=self.put_born_ppl_or_not)
        self.__put_fire_button.grid(row=0, column=3)
        
        self.__put_tree_button = Checkbutton(self.__root, text="commit murder", variable=self.__key, command=self.put_murder_smn_or_not)
        self.__put_tree_button.grid(row=1, column=3)
        
        self.__put_water_button = Checkbutton(self.__root, text="Changement d'état", variable=self.__key, command=self.put_change_state_or_not)
        self.__put_water_button.grid(row=2, column=3)
        
        self.__canvas.bind('<Button-1>',self.put_actual_state)
        
        #modifier letat peut importe quil soit mort ou vivant
        self.__random_life_button = Button(self.__root, text="modifier une habtitation", command=self.changement_detat)
        self.__random_life_button.grid(row=0, column=4)
        
        self.__10_random_changement_d_etat_button = Button(self.__root, text="modifier 10% d'habtitation", command=self.changement_detat_10)
        self.__10_random_changement_d_etat_button.grid(row=1, column=4)
        
        
        #stats
        self.__generation_label = Label(self.__root, text="Generation: 0")
        self.__generation_label.grid(row=6, column=1)
        
        self.__state_to_put_label = Label(self.__root,text=self.know_put_state())
        self.__state_to_put_label.grid(row=6, column=3)

        self.__proportion_label = Label(self.__root, text="Proportion of Life: {:.2f}".format(self.__cell.calculer_proportion_dhabitant()))
        self.__proportion_label.grid(row=6, column=2)
        
        self.__fps_label = Label(self.__root, text="temps pour faire une génération: {:.2f}".format(self.calculer_fps_moyens()))
        self.__fps_label.grid(row=6, column=4)
        
        self.update_canvas()
        self.__root.mainloop()

    def start(self):
        self.__running = True
        self.run_simulation()

    def stop(self):
        self.__running = False

    def put_born_ppl_or_not(self):
        if self.__key.get()==1:
            self.__put_state = 'Born'
            self.__canvas.focus_set()
        else:
            self.__root.focus_set()
            self.__put_state = None
        self.update_canvas()
        
    def put_murder_smn_or_not(self):
        if self.__key.get()==1:
            self.__put_state = 'murder'
            self.__canvas.focus_set()
        else:
            self.__root.focus_set()
            self.__put_state = None
        self.update_canvas()
    
    def put_change_state_or_not(self):
        if self.__key.get()==1:
            self.__put_state = 'both'
            self.__canvas.focus_set()
        else:
            self.__root.focus_set()
            self.__put_state = None
        self.update_canvas()

    def population_vivante(self):
        population_vivante = []
        for i in range(len(self.__cell._JeuDeLaVie__grille)):
            for j in range(len(self.__cell._JeuDeLaVie__grille[i])):
                if self.__cell._JeuDeLaVie__grille[i][j].get_etat() == 1:
                    population_vivante.append((i,j))
        return population_vivante
    
    def calculer_fps_moyens(self):
        return sum(self.fps_list)/len(self.fps_list) if len(self.fps_list)>0 else 0
    
    def put_actual_state(self, event):
        if self.__key.get()==1 and self.__put_state is not None:
            population_vivante = self.population_vivante()
            if not population_vivante == []:
                
                ligne = event.y//self.__PXCASE
                colonne = event.x//self.__PXCASE
                stat_to_int={
                    'Born': 1,
                    'murder': 0,
                    'both': 2-(self.__cell._JeuDeLaVie__grille[ligne][colonne].get_etat()+1)
                }
                self.__cell._JeuDeLaVie__grille[ligne][colonne].set_etat(stat_to_int[self.__put_state])
            self.update_canvas()
    
    def next_generation(self):
        self.start()
        self.stop()

    def random_life(self):
        personne_vivant = []
        for i in range(len(self.__cell._JeuDeLaVie__grille)):
            for j in range(len(self.__cell._JeuDeLaVie__grille[i])):
                if self.__cell._JeuDeLaVie__grille[i][j].get_etat() == 0:
                    personne_vivant.append((i,j))
        if not personne_vivant == []:
            personne_random = randint(0,len(personne_vivant)-1)
            ligne = personne_vivant[personne_random][0]
            colonne = personne_vivant[personne_random][1]
            self.__cell._JeuDeLaVie__grille[ligne][colonne].set_etat(1)
        self.update_canvas()

    def random_10_life(self):
        for i in range(self.__nb_cases//10):
            self.random_life()

    def random_dead(self):
        personne_morte = []
        for i in range(len(self.__cell._JeuDeLaVie__grille)):
            for j in range(len(self.__cell._JeuDeLaVie__grille[i])):
                if self.__cell._JeuDeLaVie__grille[i][j].get_etat() == 1:
                    personne_morte.append((i,j))
        if not personne_morte == []:
            personne_random = randint(0,len(personne_morte)-1)
            ligne = personne_morte[personne_random][0]
            colonne = personne_morte[personne_random][1]
            self.__cell._JeuDeLaVie__grille[ligne][colonne].set_etat(0)
        self.update_canvas()
        
    def random_10_dead(self):
        for i in range(self.__nb_cases//10):
            self.random_dead()

    def changement_detat(self):
        victim = randint(0,len(self.__cell._JeuDeLaVie__grille)-1), randint(0,len(self.__cell._JeuDeLaVie__grille[0])-1)
        new_state = 2-(self.__cell._JeuDeLaVie__grille[victim[0]][victim[1]].get_etat()+1)
        self.__cell._JeuDeLaVie__grille[victim[0]][victim[1]].set_etat(new_state)
        self.update_canvas()
        
    def changement_detat_10(self):
        for i in range(self.__nb_cases//10):
            self.changement_detat()
                
    def update_canvas(self):
        self.__canvas.delete("all")
        for i, ligne in enumerate(self.__cell._JeuDeLaVie__grille):
            for j, personne in enumerate(ligne):
                color = self.get_color(personne.get_etat())
                x0, y0 = j *self.__PXCASE, i *self.__PXCASE
                x1, y1 = x0 +self.__PXCASE, y0 +self.__PXCASE
                self.__canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
        self.__generation_label.config(text=f"Generation: {self.__generation}")
        self.__proportion_label.config(text="Proportion of Life: {:.2f}".format(self.__cell.calculer_proportion_dhabitant()))
        self.__state_to_put_label.config(text=self.know_put_state())
        self.__fps_label.config(text="temps pour faire une génération:" + str(self.calculer_fps_moyens())[:5] +'sec')

    def get_color(self, etat):
        return ["Black", "lightblue"][etat]
    
    def sign_of_life(self):
        return any(cellule.get_etat() == 1 for row in self.__cell.get_grille() for cellule in row)

    def know_put_state(self):
        if self.__put_state == 'Born':
            return "vous creez la vie"
        elif self.__put_state == 'murder':
            return "vous détuisez la vie"
        elif self.__put_state == 'both':
            return "vous faites les deux"
        else:
            return None
    
    def run_simulation(self):
        if self.__running and self.sign_of_life():
            t1 = time()
            self.__cell.mise_a_jour()
            self.__generation += 1
            self.update_canvas()
            t2 = time()
            self.fps_list += [t2-t1]
            #self.__root.after(250, self.run_simulation)
            self.__root.after(1, self.run_simulation)


# Initialize the forest GUI with dimensions and a spawn percentage
hauteur = 26
largeueur = 30
proba = 3/5
longueur_et_largeur_dune_cellule = 30
forest_app = ForestGUI(hauteur, largeueur, proba, longueur_et_largeur_dune_cellule)
JeuDeLaVieApp = JeuDeLaVieGUI(hauteur, largeueur, proba, longueur_et_largeur_dune_cellule)