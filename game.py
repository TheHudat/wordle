from tkinter import *
from tkinter import ttk
from constants import *
from gamesquare import GameSquare

class Wordle(Tk):
    #class for the full Wordle game window
    def __init__(self):
        super().__init__()
        #start window and set title on top bar
        self.title("Wordle")
        self.active_row = 0
        self.active_column = 0
        
        #initiate the window and display the background      
        self.game_window = ttk.Frame(self, padding=(3, 3, 5, 5))
        self.game_window.grid(column=0, row=0, sticky=(N, W, E, S))

        #create square widgets and display the game board
        self.squares = self.generate_starting_squares()

        #create styles for the different square states
        self.colorY = ttk.Style()
        self.colorY.configure("ColorYellow.TFrame", background="yellow")
        self.colorG = ttk.Style()
        self.colorG.configure("ColorGreen.TFrame", background="green")
    
    def generate_starting_squares(self):
        #creates a list of lists containing GameSquares to fill the game board
        squares = []
        for row in range(6):
            square_row = []
            for column in range(5):
                square_row.append(GameSquare(self.game_window, row, column))
            squares.append(square_row)
        return squares
    
    def button_input(self, event):
        letter = event.char.capitalize()
        row = self.active_row
        column = self.active_column
        if letter in LETTERS:
            self.squares[row][column].letter_text.set(letter)
        
            #move to next active input square
            if column < 4:
                self.active_column += 1
            else:
                self.squares[row][column].set_square_color()
                self.active_row += 1
                self.active_column = 0
