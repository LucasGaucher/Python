""""
Auteur: GAUCHER L.
creation: 01/10/2024 16:36
Toads and Frogs 
"""
from jour4 import display
from random import randint

def initBoard(n: int, p: int):
    """
    Crée une nouvelle grille de jeu de Toads and Frogs avec n cases et p le nombre de pions pour chaque joueur.
    """
    #return [2 if (i >= (n - p)) else 1 if (i < p) else 0 for i in range(n)] if (p := min(p, n // 2 - 1)) >= 0 else [0] * n #python 3.8 ou après 
    if p >= n/2:
        p = int(n/2-1)
        print('redefinition du nombre de pions à :', p)
    tab = [0]*n
    for i in range(p):
        tab[i] = 1
        tab[-(i+1)] = 2
    return tab
    

def possible(board: list, n:int, i:int, player:int):
    """
    Vérifie si la case i est jouable pour le joueur player.
    """
    return [i > 0, i<n - 1][player-1] and board[i] == player and (board[i + [1,-1][player-1]] == 0 or ([i < n-2, i>1][player-1] and board[i + [1,-1][player-1]] == 1 and board[i + [1,-1][player-1]*2] == 0))

def select(board: list, n:int, player:int):
    """
    fait saisir au joueur player la coordonnée d'un pion qu'il peut déplacer
    """
    pion = int(input('Veuillez choisir un pion joueur n°'+ str(player) + ':'))
    while not (0 <= pion < n and board[pion] == player):
        if 0<= pion <= n:
            print('Ce pion ne vous appartiens pas')
        else:
            print('Ce pion ne appartiens pas au plateau')
        pion = int(input('Veuillez choisie un autre pion joueur n°'+ str(player) + ':'))
    return pion

def move(board: list, n: int, player: int, i: int):
    """
    Cette procédure réalise un déplacement dont i est la coordonnée d'un pion que le joueur player peut déplace
    """
    if player == 1:
        if board[i + 1] == 0:
            board[i], board[i + 1] = 0, player
        else: 
            board[i], board[i + 2] = 0, player
    elif player == 2:
        if board[i - 1] == 0:
            board[i], board[i - 1] = 0, player
        else:
            board[i], board[i - 2] = 0, player


def again(board: list, n: int, player: int):
    """
    Vérifie si le joueur `player` peut encore bouger un pion.
    Retourne True si un déplacement est possible, sinon False.
    """
    return any(board[i] == player and ((i+1 < n and board[i+1] == 0) or (i+2 < n and board[i+1] == 2 and board[i+2] == 0)) for i in range(n-1)) if player == 1 else any(board[i] == player and ((i-1 >= 0 and board[i-1] == 0) or (i-2 >= 0 and board[i-1] == 1 and board[i-2] == 0)) for i in range(n-1, 0, -1))

#     if player == 1: 
#         for i in range(n - 1):
#             if board[i] == player and (
#                     (i + 1 < n and board[i + 1] == 0) or  
#                     (i + 2 < n and board[i + 1] == 2 and board[i + 2] == 0)
#             ):
#                 return True
#     elif player == 2: 
#         for i in range(n - 1, 0, -1):
#             if board[i] == player and (
#                     (i - 1 >= 0 and board[i - 1] == 0) or
#                     (i - 2 >= 0 and board[i - 1] == 1 and board[i - 2] == 0)
#             ):
#                 return True
#     return False 

def toadsAndFrogsPvP(n:int, p:int):
    """
    joue au jeu de toads and Frogs avec 2 joueur
    """
    board = initBoard(n, p)
    joueur = 1
    while again(board, n, joueur):
        display(board, n)
        print("C'est au tour du joueur", joueur)
        i = select(board, n, joueur)
        move(board, n, joueur, i)
        
        joueur = 2 if joueur == 1 else 1
    return joueur -1

def possible_move(board:list, n:int, player:int):
    """
    revoie tout les mouvements possible
    """
    pos_mv = []
    
    if player == 1: 
        for i in range(n - 1):
            if board[i] == player and (
                    (i + 1 < n and board[i + 1] == 0) or  
                    (i + 2 < n and board[i + 1] == 2 and board[i + 2] == 0)
            ):
                pos_mv += [i]
    elif player == 2: 
        for i in range(n - 1, 0, -1):
            if board[i] == player and (
                    (i - 1 >= 0 and board[i - 1] == 0) or
                    (i - 2 >= 0 and board[i - 1] == 1 and board[i - 2] == 0)
            ):
                pos_mv += [i]
    return pos_mv
            
        

def toadsAndFrogsPvE(n:int, p:int):
    """
    joue au jeu de toads and Frogs avec 2 joueur
    """
    board = initBoard(n, p)
    joueur = 1
    while again(board, n, joueur):
        display(board, n)
        print("C'est au tour du", ["joueur","bot"][joueur-1])
        if joueur == 1:
            i = select(board, n, joueur)
            
            while not possible(board, n, i, joueur):
                i = select(board, n)
        else:
            pos_moves = possible_move(board, n, joueur)
            i = pos_moves[randint(0,len(pos_moves))]
        move(board, n, joueur, i)
        
        joueur = 2 if joueur == 1 else 1
    return joueur-1


def toadsAndFrogsEvE(n:int, p:int):
    """
    joue au jeu de toads and Frogs avec 2 joueur
    """
    board = initBoard(n, p)
    joueur = 1
    while again(board, n, joueur):
        display(board, n)
        print("C'est au tour du bot n°", joueur)
        pos_moves = possible_move(board, n, joueur)
        i = pos_moves[randint(0,len(pos_moves)-1)]
        move(board, n, joueur, i)
        
        joueur = 2 if joueur == 1 else 1
    return joueur-1

if __name__ == "__main__" and False:# in normal case
    jouer = True
    win_rate = [0,0]
    while jouer:
        print("Bienvenue au jeu Toads and Frogs ")
        n = int(input("le nombre de cases : "))
        p = int(input("le nombre de pions : "))
        game = [toadsAndFrogsPvP, toadsAndFrogsPvE , toadsAndFrogsEvE][int(input("le nombre de mode de jeu (0: sans bot, 1: un bot et un joueur, 2: 2 bots) : "))]
        gagnant = game(n,p)
        print(['Toads', 'Frogs'][gagnant] + ' WIN !!!!!!!!!!!!')
        win_rate[gagnant] = win_rate[gagnant] + 1
        demand_rejoue = input("Voulez-vous rejouer?(oui ou non)")
        while not demand_rejoue in ['oui','non']:
            print(demand_rejoue, not demand_rejoue in ['oui,non'], demand_rejoue in ['oui','non'])
            demand_rejoue = input("réponse non compise, voulez-vous rejouer?(oui ou non)")
        if demand_rejoue == 'non':
            jouer = not jouer
        else:
             print('\n\n\n\n\n\nNEW GAME')
    print('Au final Toads a gangné',win_rate[0] ,'fois et Frogs a gagné',win_rate[1], 'pour un totale de', sum(win_rate), 'partie(s)')
        
 

if __name__ == "__main__" and False:#only far test 
    jouer = True
    win_rate = [0,0]
    n = 8
    p = 3
    nb_games = 200
    for i in range(nb_games):
        print("Bienvenue au jeu Toads and Frogs ")
        game = [toadsAndFrogsPvP, toadsAndFrogsPvE , toadsAndFrogsEvE] [2]
        gagnant = game(n,p)
        print(['Toads', 'Frogs'][gagnant] + ' WIN !!!!!!!!!!!!')
        win_rate[gagnant] = win_rate[gagnant] + 1
        print('\n\n\n\n\n\n\n\n\n\n\n\nNEW GAME, game', i)
    print('Au final Toads a gangné',win_rate[0] ,'fois et Frogs a gagné',win_rate[1], 'pour un totale de', sum(win_rate), 'partie(s)')
   
def avantages(n_min=3 , n_max=20, p_max=20, nb_games=200):
    totale = [[None]*p_max for _ in range(n_max)]
    for n in range(max(3, n_min), n_max):
        for p in range(1, n//2):
            print(n,p)
            grand_gagnant = [0,0]
            for game_number in range(nb_games):
                game = toadsAndFrogsEvE(n,p)
                grand_gagnant[game] = grand_gagnant[game] + 1
                print(['Toads', 'Frogs'][game] + ' WIN !!!!!!!!!!!!')
                print('\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n\n\nNEW GAME, game n°', game_number)
            if grand_gagnant[0]>int(nb_games/2):
                totale[n][p] = 'Toads'
            elif grand_gagnant[1]>int(nb_games/2):
                totale[n][p] = 'Frogs'
            else:
                totale[n][p] = 'TIE'
    return totale

WIN_RATE = avantages(n_min=5, n_max=6, p_max = 5, nb_games=100)
print(WIN_RATE[5])         
        