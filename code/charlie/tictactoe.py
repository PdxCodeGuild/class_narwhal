class Game:

    def __init__(self, board=[]):
        self.board = [[ '' for column in range(0,3)] for row in range(0,3)]

    
    def move(self, x, y, player):
        if self.board[x][y] == '':
            self.board[x][y] = 

    def calc_winner(self):
        pass
    def is_full(self):
        pass
    def is_game_over(self):
        pass

class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = token


def main():
    game = Game()
    choice = ''
    print("Welcome to a good ole game of tic-tac-toe!\n To get started we'll need to enter player names and tokens.\n")
    name1 = input("Player 1 please enter your name: ")
    token1 = input(f"{name1} Please choose whether you would like to be X's or O's (type X or O): ")
    name2 = input("Player 2 please enter your name: ")
    if token1 == 'X': 
        token2 = 'O'
    else:
        token2 = 'X'
    player1 = Player(name1, token1)
    player2 = Player(name2, token2)

    
    while choice != 'exit':
        if choice == 'move':
            pass
        elif choice == '':
            pass
        elif choice == 'help':
            print("move   - move your token to a position on the board")
            print("winner - checks to see who has won if anyone?")
            print("exit   -  quits the game")

main()