'''
Josh Novac
Lab 26
Python
PDX Code Guild
'''


'''//////////////////////// CLASSES/FUNCTIONS ////////////////////////'''
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __str__(self):
        return self.token

class Game:
    def __init__(self):
        self.board = [ ' ',' ',' ',
                       ' ',' ',' ',
                       ' ',' ',' ' ]

    def __repr__(self):
        board = self.board
        return f'{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}'

    def move(self, position, player):
        if self.board[position - 1] != ' ':
            return False
        else:
            self.board[position - 1] = f'{player.token}'
            return True
        
    def calc_winner(self, player):
        #### ALL VERTICAL WINS ####
        #  X|-|-
        #  X|-|-
        #  X|-|-
        if self.board[0] == self.board[3] == self.board[6] == player.token:
            return player.token
        #  -|X|-
        #  -|X|-
        #  -|X|-
        if self.board[1] == self.board[4] ==  self.board[7] == player.token:
            return player.token
        #  -|-|X
        #  -|-|X
        #  -|-|X
        if self.board[2] == self.board[5] == self.board[8] == player.token:
            return player.token
        #### ALL HORIZONTAL WINS ####
        #  X|X|X
        #  -|-|-
        #  -|-|-
        if self.board[0] == self.board[1] == self.board[2] == player.token:
            return player.token
        #  -|-|-
        #  X|X|X
        #  -|-|-
        if self.board[3] == self.board[4] == self.board[5] == player.token:
            return player.token
        #  -|-|-
        #  -|-|-
        #  X|X|X
        if self.board[6] == self.board[7] == self.board[8] == player.token:
            return player.token
        #### ALL DIAGONAL WINS ####
        #  X|-|-
        #  -|X|-
        #  -|-|X
        if self.board[0] == self.board[4] == self.board[8] == player.token:
            return player.token
        #  -|-|X
        #  -|X|-
        #  X|-|-
        if self.board[6] == self.board[4] == self.board[2] == player.token:
            return player.token
        return False

    def is_full(self):
        for i in self.board:
            if ' ' not in self.board:
                return True

    def is_game_over(self, player):
        if self.calc_winner(player) == player.token:
            return True
        else:
            if self.is_full() == True:
                return True
            else:
                return False

# prints the game rules for players that type 'help'
def help():
    print('\n----------------------------------------\n\t\t RULES\n----------------------------------------\n'\
    '\t  Enter a number 1-9\n1 = TOP LEFT, 2 = TOP MID, 3 = TOP RIGHT'\
    '\n4 = MID LEFT, 5 = MID MID, 6 = MID RIGHT\n7 = BOT LEFT, 8 = BOT MID, 9 = BOT RIGHT'\
    '\n----------------------------------------\n')


'''///////////////////////////////////////////////////////////REPL CODE///////////////////////////////////////////////////////////'''
def main():

    # welcome message to players
    print('\n    //////PYTHON TIC-TAC-TOE//////\n')
    # enter players names
    player_1 = Player(input('/PLAYER 1 NAME/: ').title(), 'X')
    player_2 = Player(input('//PLAYER 2 NAME//: ').title(), 'O')
    # program assigns tokens to players
    print(f'\n\n{player_1.name}: X\'s\t\t\t{player_2.name}: O\'s\n')
    # X's go first
    print(f'\t   {player_1.name} will go first!\n')
    print(f'xx      xx      o ooo o      xx      xx\n  xx  xx      oo       oo      xx  xx\n    xx       oo         oo       xx'\
        '\n  xx  xx      oo       oo      xx  xx\nxx      xx      o ooo o      xx      xx')
    # available move sequences for players
    print('\n----------------------------------------\n\t\t RULES\n----------------------------------------\n'\
        '\t  Enter a number 1-9\n1 = TOP LEFT, 2 = TOP MID, 3 = TOP RIGHT'\
        '\n4 = MID LEFT, 5 = MID MID, 6 = MID RIGHT\n7 = BOT LEFT, 8 = BOT MID, 9 = BOT RIGHT'\
        '\n----------------------------------------\n')

    # load empty board
    gameboard = Game()
    i = 1
    player_turn = player_1

    while True:
        if i % 2 == 0:
            player_turn = player_2
        else:
            player_turn = player_1

        print(f'\n   Player: {player_turn.name}  |  Enter Move (1-9): \n < Type \'help\' anytime to see the move sequences. >' )
        user_move = input()

        if user_move in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            user_move = int(user_move)
            if gameboard.move(user_move, player_turn):
                print('\nCURRENT GAME BOARD\n------------------\n')
                print(gameboard.__repr__())
                i += 1
            else:
                print(f'\n\tTHAT SPOT IS ALREADY TAKEN!\n')
        elif user_move == 'help':
            help()
        elif user_move == 'quit':
            break
        else:
            print(f'\nINVALID COMMAND! << Need help?  Type "help" in the command line. >> \n')

        if gameboard.is_game_over(player_turn) == True:
            if gameboard.calc_winner(player_turn) == "X":
                print(f'\n{player_turn.name} wins!\n\n')
                print(' THANK YOU FOR PLAY PYTHON TIC-TAC-TOE')
                print('\n----------------------------------------')
                print(f'xx      xx      o ooo o      xx      xx\n  xx  xx      oo       oo      xx  xx\n    xx       oo         oo       xx'\
                    '\n  xx  xx      oo       oo      xx  xx\nxx      xx      o ooo o      xx      xx')
                print('----------------------------------------')
                print('\u00A9 2021 Python Tic-Tac-Toe, Inc.\n')
                break
            elif gameboard.calc_winner(player_turn) == "O":
                print(f'\n{player_turn.name} wins!\n\n')
                print(' THANK YOU FOR PLAY PYTHON TIC-TAC-TOE')
                print('\n----------------------------------------')
                print(f'xx      xx      o ooo o      xx      xx\n  xx  xx      oo       oo      xx  xx\n    xx       oo         oo       xx'\
                    '\n  xx  xx      oo       oo      xx  xx\nxx      xx      o ooo o      xx      xx')                
                print('----------------------------------------')
                print('\u00A9 2021 Python Tic-Tac-Toe, Inc.\n')
                break
            else:
                print('\nTie Game!\n\n')
                print(' THANK YOU FOR PLAY PYTHON TIC-TAC-TOE')
                print('\n----------------------------------------\n')
                print(f'xx      xx      o ooo o      xx      xx\n  xx  xx      oo       oo      xx  xx\n    xx       oo         oo       xx'\
                    '\n  xx  xx      oo       oo      xx  xx\nxx      xx      o ooo o      xx      xx')                
                print('----------------------------------------')
                print('\n\u00A9 2021 Python Tic-Tac-Toe, Inc.')
                break

main()