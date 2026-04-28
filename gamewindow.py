from tkinter import *
from tkinter import ttk
from constants import *
from gamesquare import GameSquare

#TODO make GameWindow a frame class and generate the starting game board on init 
class GameWindow:
    def __init__(self, root):
        root.title("Wordle")

        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.generate_square_row(mainframe, 0)
        self.generate_square_row(mainframe, 1)
        self.generate_square_row(mainframe, 2)
        self.generate_square_row(mainframe, 3)
        self.generate_square_row(mainframe, 4)
        self.generate_square_row(mainframe, 5)

    
    def generate_square_row(self, parent, row_number):
        letter_square = GameSquare(parent)
        letter_square2 = GameSquare(parent)
        letter_square3 = GameSquare(parent)
        letter_square4 = GameSquare(parent)
        letter_square5 = GameSquare(parent)

        letter_square.grid(column = 0, row = row_number, sticky=(E, N))
        letter_square2.grid(column = 1, row = row_number, sticky=(E, N))
        letter_square3.grid(column = 2, row = row_number, sticky=(E, N))
        letter_square4.grid(column = 3, row = row_number, sticky=(E, N))
        letter_square5.grid(column = 4, row = row_number, sticky=(E, N))