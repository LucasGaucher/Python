"""
Author: L. GAUCHER
Creation Date: 14/11/1524 14:12
"""
from tkinter import *
from tkinter import messagebox

class Dawson:
    def __init__(self, n=15):
        self.__board = [0] * n  # 0 means no piece, 1 for player 1, -1 for player 2
        self.__n = n
        self.__currentjoueur = 1  # Player 1 starts
        self.__currentSelection = None
        self.__joueur = 1  # This tracks whose turn it is (1 for player 1, 2 for player 2)

        # GUI setup
        self.__PXCASE = 70
        self.__root = Tk()
        self.__root.configure(background='black')
        self.__root.title("Dawson's Chess")
        self.__canvas = Canvas(self.__root, width=self.__n * self.__PXCASE + 1, height=self.__PXCASE + 51, bg="white", highlightthickness=0, bd=0)
        self.__canvas.place(x=0, y=0)  # Place the canvas at the origin
        self.__canvas.bind("<Button-1>", self.gameTurn)

        self.__toPlay = StringVar()
        self.__label = Label(self.__root, text="Player " + str(self.__currentjoueur), font=("Courier", 20), fg="white", bg="black")
        self.__label.place(x=(n // 2) * self.__PXCASE - 100, y=self.__PXCASE + 10)

        self.drawBoard()  # Initial board setup
        self.__root.mainloop()

    def possible(self, case):
        """Check if a case is free to place a piece (0 means available)."""
        return self.__board[case] == 0

    def put(self, case):
        """Place a piece on the board."""
        if case - 1 >= 0:
            self.__board[case - 1] = -1  # Block previous positions
        self.__board[case] = 1
        if case + 1 < self.__n:
            self.__board[case + 1] = -1 

    def again(self):
        """Check if the game can continue (if there are any available moves)."""
        return 0 in self.__board

    def updateGUI(self):
        """Update the graphical interface based on the current board state."""
        self.__canvas.delete("all")
        self.drawBoard()

    def drawBoard(self):
        """Draw the game board and current state of pieces."""
        self.__canvas.create_line(0, self.__PXCASE, self.__n * self.__PXCASE, self.__PXCASE, fill="white", width=2)  # top border
        self.__canvas.create_line(0, 0, self.__n * self.__PXCASE, 0, fill="white", width=2)
        for i in range(self.__n):
            self.__canvas.create_rectangle(i * self.__PXCASE, 0, i * self.__PXCASE, self.__PXCASE, fill="white", width=2)
            if self.__board[i] == 1:
                self.__canvas.create_oval(i * self.__PXCASE + 10, 10, i * self.__PXCASE + 60, 60, fill="red", outline="black", tag="x" + str(i))
            elif self.__board[i] == -1:
                self.__canvas.create_oval(i * self.__PXCASE + 10, 10, i * self.__PXCASE + 60, 60, fill="yellow", outline="black", tag="x" + str(i))
            else:
                self.__canvas.create_oval(i * self.__PXCASE + 10, 10, i * self.__PXCASE + 60, 60, fill="black", outline="black", tag="x" + str(i))

        self.__label.config(text="Player " + str(self.__currentjoueur))

    def gameTurn(self, event):
        """Handle a player's turn."""
        indice = event.x // self.__PXCASE
        if self.possible(indice):
            self.put(indice)
            self.updateGUI()
            if self.again():
                self.__currentjoueur = 2 if self.__currentjoueur == 1 else 1
            else:
                messagebox.showinfo(title="Game Over", message=f"Player {self.__currentjoueur % 2 + 1} wins!")
                if messagebox.askyesno(title="Replay?", message="Do you want to play again?"):
                    self.newGame()
                else:
                    self.__root.destroy()

    def newGame(self):
        """Reset the game to start a new round."""
        self.__board = [0] * self.__n
        self.__currentjoueur = 1
        self.__canvas.delete("all")
        self.drawBoard()

class ToadsAndFrogs:
    def __init__(self, n: int = 15, p: int = 5):
        self.__n = n
        self.__p = p
        # Initialize the board: 1 for frogs, 2 for toads, and 0 for empty spaces
        self.__board = [2 if i >= (self.__n - self.__p) else 1 if i < self.__p else 0 for i in range(n)] if (p := min(self.__p, self.__n // 2 - 1)) >= 0 else [0] * self.__n
        self.__currentjoueur = 1  # Player 1 starts
        self.__currentSelection = None

        # GUI setup
        self.__PXCASE = 70
        self.__root = Tk()
        self.__root.configure(background='black')
        self.__root.title("Toads and Frogs")
        self.__canvas = Canvas(self.__root, width=self.__n * self.__PXCASE + 1, height=self.__PXCASE + 51, bg="white", highlightthickness=0, bd=0)
        self.__canvas.place(x=0, y=0)
        self.__canvas.bind("<Button-1>", self.gameTurn)

        self.__toPlay = StringVar()
        self.__label = Label(self.__root, text="Player " + str(self.__currentjoueur), font=("Courier", 20), fg="white", bg="black")
        self.__label.place(x=(n // 2) * self.__PXCASE - 100, y=self.__PXCASE + 10)

        self.drawBoard()  # Initial board setup
        self.__root.mainloop()

    def possible(self, i: int):
        """
        Check if the square i is playable for the current player.
        """
        direction = 1 if self.__currentjoueur == 1 else -1
        if self.__board[i] != self.__currentjoueur:
            return False
        # Check if the player can move to the next square
        if self.__board[i + direction] == 0:
            return True
        # Check if the player can jump over an opponent's piece
        if 0 <= i + 2 * direction < self.__n and self.__board[i + direction] == (2 if self.__currentjoueur == 1 else 1) and self.__board[i + 2 * direction] == 0:
            return True
        return False

    def put(self, i: int):
        """
        Move a piece at index i for the current player.
        """
        direction = 1 if self.__currentjoueur == 1 else -1
        if self.__board[i + direction] == 0:  # Regular move
            self.__board[i], self.__board[i + direction] = 0, self.__currentjoueur
        else:  # Jump over an opponent's piece
            self.__board[i], self.__board[i + 2 * direction] = 0, self.__currentjoueur

    def again(self):
        """Check if the current player has another valid move."""
        direction = 1 if self.__currentjoueur == 1 else -1
        for i in range(self.__n):
            if self.__board[i] == self.__currentjoueur:
                if self.possible(i):
                    return True
        return False

    def updateGUI(self):
        """Update the graphical interface based on the current board state."""
        self.__canvas.delete("all")
        self.drawBoard()

    def drawBoard(self):
        """Draw the game board and current state of pieces."""
        self.__canvas.create_line(0, self.__PXCASE, self.__n * self.__PXCASE, self.__PXCASE, fill="white", width=2)  # top border
        self.__canvas.create_line(0, 0, self.__n * self.__PXCASE, 0, fill="white", width=2)  # bottom border
        for i in range(self.__n):
            self.__canvas.create_rectangle(i * self.__PXCASE, 0, (i + 1) * self.__PXCASE, self.__PXCASE, fill="white", width=2)
            if self.__board[i] == 1:
                self.__canvas.create_oval(i * self.__PXCASE + 10, 10, (i + 1) * self.__PXCASE - 10, self.__PXCASE - 10, fill="blue", outline="black")
            elif self.__board[i] == 2:
                self.__canvas.create_oval(i * self.__PXCASE + 10, 10, (i + 1) * self.__PXCASE - 10, self.__PXCASE - 10, fill="red", outline="black")
            else:
                self.__canvas.create_oval(i * self.__PXCASE + 10, 10, (i + 1) * self.__PXCASE - 10, self.__PXCASE - 10, fill="black", outline="black")

        self.__label.config(text="Player " + str(3-self.__currentjoueur))

    def gameTurn(self, event):
        """Handle a player's turn."""
        indice = event.x // self.__PXCASE
        if self.possible(indice):
            self.put(indice)
            self.updateGUI()

            # Check if the current player has valid moves left
            if self.again():
                self.__currentjoueur = 2 if self.__currentjoueur == 1 else 1  # Switch player if the current player has moves left
            else:
                messagebox.showinfo(title="Game Over", message=f"Player {self.__currentjoueur % 2 + 1} wins!")
                if messagebox.askyesno(title="Replay?", message="Do you want to play again?"):
                    self.newGame()
                else:
                    self.__root.destroy()

    def newGame(self):
        """Reset the game to start a new round."""
        self.__board = [2 if i >= (self.__n - self.__p) else 1 if i < self.__p else 0 for i in range(self.__n)] if (p := min(self.__p, self.__n // 2 - 1)) >= 0 else [0] * self.__n
        self.__currentjoueur = 1
        self.__canvas.delete("all")
        self.drawBoard()

# Start the game
#game = ToadsAndFrogs(5, 2)

# Start the game
game = Dawson()



"""
Author: L. GAUCHER
Creation Date: 15/11/1524 13:09
"""
from tkinter import *
from time import *

class Tapis:
    def __init__(self, x:int, y:int, n:int):
        self.__x = x
        self.__y = y
        self.__root = Tk()
        self.__root.title("Tapis de Sierpińsk")
        self.__root.configure(background='white')
        

        self.__canvas = Canvas(self.__root, width=x, height=y, bg="blue")
        self.__canvas.pack()
        

        self.affiche(0, 0, n, x, y)
        self.__root.mainloop()
        
    def affiche(self, x:int, y:int, n:int, width:int, height:int):
        if not(n == 0):
            self.__canvas.create_rectangle(x + width // 3, y + height // 3, x + width*2 // 3, y + height*2 // 3, fill="white", outline="white")
            print(x + width // 3, y + height // 3, x + width*2 // 3, y + height*2 // 3)
            for i in range(3):
                for j in range(3):
                    if not (i == 1 and j == 1):
                        self.affiche(x + i * width // 3, y + j * height // 3, n - 1, width//3, height//3)


for i in range(4):
    if False:
        tapis = Tapis(900, 900, i+1)

