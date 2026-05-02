from tkinter import *
from tkinter import ttk
from game import Wordle

def main():
    game = Wordle()
    game.bind("<Key>", game.on_letter_key)
    game.bind("<BackSpace>", lambda event: game.on_backspace())
    game.bind("<Return>", lambda event: game.on_enter())
    game.mainloop()

if __name__ == "__main__":
    main()