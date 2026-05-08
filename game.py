from tkinter import *
from tkinter import ttk
import random

from constants import *
from gamesquare import GameSquare

'''TODO
Add a rules tab
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
        self.guess_count = 0
        self.input_on = True
        
        #select solution word from words file
        with open("5-Letter-Words.txt", "r") as file:
            self.words = file.read().splitlines()
        self.word_solution = random.choice(self.words)
        
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

        #Add status text to the bottom of the window
        self.status_text = StringVar() 
        self.text = ttk.Label(self.game_window, textvariable=self.status_text)
        self.status_text.set("Welcome to Wordle! Type in 5 letter words and press Enter.")
        self.text.grid(column=0, row=6, columnspan=4, pady=10)

        #add button to screen
        self.button = ttk.Button(self.game_window, text="Give Up", command=self.on_give_up)
        self.button.grid(column=4, row=6, pady=5)
    
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
        
        if letter in LETTERS and self.input_on: #add letter to active square
            self.squares[row][column].letter_text.set(letter.capitalize())
            #adding letter to word_entry
            if len(self.word_entry) == 5:
                self.word_entry = self.word_entry[:4] + letter
            else:
                self.word_entry += letter
        
            #move to next active input square
            if column < 4:
                self.active_column += 1
    
    def on_backspace(self):
        row = self.active_row
        column = self.active_column
        if self.input_on:
            if self.active_column == 4 and self.squares[row][column].letter_text.get() != '':
                self.squares[row][column].letter_text.set('')
                self.word_entry = self.word_entry[:-1]
                return
            if self.active_column > 0:
                self.active_column -= 1
                self.squares[row][self.active_column].letter_text.set('')
                self.word_entry = self.word_entry[:-1]

    def on_enter(self):
        row = self.active_row
        column = self.active_column
        green_count = 0
        yellow_count = 0
        
        #only on a full word
        if column == 4 and self.squares[row][column].letter_text.get() != '' and self.input_on:
            #check if entry is a word
            if self.word_entry not in self.words:
                self.status_text.set("Word is not on the list. Try Again.")
                self.reset_row()
                return
            
            self.guess_count += 1
            #set colors on each square in row
            for col in range(5):
                if self.word_entry[col] == self.word_solution[col]:
                    self.squares[row][col].set_square_color('g')
                    green_count += 1
                    continue
                if self.word_entry[col] in self.word_solution:
                    self.squares[row][col].set_square_color('y')
                    yellow_count += 1

            if green_count == 5:
                self.on_win()
                return
            
            if self.active_row == 5:
                self.on_loss()
                return

            #set next row as active
            self.active_column = 0
            self.active_row += 1
            self.word_entry = ""
            self.status_text.set("Type in 5 letter words and press Enter.")
        
    def on_win(self):
        self.input_on = False
        self.status_text.set(f"You Win! {self.guess_count} guesses")
        self.button.configure(text="Play Again", command=self.reset_game)
    
    def on_loss(self):
        self.input_on = False
        self.status_text.set(f"You are out of guesses. The word was: {self.word_solution}. Try Again!")
        self.button.configure(text="Play Again", command=self.reset_game)
    
    def reset_game(self):
        self.active_column = 0
        self.active_row = 0
        self.guess_count = 0
        self.input_on = True
        self.word_entry = ""
        self.word_solution = random.choice(self.words)

        for row in self.squares:
            for square in row:
                square.reset_square()
        
        self.status_text.set("Welcome to Wordle! Type in 5 letter words and press Enter.")
        self.button.configure(text="Give Up", command=self.on_give_up)
    
    def reset_row(self):
        self.active_column = 0
        self.word_entry = ""
        self.input_on = True

        for square in self.squares[self.active_row]:
            square.reset_square()

    def on_give_up(self):
        self.button.configure(text="Play Again", command=self.reset_game)
        self.status_text.set(f"The answer was: {self.word_solution}. Try Again?")