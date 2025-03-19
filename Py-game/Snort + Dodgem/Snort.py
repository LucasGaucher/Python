""""
Auteur: GAUCHER L.
creation: 24/10/2024 13:23
Snort
"""


def newBoard(n: int):
    """
    Crée une nouvelle grille de jeu de Snort avec n cases.
    """
    return [[0 for _ in range(n)] for _ in range(n)]
    
def displayBoard(board, n):
    car = '╔═╦═' + '╦═'*(n-1) + '╗\n'
    for i in range(1,n+1):
        car += '║'+str(i) + '║'
        for j in range(n):
            car += [' ','■','□'][board[i-1][j]] + '║'
        car += '\n'
        if i < n:
            car += '╠═╬' + '═╬'*(n-1) + '═╣' + '\n'
    car += '╚═╬' + '═╬'*(n-1) + '═╣' + '\n'
    car += '  ║'
    for i in range(n):
        car += str(i+1) +'║'
    car += '\n  ╚'+ '═╩'*(n-1) + '═╝'
    print(car)
    
def possibleSquare(board: list, n: int, i: int, j: int, player: int):
    """
    Vérifie si la case (i, j) est jouable pour le joueur `player`.
    Retourne True si le joueur peut y jouer, sinon False.
    """
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if board[i][j] != 0:
        return False
    if i + 1 < n and board[i + 1][j] == 3 - player:
        return False
    if i - 1 >= 0 and board[i - 1][j] == 3 - player:
        return False
    if j + 1 < n and board[i][j + 1] == 3 - player:
        return False
    if j - 1 >= 0 and board[i][j - 1] == 3 - player:
        return False
    
    return True

    
def selectSquare(board: list, n:int, player:int):
    """
    fait saisir au joueur player la coordonnée d'un pion qu'il peut déplacer
    """
    i = int(input('Choisir un numéro de ligne : '))-1
    j = int(input('Choisir un numéro de colonne : '))-1
    while not possibleSquare(board,n,i,j,player):
        i = int(input('Choisir un numéro de ligne : '))-1
        j = int(input('Choisir un numéro de colonne : '))-1
    return i,j

def updateBoard(board: list, player: int, i: int, j:int):
    """
    Cette procédure réalise un déplacement dont i est la coordonnée d'un pion que le joueur player peut déplace
    """
    board[i][j] = player


def again(board: list, n: int, player: int):
    """
    Vérifie si le joueur `player` peut encore bouger un pion.
    Retourne True si un déplacement est possible, sinon False.
    """
    for i in range(n):
        for j in range(n):
            if possibleSquare(board, n, i, j,  player):
                return True
    return False
    

def snort(n:int):
    """
    joue au jeu de snort avec 2 joueur
    """
    board = newBoard(n)
    joueur = 1
    while again(board, n, joueur):
        displayBoard(board, n)
        print("C'est au tour du joueur", joueur)
        i, j = selectSquare(board, n, joueur)
        updateBoard(board, joueur, i, j)
        joueur = 2 if joueur == 1 else 1
    displayBoard(board, n)
    return 3-joueur



if __name__ == "__main__":
    jouer = True
    print("Bienvenue au jeu de snort")
    win_rate = [0,0]
    while jouer:
        n = int(input("le nombre de cases : "))
        gagnant = snort(n)
        print('joueur', gagnant , ' WIN !!!!!!!!!!!!')
        win_rate[gagnant-1] = win_rate[gagnant-1] + 1
        demand_rejoue = input("Voulez-vous rejouer?(oui ou non)")
        while not demand_rejoue in ['oui','non']:
            print(demand_rejoue, not demand_rejoue in ['oui,non'], demand_rejoue in ['oui','non'])
            demand_rejoue = input("réponse non compise, voulez-vous rejouer?(oui ou non)")
        if demand_rejoue == 'non':
            jouer = not jouer
        else:
             print('\n\n\n\n\n\n\n\n\n\n\n\nNEW GAME partie n°', sum(win_rate)+1)
    print('Au final Joueur1 a gagné',win_rate[0] ,'fois et Joueur2 a gagné',win_rate[1], 'pour un totale de', sum(win_rate), 'partie(s)')
        