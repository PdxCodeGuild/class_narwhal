# Lab 26 - Tic Tac Toe
# Richard Farr
# Febuary 11th, 2021
'''

[Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) is a game.
Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid.
Whoever gets three in a row first wins.

You will write a **Player** class and **Game** class to model Tic Tac Toe, 
and a function **main** that models gameplay taking in user inputs through REPL.


The Player class has the following properties: 
name = player name
token = 'X' or 'O'
'''
class Player:
    def __init__(self, name, token): # this is the initializer
        self.name = name # these are member variables
        self.token = token

player_1 = Player("Richard", "X")
player_2 = Player("Theresa", "O")


'''
The Game class has the following properties:

board = your representation of the board
You can represent the board however you like, such as a 2D list, tuples, or dictionary.

'''


def drawBoard():
    board = ["","","","","","","","",""]
    print(board[0] + '|' + board[1] + '|' + board[2] )
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5] )
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8] )

drawBoard()



class Game:
    def __init__(self, board):
        self.board = board

    # def drawBoard(self):



'''
The Game class has the following methods:

 __repr__()` Returns a pretty string representation of the game board

print(board)
X| | 
O|X|O
 | | 


* `move(x, y, player)` Place a player's token character string at a given coordinate (top-left is 0, 0), 
x is horizontal position, y is vertical position.

py
>>> board.move(2, 1, player_1)
 | | 
 | |X
 | | 


* `calc_winner()` What token character string has won or `None` if no one has.


X| | 
O|X|O
 | |X
board.calc_winner()
X


* `is_full()` Returns true if the game board is full.


X|O|X
X|X|O
O|O|X
board.is_full()
True


* `is_game_over()` Returns true if the game board is full or a player has won.


X|O|X
X|X|O
O|O|X
board.is_game_over()
True

X|O|
 | |X
 | |
board.is_game_over()
False
'''