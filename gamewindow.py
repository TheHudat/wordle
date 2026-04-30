from tkinter import *
from tkinter import ttk
from constants import *
from gamesquare import GameSquare

class GameWindow(ttk.Frame):
    #class for the full Wordle game window
    def __init__(self, root):
        super().__init__(root)
        self['padding'] = (3, 3, 12, 12)

    def generate_new_window(self, root, squares_array):
        #initiate the window and display the background
        root.title("Wordle")
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        
        #display each of the GameSquares in squares_array in the window
        for row in range(6):
            for column in range(5):
                squares_array[row][column].grid(column=column, row=row, sticky=(E, N))
                squares_array[row][column].columnconfigure(column, weight=1)
                squares_array[row][column].rowconfigure(row, weight=1)
    
    def generate_starting_squares(self):
        #creates a list of lists containing GameSquares to fill the game board
        squares = []
        for row in range(6):
            square_row = []
            for column in range(5):
                square_row.append(GameSquare(self))
            squares.append(square_row)
        return squares