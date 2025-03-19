""""
Auteur: GAUCHER L.
creation: 24/10/2024 13:47
Dodgem
"""
def newBoard(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        board[i][0] = 2
    for i in range(1,n):
        board[n-1][i] = 1
    return board

def displayBoard(board, n):
    car = '╔═╦═' + '╦═'*(n-1) + '╗\n'
    for i in range(1,n+1):
        car += '║'+str(i) + '║'
        for j in range(n):
            car += [' ','□','■'][board[i-1][j]] + '║'
        car += '\n'
        if i < n:
            car += '╠═╬' + '═╬'*(n-1) + '═╣' + '\n'
    car += '╚═╬' + '═╬'*(n-1) + '═╣' + '\n'
    car += '  ║'
    for i in range(n):
        car += str(i+1) +'║'
    car += '\n  ╚'+ '═╩'*(n-1) + '═╝'
    print(car)
    
def possiblePawn(board, n, directions, player, i, j):
    if i < 0 or i >= n or j < 0 or j >= n:#appartenace au plateau
        return False
    if board[i][j] != player:#appartenance au joueur
        return False
    if player==1 and (i==0 or i>0 and board[i-1][j]==0) and (j<n-1 and board[i][j+1]==0) and (j>0 and board[i][j-1]==0):
        return False
    if player==2 and (i>0 and board[i-1][j]==0) and (j==n-1 or j<n-1 and board[i][j+1]==0) and (i<n-1 and board[i+1][j]==0):
        return False
    return True

def selectPawn(board, n, directions, player):
    """
    fait saisir au joueur player la coordonnée d'un pion qu'il peut déplacer
    """
    i = int(input('Choisir un numéro de ligne : '))-1
    j = int(input('Choisir un numéro de colonne : '))-1
    while not possiblePawn(board, n, directions, player, i, j):
        i = int(input('Choisir un numéro de ligne : '))-1
        j = int(input('Choisir un numéro de colonne : '))-1
    return i,j

def possibleMove(board, n, directions, player, i, j, m):
    if not(1 <= m <= 4):
        return False
    if player==1:
        return [i==0 or i>0 and board[i-1][j]==0, j<n-1 and board[i][j+1]==0, False, j>0 and board[i][j-1]==0][m-1]
    else:
        return [i>0 and board[i-1][j]==0, j==n-1 or j<n-1 and board[i][j+1]==0, i<n-1 and board[i+1][j]==0, False][m-1]

def selectMove(board, n, directions, player, i, j):
    poss_move = ['1 pour Nord (↑), 2 pour Est (→) et 4 pour Ouest (←)', '1 pour Nord (↑), 2 pour Est (→) et 3 pour Sud (↓)'][player-1]
    dir = int(input('Choisir la direction du mouvement ('+poss_move+') : '))
    while not possibleMove(board, n, directions, player, i, j, dir):
        dir = int(input('Choisir la direction du mouvement ('+poss_move+') : '))
    return dir


def move(board, n, directions, player, i, j, m):
    di, dj = directions[m - 1]
    new_i = i + di
    new_j = j + dj
    if 0 <= new_i < n and 0 <= new_j < n:
        board[new_i][new_j] = player
    board[i][j] = 0

def win(board, n, directions, player):
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == player:#si le joueur n'a plus de pions
                return False
            if possiblePawn(board, n, directions, 3-player, i, j):#son adversaire(3-player) ne peut plus jouer
                return False
    return True


def dodgem(n):
    board = newBoard(n)
    joueur = 1
    directions=(-1, 0), (0, 1), (1, 0), (0, -1)
    while not(win(board, n, directions, 3-joueur)):# tant que l'adversaire n'a pas déjà gagné
        displayBoard(board, n)
        print("C'est au tour du joueur", joueur,'(vous etres ' + ['□','■'][joueur-1] + ')' )
        i, j = selectPawn(board, n,directions , joueur)
        m = selectMove(board, n, directions, joueur, i, j)
        move(board, n, directions, joueur, i, j, m)
        joueur = 3- joueur
    displayBoard(board, n)
    return 3-joueur


if __name__ == "__main__":
    jouer = True
    print("Bienvenue au jeu de dodgem")
    win_rate = [0,0]
    while jouer:
        n = int(input("le nombre de cases : "))
        gagnant = dodgem(n)
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
