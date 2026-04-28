from tkinter import *
from tkinter import ttk
from constants import *

class GameSquare(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['width'] = GAME_SQUARE_WIDTH
        self['height'] = GAME_SQUARE_HEIGHT
        self['borderwidth'] = 5
        self['relief'] = "ridge"
