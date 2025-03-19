""""
Auteur: GAUCHER L.
creation: 01/10/2024 14:34
"""

def new_board(n: int):
    """
    Crée une nouvelle grille de jeu de Dawson's Chess avec n cases.
    """
    return [0] * n

def display(board: list, n: int):
    """
    l'affichage du plateau sur la console du jeu de Dawson's Chess et de Toads and Frogs 
    """
    for i in range(n):
        nb = board[i]
        print(['.', 'X', 'O'][nb], end=' '*(len(str(i+2))))
    
    print('')
    
    for i in range(n):
        print(str(i+1), end=' ')
    print('')


def possible(board, n, i):
    """
    Vérifie si la case i est jouable.
    """
    if n>i and i>0:
        print(n>=i, i>0)
        return board[i] == 0
    return False

def select(board, n):
    nb = int(input("Quelle case choisissez-vous : "))
    while not possible(board, n, nb-1):
        print("Case invalide. Choisissez une autre case.")
        nb = int(input("Quelle case choisissez-vous : "))
    return nb-1

def put(board, n, i):
    """
    Joue une pièce dans la case i
    """
    if i-1 >= 0:
        board[i-1] = -1
    board[i] = 1
    if i+1 <= n-1:
        board[i+1] = -1
    

def again(board, n):
    """
    retourne True si le joueur courant peut poser un pion sur le plateau et False sinon
    """
    return 0 in board   

def Dawson(n):
    """
    Joue le jeu de Dawson avec 2 joueurs
    """
    board = new_board(n)
    joueur = 1
    while again(board, n):
        display(board, n)
        print("C'est au tour du joueur"+str(joueur))
        
        i = select(board, n)
        put(board, n, i)
        
        joueur = 2 if joueur == 1 else 1
    return joueur


if __name__ == "__main__":
    print("Bienvenue au jeu de Dawson's Chess")
    n = int(input("le nombre de cases : "))
    print("Le joueur", Dawson(n), "a gagné!")

