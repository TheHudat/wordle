# Wordle
Its just wordle. Type in 5 letter words and use the feedback about the letters to guess the mystery word.

## How it work
A game window opens when you run main.py and the game chooses a random 5 letter word as the answer. The game reads when letters are typed in (backspace will remove the last letter). Letters are added to the game board as they are typed in. When 5 letters are entered and the user presses Return they get feedback on the entry.
- Each letter that matches the letter and position in the answer turns green
- Each letter that matches a letter in the answer but in the wrong position turns yellow
- If the 5 letters are not a word on the word list, the row resets and the user starts the word again

The player gets 6 guesses (same as the number of entry rows on the game board). If they guess the correct word within the 6 guesses, the game tells them they have won and a Try Again button appears. If they use 6 guesses and dont get the answer, the game tells them they lost and the Try Again button appears. The Try Again button resets the game.

There is a Give Up button at the bottom of the game window at all times before the player has won or lost. The give up button reveals the answer and turns into the Try Again button.

## Tools
Built with tkinter package to create a game window

5 letter word file comes from here: https://gist.github.com/daemondevin/df09befaf533c380743bc2c378863f0c
