from tkinter import *
from tkinter import ttk
import random

from constants import *
from gamesquare import GameSquare

'''TODO add text field at the bottom of the window to give feedback
Add a play again button that comes up after a correct guess?
Add a score screen?
Add difficulty?'''
class Wordle(Tk):
    #class for the full Wordle game window
    def __init__(self):
        super().__init__()
        #start window and set title on top bar
        self.title("Wordle")
        self.active_row = 0
        self.active_column = 0
        self.word_entry = ""
        
        #select solution word from words file
        with open("5-Letter-Words.txt", "r") as file:
            self.words = file.read().splitlines()
        self.word_solution = random.choice(self.words)
        print(f"Solution: {self.word_solution}")
        
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
    
    def on_letter_key(self, event):
        letter = event.char
        row = self.active_row
        column = self.active_column
        
        if letter in LETTERS: #add letter to active square
            self.squares[row][column].letter_text.set(letter.capitalize())
            #adding letter to word_entry
            if len(self.word_entry) == 5:
                self.word_entry = self.word_entry[:4] + letter
            else:
                self.word_entry += letter
            print(f"Letter Set. Letter: {letter}  Word_entry: {self.word_entry}")
        
            #move to next active input square
            if column < 4:
                self.active_column += 1
    
    def on_backspace(self):
        row = self.active_row
        column = self.active_column
        if self.active_column == 4 and self.squares[row][column].letter_text.get() != '':
            self.squares[row][column].letter_text.set('')
            self.word_entry = self.word_entry[:-1]
            print(f"Letter Removed. Word_entry: {self.word_entry}")
            return
        if self.active_column > 0:
            self.active_column -= 1
            self.squares[row][self.active_column].letter_text.set('')
            self.word_entry = self.word_entry[:-1]
            print(f"Letter Removed. Word_entry: {self.word_entry}")

    def on_enter(self):
        row = self.active_row
        column = self.active_column
        #only on a full word
        if column == 4 and self.squares[row][column].letter_text.get() != '':
            #set colors on each square in row
            for col in range(5):
                if self.word_entry[col] == self.word_solution[col]:
                    self.squares[row][col].set_square_color('g')
                    continue
                if self.word_entry[col] in self.word_solution:
                    self.squares[row][col].set_square_color('y')
                
            #set next row as active
            self.active_column = 0
            self.active_row +=1
            self.word_entry = ""
            print(f'Row reset exicuted. Word_entry: "{self.word_entry}" (should be blank)')
        
