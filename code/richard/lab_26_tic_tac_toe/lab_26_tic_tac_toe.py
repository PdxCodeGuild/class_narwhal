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

# player_1 = Player("Richard", "X")
# player_2 = Player("Theresa", "O")


'''
The Game class has the following properties:

board = your representation of the board
You can represent the board however you like, such as a 2D list, tuples, or dictionary.
'''

class Game:
    def __init__(self, board):
        self.board = [" "] * 10

    # __repr__()` print(board) - Returns a pretty string representation of the game board 
    def __repr__(self):
        show = f"{self.board[0]}|{self.board[1]}|{self.board[2]}" + '\n' + f"{self.board[3]}|{self.board[4]}|{self.board[5]}" + '\n' + f"{self.board[6]}|{self.board[7]}|{self.board[8]}"
        return show

    # move(x, y, player) - Place a player's token character string at a given coordinate (top-left is 0, 0),
    # x is horizontal position, y is vertical position.
    def move(self, x, y, player):  # Do I need a long chain of ifs here?
        x = int(x) - 1
        y = int(y) - 1
        if x == 0 and y == 0 and self.board[0] == " ":
            self.board[0] = player.token
        elif x == 1 and y == 0 and self.board[1] == " ":
            self.board[1] = player.token
        elif x == 2 and y == 0 and self.board[2] == " ":
            self.board[2] = player.token  
        elif x == 0 and y == 1 and self.board[3] == " ":
            self.board[3] = player.token  
        elif x == 1 and y == 1 and self.board[4] == " ":
            self.board[4] = player.token  
        elif x == 2 and y == 1 and self.board[5] == " ":
            self.board[5] = player.token
        elif x == 0 and y == 2 and self.board[6] == " ":
            self.board[6] = player.token  
        elif x == 1 and y == 2 and self.board[7] == " ":
            self.board[7] = player.token  
        elif x == 2 and y == 2 and self.board[8] == " ":
            self.board[8] = player.token         

    # calc_winner() - What token character string has won or `None` if no one has.
    def calc_winner(self):
        if self.board[0] == self.board[1] == self.board[2]: # Across the Top
            return self.board[0]
        elif self.board[3] == self.board[4] == self.board[5]: # Across the Middle
            return self.board[3]
        elif self.board[6] == self.board[7] == self.board[8]: # Across the Bottom
            return self.board[6]
        elif self.board[0] == self.board[3] == self.board[6]: # Down the left side
            return self.board[0]
        elif self.board[1] == self.board[4] == self.board[7]: # Down the Middle
            return self.board[1]
        elif self.board[2] == self.board[5] == self.board[8]: # Down the Right Side
            return self.board[2]
        elif self.board[0] == self.board[4] == self.board[8]: # Diagnol - Top Left to bottom right 
            return self.board[0]
        elif self.board[6] == self.board[4] == self.board[2]: # Diagnol - Bottom Left to top right
            return self.board[6]
        

    # is_full() - Returns true if the game board is full.
    def is_full(self): #returns true if board full
        space = " "
        if space not in ''.join(self.board):
            return True

    # is_game_over() - Returns true if the game board is full or a player has won.
    def is_game_over(self):
        if self.is_full() == True or self.calc_winner() in ["x", 'o']:
            return True


    # reset_board() - takes the board back to 9 spaces with a " " in
    def reset_board(self):
        self.board = [" "] * 10
    

# print("print a blank board just to see if I can")
# board = Game(1)
# print(board)

    


# Steps to run the program below

while True:
    # Ask player one for input
    player_1_name = input("Player 1: Whats your name? ")
    player_1_token = input("Player 1: Do you want X or O? ").lower()

    # Create player one
    player_1 = Player(player_1_name, player_1_token)

    # Ask player two for their info
    player_2_name = input("Player 2: Whats your name? ")

    # Calculate player 2s token
    if player_1_token == "x":
        player_2_token = "o"
    else:
        player_2_token = "x"

    # Create player two
    player_2 = Player(player_2_name, player_2_token)

    # Tell the players what their tokens are:
    print(f"Player 1: {player_1_name} - {player_1_token}")
    print(f"Player 2: {player_2_name} - {player_2_token}")

    # Print the empty board
    board = Game(1)
    print(board)

    current_player = player_1

    while True:
        

        # Players Turn
        print(f"{current_player.name}: You are up next")

        col_choices = ["1", "2", "3"]
        col_choice = "0"
        while col_choice not in col_choices:
            col_choice = input("Which column do you pick? (1, 2, or 3) ")
        print(f"column choice: {col_choice}")
        
        row_choices = ["1", "2", "3"]
        row_choice = "0"
        while row_choice not in row_choices:
            row_choice = input("Which row do you pick? (1, 2, or 3 - top to bottom) ")
        print(f"row choice: {row_choice}")

        board.move(col_choice, row_choice, current_player)
        print(board)

        # see if we have a winner
        winner = board.calc_winner()

        # check to see if the game is over
        if board.is_game_over() == True:
            print("We have a winner!")
            break

        # Next players turn - if the game is not over
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1


    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break







'''
The Game class has the following methods:


print(board)

X| | 
O|X|O
 | | 


move(x, y, player)
 
Place a player's token character string at a given coordinate (top-left is 0, 0), 
x is horizontal position, y is vertical position.

board.move(2, 1, player_1)
 | | 
 | |X
 | | 


calc_winner()
What token character string has won or `None` if no one has.


X| | 
O|X|O
 | |X


board.calc_winner()
X


is_full()

 Returns true if the game board is full.


X|O|X
X|X|O
O|O|X


board.is_full()
True


is_game_over()
 Returns true if the game board is full or a player has won.


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










'''
board = ["","","","","","","","",""]

def drawBoard():
    
    print(board[7] + '|' + board[8] + '|' + board[9] )
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6] )
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3] )

drawBoard()
'''
