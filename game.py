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
        self.active_row = IntVar()
        self.active_row.set(0)
        self.active_column = IntVar()
        self.active_column.set(0)
        
        #initiate the window and display the background      
        self.game_window = ttk.Frame(self, padding=(3, 3, 12, 12))
        self.game_window.grid(column=0, row=0, sticky=(N, W, E, S))

        #create square widgets and display the game board
        self.squares = self.generate_starting_squares()
    
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
        row = self.active_row.get()
        column = self.active_column.get()
        if letter in LETTERS:
            self.squares[row][column].letter_text.set(letter)
        
            #move to next active input square
            if column < 4:
                self.active_column.set(column + 1)
            else:
                self.active_row.set(row + 1)
                self.active_column.set(0)
