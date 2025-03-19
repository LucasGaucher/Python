"""
Author: Lucas GAUCHER
created: 16/11/2024 17:22
"""
from tkinter import*
from tkinter import messagebox
from random import choice, randint


class Joueur:
    def __init__(self,name,  player, nb_cases, is_bot):
        self.__nom = name
        self.__queen_pos = (0,0) if nb_cases is None or player not in [1,2] else (nb_cases-1, 0) if player == 1 else (0, nb_cases-1)
        self.__nb_pions = 0 if nb_cases is None else (nb_cases**2)//4
        self.__type = 'bot' if is_bot else 'player'
    
    def get_type(self):
        return self.__type
    def get_name(self):
        return self.__nom
    
    def get_queen_pos(self):
        return self.__queen_pos
    
    def get_nb_pions(self):
        return self.__nb_pions
    
    def set_queen_pos(self, pos):
        self.__queen_pos = pos
        
    def one_pions_down(self):
        self.__nb_pions -= 1
        
class Theme:
    def __init__(self, theme_name, forme_pions):
        """
        Initialise le thème avec un nom et une forme de pion.
        """
        self.__PXCASE = 50 #taille de la case
        # Attributs des couleurs pour personnalisation
        self.__couleurs_cases = None
        self.__couleurs_grille_texte = None
        self.__players_couleurs_tour = None
        self.__players_couleurs_tour_selected = None
        self.__players_couleurs_reine = None
        self.__players_couleurs_reine_selected = None

        # Attributs supplémentaires
        self.__forme_pions = [None, None]  # Forme des pions

        # Initialisation des couleurs et de la forme en fonction du thème
        
        if forme_pions[0] == "random":
            forme_pions[0] = choice(["cercle","losange","rectangle"])
        if forme_pions[1] == "random":
            forme_pions[1] = choice(["cercle","losange","rectangle"])

        self.__definir_color(theme_name)
        self.__definir_shape(forme_pions)
        
        
    def __definir_color(self, theme_name):
        """
        Définit les couleurs et attributs spécifiques selon le nom du thème
        et la forme des pions.
        """
        colors_theme = {
            "basic": ['#FFFFFF', '#000000',
                      ['#0000ff', '#ff0000'],
                      ['#00F2FF', '#43FF00'],
                      ['#FF00FF', '#FFA500'],
                      ['#A1097D', '#F24213']],
            "Pastel Sugar": ['#FFFFFF', '#000000',
                             ['#BA6E6E', '#A63A50'],
                             ['#E8DBC5', '#A1674A'],
                             ['#A9CEF4', '#74A0B7'],
                             ['#d9863b', '#F09D51']]
        }

        # Si le thème existe, applique ses couleurs et autres propriétés
        if theme_name in colors_theme:
            theme = colors_theme[theme_name]
            self.__couleurs_cases = theme[0]
            self.__couleurs_grille_texte = theme[1]
            self.__players_couleurs_tour = theme[2]
            self.__players_couleurs_tour_selected = theme[3]
            self.__players_couleurs_reine = theme[4]
            self.__players_couleurs_reine_selected = theme[5]

        elif theme_name == 'random, peut être instable':
            # Choisir aléatoirement des couleurs pour les cases et le texte
            self.__couleurs_cases = '#' + ''.join([choice('0123456789ABCDEF') for _ in range(6)])
            self.__couleurs_grille_texte = '#' + ''.join([choice('0123456789ABCDEF') for _ in range(6)])
            self.__couleurs_grille_texte = '#' + ''.join([choice('0123456789ABCDEF') for _ in range(6)])
            self.__players_couleurs_tour = ['#' + ''.join([choice('0123456789ABCDEF') for _ in range(6)]), '#' + ''.join([choice('0123456789ABC') for _ in range(6)])]
            self.__players_couleurs_tour_selected = ['#' + ''.join([choice('0123456789ABCDEF') for _ in range(6)]), '#' + ''.join([choice('0123456789ABC') for _ in range(6)])]
            self.__players_couleurs_reine = ['#' + ''.join([choice('0123456789ABCDEF') for _ in range(6)]), '#' + ''.join([choice('0123456789ABC') for _ in range(6)])]
            self.__players_couleurs_reine_selected = ['#' + ''.join([choice('0123456789ABCDEF') for _ in range(6)]), '#' + ''.join([choice('0123456789ABC') for _ in range(6)])]
        else:
            # Valeurs par défaut si le thème est inconnu
            self.__couleurs_cases = '#CCCCCC'
            self.__couleurs_grille_texte = '#000000'
            self.__players_couleurs_tour = ['#AAAAAA', '#BBBBBB']
            self.__players_couleurs_tour_selected = ['#888888', '#777777']
            self.__players_couleurs_reine = ['#444444', '#555555']
            self.__players_couleurs_reine_selected = ['#222222', '#333333']
        
        
    def __definir_shape(self, forme_pions):
        """
        Defines the shapes of the pieces for both players based on the provided names.
        """
        def draw_circle(x, y, color, plateau):
            x1, y1 = x + self.__PXCASE, y + self.__PXCASE
            return plateau.create_oval(x+5, 
                                       y+5, 
                                       x1-5, 
                                       y1-5,
                                       fill=color, 
                                       outline=color)
        
        def draw_losange(x, y, color, plateau):
            px = self.__PXCASE
            cx, cy = x  + px // 2, y + px // 2  # centre
            
            return plateau.create_polygon(
                cx, y + 5,  # en haut                
                x + 5, cy,  # gauche
                cx, y +  px - 5,  # bas
                x + px - 5, cy,  # droite

                fill=color, outline=color
            )
        
        def draw_square(x, y, color, plateau):
            return plateau.create_rectangle(
                x + 5, y + 5,
                x + self.__PXCASE - 5, y + self.__PXCASE - 5,
                fill=color, outline=color
            )
        
        # Map shapes to their respective functions
        shape_theme = {
            "cercle": draw_circle,
            "losange": draw_losange,
            "rectangle": draw_square
        }

        # Assign shapes to players
        self.__forme_pions = [
            shape_theme.get(forme_pions[0], draw_circle),  # Default to circle if not found
            shape_theme.get(forme_pions[1], draw_circle)
        ]
            
    def get_colors(self):
        """
        Retourne une liste de toutes les couleurs utilisées par le thème.
        """
        return [
            self.__couleurs_cases,
            self.__couleurs_grille_texte,
            self.__players_couleurs_tour,
            self.__players_couleurs_tour_selected,
            self.__players_couleurs_reine,
            self.__players_couleurs_reine_selected,
        ]

    def create_shape(self, player_number):
        """
        Retourne la forme des pions pour le joueur donné.
        """
        
        if self.__forme_pions[player_number] is not None:
            return self.__forme_pions[player_number]
        else:
            return lambda x, y, color, plateau: plateau.create_oval(x*self.__PXCASE +5, y*self.__PXCASE +5, (x+1)*self.__PXCASE -5, (y+1)*self.__PXCASE -5, fill=color, outline=color)        

class Jeu:
    def __init__(self):
        if self.see_load_game():
            self.load_game()
            self.end_game_turn()
            self.__root.mainloop()
        else:
            with open('Save.txt', 'r') as f:
                content = f.read()
            if len(content) >0 and messagebox.askyesno(title="Dellet?", message="Do you want to dellet the ancien game?"):
                with open('Save.txt', 'w') as save:
                    save.write('')
            self.__nb_cases = None #pas de plateau
            self.__root = Tk()
            self.__root.title("Jeu de plateau")
            self.__PXCASE = 50 #taille de d'une case
            self.__case_selected = None
            self.__player_1_is_bot = False
            self.__player_2_is_bot = False
            
                    
            #premiere fenetre (pour la configuration du plateau)
            
            # Conteneur principal
            self.__plateau_player_config = Frame(self.__root)
            self.__plateau_player_config.grid(row=0, column=0, sticky="n", padx=10, pady=10)

            # Ligne 1 : Configuration des joueurs côte à côte
            Label(self.__plateau_player_config, text="Joueur 1").grid(row=0, column=0, padx=10, pady=5)
            Label(self.__plateau_player_config, text="Joueur 2").grid(row=0, column=1, padx=10, pady=5)

            # Widgets pour Joueur 1
            self.__is_j1_bot = BooleanVar(value=False)
            Checkbutton(
                self.__plateau_player_config,
                text="BOT",
                variable=self.__is_j1_bot,
                command=self.toggle_player_1_bot
            ).grid(row=1, column=0, padx=10, pady=5)
            self.__player_or_bot_display_j1 = Label(
                self.__plateau_player_config,
                text="Vous êtes actuellement un joueur"
            )
            self.__player_or_bot_display_j1.grid(row=2, column=0, padx=10, pady=5)
        
            
            # Liste déroulante pour la difficulté de J1 (cachée par défaut)
            self.__j1_difficulty = StringVar(value="Bot facile")
            self.__j1_difficulty_menu = OptionMenu(
                self.__plateau_player_config,
                self.__j1_difficulty,
                "Bot facile",
                "Bot difficile niveau 1",
                "Bot difficile niveau 2",
                "Bot impossible"
            )
            self.__j1_difficulty_menu.grid(row=3, column=0, padx=10, pady=5)
            self.__j1_difficulty_menu.grid_remove()

            self.__nom_chosed_j1 = StringVar(value="Joueur 1")
            self.__nom_chosed_j1_entry = Entry(self.__plateau_player_config, textvariable=self.__nom_chosed_j1)
            self.__nom_chosed_j1_entry.grid(row=3, column=0, padx=10, pady=5)

            self.__shape_j1_chosed  = StringVar(value="cercle")
            self.__shape_j1_chosed_menu = OptionMenu(
                self.__plateau_player_config,
                self.__shape_j1_chosed,
                "cercle",
                "losange",
                "rectangle",
                "random"
            )
            self.__shape_j1_chosed_menu.grid(row=4, column=0, padx=10, pady=5)

            # Widgets pour Joueur 2
            self.__is_j2_bot = BooleanVar(value=False)
            Checkbutton(
                self.__plateau_player_config,
                text="BOT",
                variable=self.__is_j2_bot,
                command=self.toggle_player_2_bot
            ).grid(row=1, column=1, padx=10, pady=5)
            self.__player_or_bot_display_j2 = Label(
                self.__plateau_player_config,
                text="Vous êtes actuellement un joueur"
            )
            self.__player_or_bot_display_j2.grid(row=2, column=1, padx=10, pady=5)

            # Liste déroulante pour la difficulté de J2 (cachée par défaut)
            self.__j2_difficulty = StringVar(value="Bot facile")
            self.__j2_difficulty_menu = OptionMenu(
                self.__plateau_player_config,
                self.__j2_difficulty,
                "Bot facile",
                "Bot difficile niveau 1",
                "Bot difficile niveau 2",
                "Bot impossible"
            )
            self.__j2_difficulty_menu.grid(row=3, column=1, padx=10, pady=5)
            self.__j2_difficulty_menu.grid_remove()
            
            self.__nom_chosed_j2 = StringVar(value="Joueur 2")
            self.__nom_chosed_j2_entry = Entry(self.__plateau_player_config, textvariable=self.__nom_chosed_j2)
            self.__nom_chosed_j2_entry.grid(row=3, column=1, padx=10, pady=5)
                    
            self.__shape_j2_chosed  = StringVar(value="cercle")
            self.__shape_j2_chosed_menu = OptionMenu(
                self.__plateau_player_config,
                self.__shape_j2_chosed,
                "cercle",
                "losange",
                "rectangle",
                "random"
            )
            self.__shape_j2_chosed_menu.grid(row=4, column=1, padx=10, pady=5)

            # Partie 2 : Paramètres du plateau
            Label(self.__plateau_player_config, text="Paramètres du plateau").grid(
                row=5, column=0, columnspan=2, pady=(20, 5)
            )
            self.__nb_cases_listbox = Listbox(self.__plateau_player_config, height=4)
            for i in range(6, 13, 2):  # Générer les choix (6, 8, 10, 12 cases)
                self.__nb_cases_listbox.insert(END, str(i) + " cases")
            self.__nb_cases_listbox.grid(row=6, column=0, columnspan=2, pady=(5, 10))
            
            
            self.__theme_chosed = StringVar(value="Choissisez un theme(Theme actuel : RIEN)")
            self.__theme_chosed_menu = OptionMenu(
                self.__plateau_player_config,
                self.__theme_chosed,
                "basic",
                "Pastel Sugar",
                "random, peut être instable"
            )
            self.__theme_chosed_menu.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
            
            btn_tester_plateau = Button(self.__plateau_player_config, text="Tester Plateau", command=self.tester_plateau)
            btn_tester_plateau.grid(row=8, column=0, columnspan=2, pady=(5, 15))        
            
            self.__btn_valider_plateau = Button(self.__plateau_player_config, text="Valider Plateau", command=self.new_game)
            self.__btn_valider_plateau.grid(row=9, column=0, columnspan=2, pady=(5, 15))
            
            self.__root.mainloop()
            
    def toggle_player_1_bot(self):
        """
        Met à jour l'état du joueur 1 (BOT ou joueur) et affiche/masque la liste de difficulté.
        """
        self.__player_1_is_bot = self.__is_j1_bot.get()
        if self.__player_1_is_bot:
            self.__player_or_bot_display_j1.config(text="Vous êtes actuellement un BOT")
            self.__j1_difficulty_menu.grid()  # Affiche la liste de difficulté
            self.__nom_chosed_j1_entry.grid_remove()# Cache le nom
            self.__nom_chosed_j1.set(self.__j1_difficulty.get()) 
        else:
            self.__player_or_bot_display_j1.config(text="Vous êtes actuellement un joueur")
            self.__j1_difficulty_menu.grid_remove()  # Cache la liste de difficulté
            self.__nom_chosed_j1_entry.grid() # Affiche le nom
          
    def toggle_player_2_bot(self):
        """
        Met à jour l'état du joueur 2 (BOT ou joueur) et affiche/masque la liste de difficulté.
        """
        self.__player_2_is_bot = self.__is_j2_bot.get()
        if self.__player_2_is_bot:
            self.__player_or_bot_display_j2.config(text="Vous êtes actuellement un BOT")
            self.__j2_difficulty_menu.grid()  # Affiche la liste de difficulté
            self.__nom_chosed_j2_entry.grid_remove()# Cache le nom
            self.__nom_chosed_j2.set(self.__j2_difficulty.get())
        else:
            self.__player_or_bot_display_j2.config(text="Vous êtes actuellement un joueur")
            self.__j2_difficulty_menu.grid_remove()  # Cache la liste de difficulté
            self.__nom_chosed_j2_entry.grid() # Affiche le nom
        self.__root.mainloop()
     
    def tester_plateau(self):
        if not(self.__player_1_is_bot and self.__player_2_is_bot):#pas de partie avec 2 bots(pas pertinant) 
            selected = self.__nb_cases_listbox.curselection()
            if selected:
                self.__curent_player = 1
                selected = int(self.__nb_cases_listbox.get(selected)[:2])
                #creation de la liste imbriquer pour stoquer les pions
                self.__liste_board = [[0 for _ in range(selected//2)] + [2 for _ in range(selected//2)] for _ in range(selected//2)] + [[1 for _ in range(selected//2)] + [0 for i in range(selected//2)] for _ in range(selected//2)]
                self.__liste_board[0][selected-1] = 4
                self.__liste_board[selected-1][0] = 3
                self.__joueur_1_info = Joueur(self.__nom_chosed_j1_entry.get(), 1, selected, self.__player_1_is_bot)
                self.__joueur_2_info = Joueur(self.__nom_chosed_j2_entry.get(), 2, selected, self.__player_2_is_bot)
                if not self.__nb_cases is None:#si il y avait un plateau avant il faut l'effacer
                    self.__plateau_frame.destroy()
                self.__plateau_frame = Frame(self.__root)
                self.__display_player = Label(self.__plateau_frame, text="")
                self.__display_player.grid(row=1, column=0)
                self.__plateau_frame.grid(row=0, column=1)
                self.__theme = Theme(self.__theme_chosed.get(), [self.__shape_j1_chosed.get(), self.__shape_j2_chosed.get()])
                self.__nb_cases = selected
                self.draw_board()
            else:
                messagebox.showerror(title="Erreur", message="Choisissez un taille de plateau")
        else:
            messagebox.showerror(title="Erreur", message="Au moins un joueur doit jouer")
        
    def pause_game(self, event):
        self.__plateau.destroy()
        self.__pause_menu = Frame(self.__root)
        self.__pause_menu.grid(row=0, column=1, pady=(5, 15))
        buttons = [
            ("Resume" , self.resume_game),
            ("Paramètres", self.settings_button),
            ("Recommencer partie" , self.new_match),
            ("Sauvegarder", self.save_game),
            ("Quitter sans sauvegarder", self.quit_game),
            ("Sauvegarder et quitter", self.save_and_quit_game),
        ]

        for i in range(len(buttons)):
            button = Button(self.__pause_menu, text=buttons[i][0], command=buttons[i][1])
            button.grid(row=i+1, column=0, pady=(5, 15))
    
    def resume_game(self):
        self.__pause_menu.destroy()
        self.__pause_menu = None
        self.draw_board()
    
    def settings_button(self):
        self.__pause_menu.destroy()
        self.__settings_menu = Frame(self.__root)
        self.__settings_menu.grid(row=0, column=1, pady=(5, 15))
        Label(self.__settings_menu, text="Settings").grid(row=0, column=0, columnspan=2,  padx=10, pady=5)

        Label(self.__settings_menu, text="Joueur 1").grid(row=1, column=0, padx=10, pady=5)
        Label(self.__settings_menu, text="Joueur 2").grid(row=1, column=1, padx=10, pady=5)

        #J1 Shape
        self.__shape_j1_chosed_menu = OptionMenu(
            self.__settings_menu,
            self.__shape_j1_chosed,
            "cercle",
            "losange",
            "rectangle",
            "random"
        )
        self.__shape_j1_chosed_menu.grid(row=2, column=0)
        #J2 shape
        self.__shape_j2_chosed_menu = OptionMenu(
            self.__settings_menu,
            self.__shape_j2_chosed,
            "cercle",
            "losange",
            "rectangle",
            "random"
        )
        self.__shape_j2_chosed_menu.grid(row=2, column=1)
        # theme
        Label(self.__settings_menu, text="Change colors").grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.__theme_chosed_menu = OptionMenu(
            self.__settings_menu,
            self.__theme_chosed,
            "basic",
            "Pastel Sugar",
            "random, peut être instable"
        )
        self.__theme_chosed_menu.grid(row=4, column=0, columnspan=2)
        button = Button(self.__settings_menu, text="apply changes", command=self.apply_changes)
        button.grid(row=5, column=0, columnspan=2, pady=(5, 15))
        button = Button(self.__settings_menu, text="go back", command=self.go_back_to_pause_menu)
        button.grid(row=6, column=0, columnspan=2, pady=(5, 15))

    def apply_changes(self):
        self.__theme = Theme(self.__theme_chosed.get(), [self.__shape_j1_chosed.get(), self.__shape_j2_chosed.get()])
         
    def go_back_to_pause_menu(self):
        self.__settings_menu.destroy()
        self.pause_game(None)
        
    def save_game(self):
        plateau = '\n'.join([''.join(map(str, row)) for row in self.__liste_board])
        content = str(self.__player_1_is_bot) +'\n' + str(self.__player_2_is_bot) + '\n' + self.__joueur_1_info.get_name()+ '\n' + self.__joueur_2_info.get_name()  +'\n' + self.__shape_j1_chosed.get() + '\n' + self.__shape_j2_chosed.get() + '\n' + str(self.__curent_player) + '\n' + self.__theme_chosed.get() + '\n' + plateau
        with open('Save.txt', 'w') as f:
            f.write(content)
        
    def see_load_game(self):
        with open('Save.txt', 'r') as f:
            content = f.read()
        content_list = content.split('\n')
        return len(content)>0 and messagebox.askyesno(title="Replay?", message="Do you want to reload the game?(" + content_list[2] + " VS " + content_list[3] +")")
                        
    def load_game(self):
        with open('Save.txt', 'r') as f:
            content = f.read()
        
        content_list = content.split('\n')
        self.__theme = Theme(content_list[7], [content_list[4], content_list[5]])
        self.__curent_player = int(content_list[6])
        self.__nb_cases = len(content_list[-1])
        self.__liste_board = [list(map(int, row)) for row in content_list[-self.__nb_cases:]]
        self.__root = Tk()
        self.__root.title("Jeu de plateau")
        self.__PXCASE = 50 
        self.__case_selected = None
        self.__player_1_is_bot = content_list[0] == 'True'
        self.__player_2_is_bot = content_list[1] == 'True'
        self.__joueur_1_info = Joueur(content_list[2], 1, self.__nb_cases, self.__player_1_is_bot)
        self.__joueur_2_info = Joueur(content_list[3], 2, self.__nb_cases, self.__player_2_is_bot)
        self.__j1_difficulty = StringVar(value=content_list[2])
        self.__j2_difficulty = StringVar(value=content_list[3])
        self.__theme_chosed = content_list[7]
        self.__shape_j1_chosed = StringVar(value=content_list[4])
        self.__shape_j2_chosed = StringVar(value=content_list[5])
        self.__plateau_frame = Frame(self.__root)
        self.__display_player = Label(self.__plateau_frame, text="")
        self.__plateau_frame = Frame(self.__root)
        self.__display_player = Label(self.__plateau_frame, text="")
        self.__display_player.grid(row=1, column=0)
        self.__plateau_frame.grid(row=0, column=1)
        self.end_game_turn()
    
    def new_match(self):
        if messagebox.askyesno(title="Replay?", message="Do you want to restart the game?"):
            self.resume_game()
            self.new_game()
         
    def save_and_quit_game(self):
        self.save_game()
        self.quit_game()
        
    def quit_game(self):
        if messagebox.askyesno(title="Replay?", message="Do you want to quit the game?"):
            self.__root.destroy()
    
    def new_game(self):
        if self.__nb_cases:
            if self.__plateau_player_config.winfo_exists():
                self.__plateau_player_config.destroy()
            self.__joueur_1_info = Joueur(self.__joueur_1_info.get_name(), 1, self.__nb_cases, self.__player_1_is_bot)
            self.__joueur_2_info = Joueur(self.__joueur_2_info.get_name(), 2, self.__nb_cases, self.__player_1_is_bot)
            self.__liste_board = [[0 for _ in range(self.__nb_cases//2)] + [2 for _ in range(self.__nb_cases//2)] for _ in range(self.__nb_cases//2)] + [[1 for _ in range(self.__nb_cases//2)] + [0 for i in range(self.__nb_cases//2)] for _ in range(self.__nb_cases//2)]
            self.__liste_board[0][self.__nb_cases-1] = 4
            self.__liste_board[self.__nb_cases-1][0] = 3
            self.__case_selected = None
            self.__curent_player = 1
            self.end_game_turn()
        else:
            messagebox.showerror(title="Erreur", message="Testez le plateau avant")
     
    def player_game_turn(self, event):
        """Handle a player's turn."""
        indice =  event.y // self.__PXCASE, event.x // self.__PXCASE
        if self.__case_selected is None and self.possible(indice):
            self.__case_selected = indice
            self.draw_possible()
        
        elif self.possible(indice):
            self.put(indice)
            self.end_game_turn()
               
    def draw_possible(self):
        """ ajoute des bébés cercle gris de toutes les cases possible"""
        if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]]%2 == self.__curent_player%2:
            selected = [self.__case_selected[0], self.__case_selected[1]]
            marge = 15
            while selected[0]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]] == 0:
                selected[0] += 1
                x0, y0 = selected[1] * self.__PXCASE, selected[0] * self.__PXCASE
                x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE
                self.__plateau.create_oval(x0+marge, y0+marge, x1-marge, y1-marge, fill='#555555', outline='#555555')
            selected = [self.__case_selected[0], self.__case_selected[1]]
            while selected[0]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]] == 0:
                selected[0] -= 1
                x0, y0 = selected[1] * self.__PXCASE, selected[0] * self.__PXCASE
                x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE               
                self.__plateau.create_oval(x0+marge, y0+marge, x1-marge, y1-marge, fill='#555555', outline='#555555')
            selected = [self.__case_selected[0], self.__case_selected[1]]
            while selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]][selected[1]+1] == 0:
                selected[1] += 1
                x0, y0 = selected[1] * self.__PXCASE, selected[0] * self.__PXCASE
                x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE               
                self.__plateau.create_oval(x0+marge, y0+marge, x1-marge, y1-marge, fill='#555555', outline='#555555')
            selected = [self.__case_selected[0], self.__case_selected[1]]
            while selected[1]-1 >= 0 and self.__liste_board[selected[0]][selected[1]-1] == 0:
                selected[1] -= 1
                x0, y0 = selected[1] * self.__PXCASE, selected[0] * self.__PXCASE
                x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE                
                self.__plateau.create_oval(x0+marge, y0+marge, x1-marge, y1-marge, fill='#555555', outline='#555555')
            
            if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]]>2:
                selected = [self.__case_selected[0], self.__case_selected[1]]
                while selected[0]+1 < self.__nb_cases and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]+1] == 0:
                    selected[0] += 1
                    selected[1] += 1
                    x0, y0 = selected[1] * self.__PXCASE, selected[0] * self.__PXCASE
                    x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE                
                    self.__plateau.create_oval(x0+marge, y0+marge, x1-marge, y1-marge, fill='#555555', outline='#555555')
                selected = [self.__case_selected[0], self.__case_selected[1]]
                while selected[0]+1 < self.__nb_cases and selected[1]-1 >= 0 and self.__liste_board[selected[0]+1][selected[1]-1] == 0:
                    selected[0] += 1
                    selected[1] -= 1
                    x0, y0 = selected[1] * self.__PXCASE, selected[0] * self.__PXCASE
                    x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE                
                    self.__plateau.create_oval(x0+marge, y0+marge, x1-marge, y1-marge, fill='#555555', outline='#555555')
                selected = [self.__case_selected[0], self.__case_selected[1]]
                while selected[0]-1 >= 0 and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]-1][selected[1]+1] == 0:
                    selected[0] -= 1
                    selected[1] += 1
                    x0, y0 = selected[1] * self.__PXCASE, selected[0] * self.__PXCASE
                    x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE                
                    self.__plateau.create_oval(x0+marge, y0+marge, x1-marge, y1-marge, fill='#555555', outline='#555555')
                selected = [self.__case_selected[0], self.__case_selected[1]]
                while selected[0]-1 >= 0 and selected[1]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]-1] == 0:
                    selected[0] -= 1
                    selected[1] -= 1
                    x0, y0 = selected[1] * self.__PXCASE, selected[0] * self.__PXCASE
                    x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE                
                    self.__plateau.create_oval(x0+marge, y0+marge, x1-marge, y1-marge, fill='#555555', outline='#555555')
            x0, y0 = self.__case_selected[1] * self.__PXCASE, self.__case_selected[0] * self.__PXCASE
            x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE
            if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]]>2:
                self.__theme.create_shape(self.__curent_player-1)(x0, y0,self.__theme.get_colors()[5][self.__curent_player-1] ,self.__plateau)
            else:
                self.__theme.create_shape(self.__curent_player-1)(x0, y0,self.__theme.get_colors()[3][self.__curent_player-1] ,self.__plateau)
                 
    def put(self, indice):
        #indice est l'indice ddu nouveau pion
        if (indice[0], indice[1]) != (self.__case_selected[0], self.__case_selected[1]): # si la case n'a pas été reselectionner
            if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] > 2: # si c'est une reine
                self.__liste_board[indice[0]][indice[1]] = self.__curent_player + 2
                self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] = 0
                
                if self.__curent_player == 1:
                    self.__curent_player = 2
                    self.__joueur_1_info.set_queen_pos((indice[0], indice[1]))
                else:
                    self.__curent_player = 1
                    self.__joueur_2_info.set_queen_pos((indice[0], indice[1]))
                
            else:
                self.__liste_board[indice[0]][indice[1]] = self.__curent_player
                self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] = 0
                if self.__curent_player == 1:
                    if not(self.__joueur_1_info.get_queen_pos()[0] == indice[0] or self.__joueur_1_info.get_queen_pos()[1] == indice[1]):
                        if self.__liste_board[indice[0]][self.__joueur_1_info.get_queen_pos()[1]] == 2:#si la case menacer est une case enemie on la capture
                            self.__liste_board[indice[0]][self.__joueur_1_info.get_queen_pos()[1]] = 0
                            self.__joueur_2_info.one_pions_down()
                        if self.__liste_board[self.__joueur_1_info.get_queen_pos()[0]][indice[1]] == 2:#si la case menacer est une case enemie on la capture
                            self.__liste_board[self.__joueur_1_info.get_queen_pos()[0]][indice[1]] = 0
                            self.__joueur_2_info.one_pions_down()
                    self.__curent_player = 2
                else:
                    if not(self.__joueur_2_info.get_queen_pos()[0] == indice[0] or self.__joueur_2_info.get_queen_pos()[1] == indice[1]):
                        if self.__liste_board[indice[0]][self.__joueur_2_info.get_queen_pos()[1]] == 1:#si la case menacer est une case enemie on la capture
                            self.__liste_board[indice[0]][self.__joueur_2_info.get_queen_pos()[1]] = 0
                            self.__joueur_1_info.one_pions_down()
                        if self.__liste_board[self.__joueur_2_info.get_queen_pos()[0]][indice[1]] == 1:#si la case menacer est une case enemie on la capture
                            self.__liste_board[self.__joueur_2_info.get_queen_pos()[0]][indice[1]] = 0
                            self.__joueur_1_info.one_pions_down()
                    self.__curent_player = 1
        else:
            x0, y0 = indice[1] * self.__PXCASE, indice[0] * self.__PXCASE
            x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE
            if self.__liste_board[indice[0]][indice[1]] > 2:
                self.__plateau.create_oval(x0+5, y0+5, x1-5, y1-5, fill=self.__theme.get_colors()[4][self.__curent_player-1], outline=self.__theme.get_colors()[4][self.__curent_player-1])
            else:
                self.__plateau.create_oval(x0+5, y0+5, x1-5, y1-5, fill=self.__theme.get_colors()[2][self.__curent_player-1], outline=self.__theme.get_colors()[2][self.__curent_player-1])
        self.__case_selected = None
    
    def possible(self, indice): 
        if self.__case_selected is None:
            if self.__liste_board[indice[0]][indice[1]]%2 == self.__curent_player%2 and self.__liste_board[indice[0]][indice[1]]>0:
                if indice[0]+1 < self.__nb_cases and self.__liste_board[indice[0]+1][indice[1]] == 0:
                    return True
                if indice[0]-1 >= 0 and self.__liste_board[indice[0]-1][indice[1]] == 0:
                    return True
                if indice[1]+1 < self.__nb_cases and self.__liste_board[indice[0]][indice[1]+1] == 0:
                    return True
                if indice[1]-1 >= 0 and self.__liste_board[indice[0]][indice[1]-1] == 0:
                    return True
                if self.__liste_board[indice[0]][indice[1]] > 2:
                    if indice[0]+1 < self.__nb_cases and indice[1]+1 < self.__nb_cases and self.__liste_board[indice[0]+1][indice[1]+1] == 0:
                        return True
                    if indice[0]+1 < self.__nb_cases and indice[1]-1 >= 0 and self.__liste_board[indice[0]+1][indice[1]-1] == 0:
                        return True
                    if indice[0]-1 >= 0 and indice[1]+1 < self.__nb_cases and self.__liste_board[indice[0]-1][indice[1]+1] == 0:
                        return True
                    if indice[0]-1 >= 0 and indice[1]-1 >= 0 and self.__liste_board[indice[0]-1][indice[1]-1] == 0:
                        return True 
            return False
        else:
            if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]]%2 == self.__curent_player%2:
                selected = [self.__case_selected[0], self.__case_selected[1]]
                possible_cords = [[self.__case_selected[0], self.__case_selected[1]]]
                while selected[0]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]] == 0:
                    selected[0] += 1
                    possible_cords+= [[selected[0], selected[1]]]
                selected = [self.__case_selected[0], self.__case_selected[1]]
                while selected[0]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]] == 0:
                    selected[0] -= 1
                    possible_cords+= [[selected[0], selected[1]]]
                selected = [self.__case_selected[0], self.__case_selected[1]]
                while selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]][selected[1]+1] == 0:
                    selected[1] += 1
                    possible_cords+= [[selected[0], selected[1]]]
                selected = [self.__case_selected[0], self.__case_selected[1]]
                while selected[1]-1 >= 0 and self.__liste_board[selected[0]][selected[1]-1] == 0:
                    selected[1] -= 1
                    possible_cords+= [[selected[0], selected[1]]]
                if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] > 2:
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[0]+1 < self.__nb_cases and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]+1] == 0:
                        selected[0] += 1
                        selected[1] += 1
                        possible_cords+= [[selected[0], selected[1]]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[0]+1 < self.__nb_cases and selected[1]-1 >= 0 and self.__liste_board[selected[0]+1][selected[1]-1] == 0:
                        selected[0] += 1
                        selected[1] -= 1
                        possible_cords+= [[selected[0], selected[1]]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[0]-1 >= 0 and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]-1][selected[1]+1] == 0:
                        selected[0] -= 1
                        selected[1] += 1
                        possible_cords+= [[selected[0], selected[1]]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[0]-1 >= 0 and selected[1]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]-1] == 0:
                        selected[0] -= 1
                        selected[1] -= 1
                        possible_cords+= [[selected[0], selected[1]]]
            return [indice[0], indice[1]] in possible_cords
    
    def again(self, joueur):
        if joueur.get_nb_pions() > 2:
            for i in range(self.__nb_cases):
                for j in range(self.__nb_cases):
                    if self.__liste_board[i][j] > 0:
                        if self.possible((i, j)):
                            return True
        return False
        
    def draw_board(self):
        self.__plateau = Canvas(self.__plateau_frame, width=self.__PXCASE*self.__nb_cases , height=self.__PXCASE*self.__nb_cases)
        self.__plateau.grid(row=0, column=0)
        for i in range(self.__nb_cases):
            for j in range(self.__nb_cases):
                x0, y0 = j * self.__PXCASE, i * self.__PXCASE
                x1, y1 = x0 + self.__PXCASE, y0 + self.__PXCASE
                self.__plateau.create_rectangle(x0, y0, x1, y1, fill=self.__theme.get_colors()[0], outline=self.__theme.get_colors()[1])
                if self.__liste_board[i][j]>0:
                    player = self.__liste_board[i][j]-1
                    if self.__liste_board[i][j] >2:
                        player -= 2 # car c'est une reine
                        self.__theme.create_shape(player)(x0, y0,self.__theme.get_colors()[4][player] ,self.__plateau)
                    else:
                        self.__theme.create_shape(player)(x0, y0,self.__theme.get_colors()[2][player] ,self.__plateau)
        joueur = self.__joueur_1_info.get_name() if self.__curent_player == 1 else self.__joueur_2_info.get_name()
        self.__display_player.config(text=joueur, fg=self.__theme.get_colors()[2][self.__curent_player-1], bg=self.__theme.get_colors()[0], font=("Arial", 20))
        self.__plateau.bind("<Button-1>", self.player_game_turn)
        self.__plateau.bind("<Button-3>", self.pause_game)

    def end_game_turn(self):
        self.draw_board()
        joueur = self.__joueur_1_info if self.__curent_player == 1 else self.__joueur_2_info
        enememie = self.__joueur_2_info if self.__curent_player == 1 else self.__joueur_2_info
        if not(self.again(joueur)):
            messagebox.showinfo(title="Game Over", message=enememie.get_name() + " wins!")
            if messagebox.askyesno(title="Replay?", message="Do you want to play again?"):
                self.new_game()
            else:
                self.__root.destroy()
        elif [self.__player_1_is_bot, self.__player_2_is_bot][self.__curent_player-1]:
            self.__plateau_frame.after(1, self.bot_play())
            
            
    def bot_play(self):
        difficulte_played = [self.__joueur_1_info.get_name(), self.__joueur_2_info.get_name()][self.__curent_player-1]
        if difficulte_played == "Bot facile":
            self.bot_play_facile()
        elif difficulte_played == "Bot difficile niveau 1":
            self.bot_play_difficile1()
        elif difficulte_played == "Bot difficile niveau 2":
            self.bot_play_difficile2()
        elif difficulte_played == "Bot impossible":
            self.bot_play_god_moves()
        else:
            raise ValueError("difficultée choisie ("+difficulte_played+") pas implémntée")
        self.end_game_turn()

    def bot_play_facile(self):
        """Joue les coup aléatoirement"""
        case_pion_slectionable = []
        for i in range(self.__nb_cases):
            for j in range(self.__nb_cases):
                if self.__liste_board[i][j] > 0 and self.possible((i, j)):
                    case_pion_slectionable.append((i, j))
        
        indice_case_choisi = randint(0, len(case_pion_slectionable)-1)
        self.__case_selected = case_pion_slectionable[indice_case_choisi]
        #selection de la case cible
        i, j = self.__case_selected[0] , self.__case_selected[1]
        selected = [i, j]
        possible_cords = []
        while selected[0]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]] == 0:
            selected[0] += 1
            possible_cords+= [[selected[0], selected[1]]]
        selected = [i, j]
        while selected[0]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]] == 0:
            selected[0] -= 1
            possible_cords+= [[selected[0], selected[1]]]
        selected = [i, j]
        while selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]][selected[1]+1] == 0:
            selected[1] += 1
            possible_cords+= [[selected[0], selected[1]]]
        selected = [i, j]
        while selected[1]-1 >= 0 and self.__liste_board[selected[0]][selected[1]-1] == 0:
            selected[1] -= 1
            possible_cords+= [[selected[0], selected[1]]]
        if self.__liste_board[i][j] > 2:
            selected = [i, j]
            while selected[0]+1 < self.__nb_cases and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]+1] == 0:
                selected[0] += 1
                selected[1] += 1
                possible_cords+= [[selected[0], selected[1]]]
            selected = [i, j]
            while selected[0]+1 < self.__nb_cases and selected[1]-1 >= 0 and self.__liste_board[selected[0]+1][selected[1]-1] == 0:
                selected[0] += 1
                selected[1] -= 1
                possible_cords+= [[selected[0], selected[1]]]
            selected = [i, j]
            while selected[0]-1 >= 0 and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]-1][selected[1]+1] == 0:
                selected[0] -= 1
                selected[1] += 1
                possible_cords+= [[selected[0], selected[1]]]
            selected = [i, j]
            while selected[0]-1 >= 0 and selected[1]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]-1] == 0:
                selected[0] -= 1
                selected[1] -= 1
                possible_cords+= [[selected[0], selected[1]]]
        
        indice_case_choisi = randint(0, len(possible_cords)-1)
        coup_choisi = possible_cords[indice_case_choisi]
        self.put((coup_choisi))
            
    def bot_play_difficile1(self):
        """Joue les coup en priorité si une ou plusieur prise est possible tout en favorisant le plus possible, sinon joue aléatoirement"""
        posqueen = self.__joueur_1_info.get_queen_pos() if self.__curent_player == 1 else self.__joueur_2_info.get_queen_pos()
        case_pion_slectionable_avec_indice_possible = []
        coup_avec_prise = []
        coup_avec_deux_prises = []
        for i in range(self.__nb_cases):
            for j in range(self.__nb_cases):
                if self.possible((i, j)):
                    self.__case_selected = i, j
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[0]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]] == 0:
                        selected[0] += 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                        tableau_selected += [[i, j, selected[0], selected[1]]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[0]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]] == 0:
                        selected[0] -= 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                        tableau_selected += [[i, j, selected[0], selected[1]]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]][selected[1]+1] == 0:
                        selected[1] += 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                        tableau_selected += [[i, j, selected[0], selected[1]]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[1]-1 >= 0 and self.__liste_board[selected[0]][selected[1]-1] == 0:
                        selected[1] -= 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                        tableau_selected += [[i, j, selected[0], selected[1]]]
                    if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] > 2:
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]+1 < self.__nb_cases and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]+1] == 0:
                            selected[0] += 1
                            selected[1] += 1
                            case_pion_slectionable_avec_indice_possible += [[i, j, selected[0], selected[1]]]
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]+1 < self.__nb_cases and selected[1]-1 >= 0 and self.__liste_board[selected[0]+1][selected[1]-1] == 0:
                            selected[0] += 1
                            selected[1] -= 1
                            case_pion_slectionable_avec_indice_possible += [[i, j, selected[0], selected[1]]]
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]-1 >= 0 and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]-1][selected[1]+1] == 0:
                            selected[0] -= 1
                            selected[1] += 1
                            case_pion_slectionable_avec_indice_possible += [[i, j, selected[0], selected[1]]]
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]-1 >= 0 and selected[1]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]-1] == 0:
                            selected[0] -= 1
                            selected[1] -= 1
                            case_pion_slectionable_avec_indice_possible += [[i, j, selected[0], selected[1]]]
                    self.__case_selected = None
                
        if coup_avec_deux_prises:#execute si il y a un coup possible
            coup = choice(coup_avec_deux_prises)
        elif coup_avec_prise:#execute si il y a un coup possible
            coup = choice(coup_avec_prise)
        elif case_pion_slectionable_avec_indice_possible:#execute si il y a un coup possible
            coup = choice(case_pion_slectionable_avec_indice_possible)
        self.__case_selected = coup[0], coup[1]
        self.put((coup[2], coup[3]))
        
    def bot_play_difficile2(self):
        """Joue les coup en priorité si une prise est possible en évitant de se mettre en danger (sur la meme ligen et colone de la reine adverse), sinon joue aléatoirement en éviant le danger au maximum"""
        posqueen = self.__joueur_1_info.get_queen_pos() if self.__curent_player == 1 else self.__joueur_2_info.get_queen_pos()
        posqueen_enemi = self.__joueur_2_info.get_queen_pos() if self.__curent_player == 1 else self.__joueur_1_info.get_queen_pos()
        case_pion_slectionable_avec_indice_possible = []
        coup_avec_prise = []
        coup_avec_deux_prises = []
        for i in range(self.__nb_cases):
            for j in range(self.__nb_cases):
                if self.possible((i, j)):
                    self.__case_selected = i, j
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[0]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]] == 0:
                        selected[0] += 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                        dangerous_placement = posqueen_enemi[0] == selected[0] or posqueen_enemi[1] == selected[1]
                        tableau_selected += [[i, j, selected[0], selected[1], dangerous_placement]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[0]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]] == 0:
                        selected[0] -= 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                        dangerous_placement = posqueen_enemi[0] == selected[0] or posqueen_enemi[1] == selected[1]
                        tableau_selected += [[i, j, selected[0], selected[1], dangerous_placement]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]][selected[1]+1] == 0:
                        selected[1] += 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                        dangerous_placement = posqueen_enemi[0] == selected[0] or posqueen_enemi[1] == selected[1]
                        tableau_selected += [[i, j, selected[0], selected[1], dangerous_placement]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[1]-1 >= 0 and self.__liste_board[selected[0]][selected[1]-1] == 0:
                        selected[1] -= 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                        dangerous_placement = posqueen_enemi[0] == selected[0] or posqueen_enemi[1] == selected[1]
                        tableau_selected += [[i, j, selected[0], selected[1], dangerous_placement]]
                    if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] > 2:
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]+1 < self.__nb_cases and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]+1] == 0:
                            selected[0] += 1
                            selected[1] += 1
                            case_pion_slectionable_avec_indice_possible += [[i, j, selected[0], selected[1], False]]
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]+1 < self.__nb_cases and selected[1]-1 >= 0 and self.__liste_board[selected[0]+1][selected[1]-1] == 0:
                            selected[0] += 1
                            selected[1] -= 1
                            case_pion_slectionable_avec_indice_possible += [[i, j, selected[0], selected[1], False]]
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]-1 >= 0 and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]-1][selected[1]+1] == 0:
                            selected[0] -= 1
                            selected[1] += 1
                            case_pion_slectionable_avec_indice_possible += [[i, j, selected[0], selected[1], False]]
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]-1 >= 0 and selected[1]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]-1] == 0:
                            selected[0] -= 1
                            selected[1] -= 1
                            case_pion_slectionable_avec_indice_possible += [[i, j, selected[0], selected[1], False]]
                    self.__case_selected = None
                
        coup = None      
        if coup_avec_deux_prises:#execute si il y a un coup possible
            # coup[4] dit si oui ou non elle est une case dangeureuse
            for coup_actuelle in coup_avec_deux_prises:
                if not coup_actuelle[4]:
                    coup = coup_actuelle
            if coup is None:
                coup = choice(coup_avec_deux_prises)
        elif coup_avec_prise:#execute si il y a un coup possible
            for coup_actuelle in coup_avec_prise:
                if not coup_actuelle[4]:
                    coup = coup_actuelle
            if coup is None:
                coup = choice(coup_avec_prise)
        elif case_pion_slectionable_avec_indice_possible:#execute si il y a un coup possible
            for coup_actuelle in case_pion_slectionable_avec_indice_possible:
                if not coup_actuelle[4]:
                    coup = coup_actuelle
            if coup is None:
                coup = choice(case_pion_slectionable_avec_indice_possible)
        self.__case_selected = coup[0], coup[1]
        self.put((coup[2], coup[3]))

    def nombre_ennemi_en_danger(self, posqueen):
        nb_ennemi_en_danger = 0
        selected = [posqueen[0], posqueen[1]]
        while selected[0]+1 < self.__nb_cases:
            selected[0] += 1
            if self.__liste_board[selected[0]][selected[1]] == 3-self.__curent_player:
                nb_ennemi_en_danger += 1
        selected = [posqueen[0], posqueen[1]]
        while selected[0]-1 >= 0:
            selected[0] -= 1
            if self.__liste_board[selected[0]][selected[1]] == 3-self.__curent_player:
                nb_ennemi_en_danger += 1
        selected = [posqueen[0], posqueen[1]]
        while selected[1]+1 < self.__nb_cases:
            selected[1] += 1
            if self.__liste_board[selected[0]][selected[1]] == 3-self.__curent_player:
                nb_ennemi_en_danger += 1
        selected = [posqueen[0], posqueen[1]]
        while selected[1]-1 >= 0:
            selected[1] -= 1
            if self.__liste_board[selected[0]][selected[1]] == 3-self.__curent_player:
                nb_ennemi_en_danger += 1
        return nb_ennemi_en_danger

    def bot_play_god_moves(self):
        """
        fonctionnemeent du bot : 
            si tour en danger, la sauver sinon
            si reine menace plus d'un pion/si on peut manger
                on essay de tuer un de ces pions
            si reine menace 0 pion
                on regarde pour changer de place pour menacer un pion
            si la rien n'est pas bougable/ ou aucun coup précédament dit n'est possible
                joue une toure aléatoires en evitant le danger
        """
        posqueen = self.__joueur_1_info.get_queen_pos() if self.__curent_player == 1 else self.__joueur_2_info.get_queen_pos()
        posqueen_enemi = self.__joueur_2_info.get_queen_pos() if self.__curent_player == 1 else self.__joueur_1_info.get_queen_pos()
        queen_moves = []
        case_pion_slectionable_avec_indice_possible_et_en_danger = []
        case_pion_slectionable_avec_indice_possible = []
        coup_avec_prise = []
        coup_avec_deux_prises = []
        nombre_ennemi_en_danger_acctuellement = self.nombre_ennemi_en_danger(posqueen)
        
        for i in range(self.__nb_cases):
            for j in range(self.__nb_cases):
                if self.possible((i, j)):
                    self.__case_selected = i, j
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[0]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]] == 0:
                        selected[0] += 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] > 2:
                            queen_moves  += [[i, j, selected[0], selected[1], False, self.nombre_ennemi_en_danger((selected[0], selected[1]))]]
                        else:
                            dangerous_placement = posqueen_enemi[0] == selected[0] or posqueen_enemi[1] == selected[1]
                            tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                            tableau_selected = case_pion_slectionable_avec_indice_possible_et_en_danger if posqueen_enemi[0] == self.__case_selected[0] or posqueen_enemi[1] == self.__case_selected[1] else tableau_selected
                            tableau_selected += [[i, j, selected[0], selected[1], dangerous_placement]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[0]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]] == 0:
                        selected[0] -= 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] > 2:
                            queen_moves  += [[i, j, selected[0], selected[1], False, self.nombre_ennemi_en_danger((selected[0], selected[1]))]]
                        else:
                            dangerous_placement = posqueen_enemi[0] == selected[0] or posqueen_enemi[1] == selected[1]
                            tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                            tableau_selected = case_pion_slectionable_avec_indice_possible_et_en_danger if posqueen_enemi[0] == self.__case_selected[0] or posqueen_enemi[1] == self.__case_selected[1] else tableau_selected
                            tableau_selected += [[i, j, selected[0], selected[1], dangerous_placement]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]][selected[1]+1] == 0:
                        selected[1] += 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] > 2:
                            queen_moves  += [[i, j, selected[0], selected[1], False, self.nombre_ennemi_en_danger((selected[0], selected[1]))]]
                        else:
                            dangerous_placement = posqueen_enemi[0] == selected[0] or posqueen_enemi[1] == selected[1]
                            tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                            tableau_selected = case_pion_slectionable_avec_indice_possible_et_en_danger if posqueen_enemi[0] == self.__case_selected[0] or posqueen_enemi[1] == self.__case_selected[1] else tableau_selected
                            tableau_selected += [[i, j, selected[0], selected[1], dangerous_placement]]
                    selected = [self.__case_selected[0], self.__case_selected[1]]
                    while selected[1]-1 >= 0 and self.__liste_board[selected[0]][selected[1]-1] == 0:
                        selected[1] -= 1
                        nb_kill = 0 #le nombre de capture possible grace à ce coup
                        if self.__liste_board[selected[0]][posqueen[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[posqueen[0]][selected[1]] == 3-self.__curent_player:
                            nb_kill+=1
                        if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] > 2:
                            queen_moves  += [[i, j, selected[0], selected[1], False, self.nombre_ennemi_en_danger((selected[0], selected[1]))]]
                        else:
                            dangerous_placement = posqueen_enemi[0] == selected[0] or posqueen_enemi[1] == selected[1]
                            tableau_selected = [case_pion_slectionable_avec_indice_possible, coup_avec_prise, coup_avec_deux_prises][nb_kill]#comme ça le tableau select modifira le bon tableau car cela "copie" l'emplacement mémoire 
                            tableau_selected = case_pion_slectionable_avec_indice_possible_et_en_danger if posqueen_enemi[0] == self.__case_selected[0] or posqueen_enemi[1] == self.__case_selected[1] else tableau_selected
                            tableau_selected += [[i, j, selected[0], selected[1], dangerous_placement]]
                    if self.__liste_board[self.__case_selected[0]][self.__case_selected[1]] > 2:
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]+1 < self.__nb_cases and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]+1][selected[1]+1] == 0:
                            selected[0] += 1
                            selected[1] += 1
                            queen_moves  += [[i, j, selected[0], selected[1], False, self.nombre_ennemi_en_danger((selected[0], selected[1]))]]
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]+1 < self.__nb_cases and selected[1]-1 >= 0 and self.__liste_board[selected[0]+1][selected[1]-1] == 0:
                            selected[0] += 1
                            selected[1] -= 1
                            queen_moves  += [[i, j, selected[0], selected[1], False, self.nombre_ennemi_en_danger((selected[0], selected[1]))]]
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]-1 >= 0 and selected[1]+1 < self.__nb_cases and self.__liste_board[selected[0]-1][selected[1]+1] == 0:
                            selected[0] -= 1
                            selected[1] += 1
                            queen_moves  += [[i, j, selected[0], selected[1], False, self.nombre_ennemi_en_danger((selected[0], selected[1]))]]
                        selected = [self.__case_selected[0], self.__case_selected[1]]
                        while selected[0]-1 >= 0 and selected[1]-1 >= 0 and self.__liste_board[selected[0]-1][selected[1]-1] == 0:
                            selected[0] -= 1
                            selected[1] -= 1
                            queen_moves  += [[i, j, selected[0], selected[1], False, self.nombre_ennemi_en_danger((selected[0], selected[1]))]]
                    self.__case_selected = None
        #trie de la liste queen_moves en fonction du nombre de nombre d'ennemi en danger, triée selon le principe du tri par sélection.
        if queen_moves:
        
            n = len(queen_moves)
            for i in range(n):
                indice = i
                for j in range(i+1, n):
                    if queen_moves[j][5] < queen_moves[indice][5]:
                        indice = j
                queen_moves[i], queen_moves[indice] = queen_moves[indice], queen_moves[i]
        coup = None 
        if coup_avec_deux_prises:#execute si il y a un coup possible
            coup_pos = []
            # coup[4] dit si oui ou non elle est une case dangeureuse
            for coup_actuelle in coup_avec_deux_prises:
                if not coup_actuelle[4]:
                    coup_pos += [coup_actuelle]
            if coup_pos:
                coup = choice(coup_pos)
            else:
                coup = choice(coup_avec_deux_prises)     
        elif case_pion_slectionable_avec_indice_possible_et_en_danger:
            for coup_actuelle in case_pion_slectionable_avec_indice_possible_et_en_danger:
                if not coup_actuelle[4]:
                    coup = coup_actuelle
        elif coup_avec_prise:
            coup_pos = []
            for coup_actuelle in coup_avec_prise:
                if not coup_actuelle[4]:
                    coup_pos += [coup_actuelle]
            if coup_pos:
                coup = choice(coup_pos)
            else:
                coup = choice(coup_avec_prise)
        
        if queen_moves and coup is None:
            coup_pos = []
            for coup_actuelle in queen_moves:
                if coup_actuelle[5] > nombre_ennemi_en_danger_acctuellement: #pour la reine ce n'est pas si elle est en danger car elle est imprenable c'est plutot le nombre de victimes
                    coup = coup_actuelle # vu que la liste est triée on prennd juste le dernier possible
        if case_pion_slectionable_avec_indice_possible and coup is None:
            coup_pos = []
            for coup_actuelle in case_pion_slectionable_avec_indice_possible:
                if not coup_actuelle[4]:
                    coup_pos += [coup_actuelle]
            if coup_pos:
                coup = choice(coup_pos)
            else:
                coup = choice(case_pion_slectionable_avec_indice_possible)
        
        if coup is None:
            coup = choice(queen_moves)
        self.__case_selected = coup[0], coup[1]
        self.put((coup[2], coup[3]))

game = Jeu()
