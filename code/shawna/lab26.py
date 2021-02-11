class GameBoard:
 
    def __init__(self):
        self.board = {
        #(x,y)
        (0,0) : "O",
        (0,1) : " ",
        (0,2) : " ",
        (1,0) : " ",
        (1,1) : "O",
        (1,2) : " ",
        (2,0) : " ",
        (2,1) : " ",
        (2,2) : " ",
        }

    def __repr__(self):
        #x is horizontal, y is vertical positions are(x,y)
        return(f"""
        -------------
        | {self.board.get((0,0))} | {self.board.get((1,0))} | {self.board.get((2,0))} |
        -------------
        | {self.board.get((0,1))} | {self.board.get((1,1))} | {self.board.get((2,1))} |
        -------------
        | {self.board.get((0,2))} | {self.board.get((1,2))} | {self.board.get((2,2))} |
        -------------
        """)

    def move(self, x, y, player):
        x = ((int(x) - 1))
        y = (int(y) - 1)
        self.board[(x,y)] = player.token

    def calc_winner(self, x, y, player):
        x = ((int(x) - 1))
        y = ((int(y) - 1))
        #check column
        if self.board[(x,0)] == player.token and self.board[(x,1)] == player.token and self.board[(x,2)] == player.token:
            print(f"{player.name} is the winner.")
        #check row
        elif self.board[(0,y)] == player.token and self.board[(1,y)] == player.token and self.board[(2,y)] == player.token:
            print(f"{player.name} is the winner.")
        #check diagonal 
        elif self.board[(0,0)] == player.token and self.board[(1,1)] == player.token and self.board[(2,2)] == player.token:
            print(f"{player.name} is the winner.")
        #continue
        else:
            return False

class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = token


#------------------------------------------------------------------------------------#
# Main Repl
#------------------------------------------------------------------------------------#

print("Let's Play Tic-Tac-Toe")

while True:

    #gather player one info
    p1_name = input("Player 1, enter your name: ")
    p1_token = ""
    while not (p1_token == 'X' or p1_token == 'O'):
        p1_token = (input("Would you like to be X's or O's: ")[0]).upper()
    
    #Create player one
    p1 = Player(p1_name, p1_token)

    #gather player two info
    p2_name = input("Player 2, enter your name: ")
    p2_token = ""
    while not (p2_token == 'X' or p2_token == 'O'):
        p2_token = (input("Would you like to be X's or O's: ")[0]).upper()
    
    #Create player one
    p2 = Player(p2_name, p2_token)

    #Print the empty board
    board = GameBoard()
    print(board.__repr__())
    
    #player 1 move
    print(f"{p1.name} it is your turn.")
    x = ""
    while not (x == "1" or x == "2" or x == "3"):
        x = input("Which COLUMN would you like to place your token? 1, 2, or 3?\nColumn: ")
    y = ""
    while not (y == "1" or y == "2" or y == "3"):
        y = input("Which ROW would you like to place your token? 1, 2, or 3?\nRow: ")
    
    board.move(x,y,p1)
    board.calc_winner(x,y,p1)

    print(board.__repr__())

