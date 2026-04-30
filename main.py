from tkinter import *
from tkinter import ttk
from game import Wordle

def main():
    game = Wordle()
    game.bind("<Key>", game.button_input)
    game.mainloop()

if __name__ == "__main__":
    main()