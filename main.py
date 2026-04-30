from tkinter import *
from tkinter import ttk
from gamewindow import GameWindow


root = Tk()
game = GameWindow(root)
squares = game.generate_starting_squares()
game.generate_new_window(root, squares)
squares[0][0].letter_text.set("T")
root.mainloop()

