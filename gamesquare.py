from tkinter import *
from tkinter import ttk
from constants import *

class GameSquare(ttk.Frame):
    def __init__(self, parent, row, column):
        super().__init__(parent)
        #set options for GameSquare ttk.Frame
        self['width'] = GAME_SQUARE_WIDTH
        self['height'] = GAME_SQUARE_HEIGHT
        self['borderwidth'] = 5
        self['relief'] = "ridge"
        self.grid_propagate(False)
        self.grid(row=row, column=column)
        self.columnconfigure(column, weight=1)
        self.rowconfigure(row, weight=1)
        
        #create a widget to display a letter in the GameSquare
        self.letter_text = StringVar() #setable variable for the squares letter
        self.letter = ttk.Label(self, textvariable=self.letter_text, justify="center", font=("arial", -90))
        self.letter.grid(row=0, column=0)
        self.letter.columnconfigure(column, weight=1)
        self.letter.rowconfigure(row, weight=1)

#TODO get text to align in center of square after first in each row