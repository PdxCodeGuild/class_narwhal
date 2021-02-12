'''
=-=-= Lab 26 11 Feb 20201 =-=-=
=-=-=-=-= Tic Tac Toe =-=-=-=-=
=-=-=- Composer: brndn -=-=-=-=
'''

class Player:
    def __init__(self,name=0,token=''):
        self.name = name
        self.token = token

class Game(Player):
    def __init__(self,board='0|1|2\n3|4|5\n6|7|8'):
        super().__init__()
        self.board = board

    def __repr__(self):
        return '\033[4m'+self.board[0:11]+'\033[0m'+self.board[11:17]

    def move(self,place,player):
        self.token = player
        if place not in 'XxOo':
            self.board = self.board.replace(place, self.token)
        
        #print(f'\n{game.__repr__()}')
    def calc_winner(self):
        win = self.board.replace('\n','').replace('|','')
        won = win[::4],win[2:8:2],win[::3],win[1::3],win[2::3],win[0:3],win[3:6],win[6:9]
        if 'XXX' in won:
            return 1
        elif 'OOO' in won:
            return 2

    def is_full(self): #returns true if board full
        return sorted(self.board) == 'OOOOXXXXX'

    def is_game_over(self): #returns true if board full or player won
        if is_full == True or calc_winner == True:
            return True

game = Game()

players = 1
while True:

    print(f'\n{game.__repr__()}')

    if players == 1:
        player = 'X'
    else:
        player = 'O'

    move = input(f'\nPlayer {players}\nPlace Token: >>> ')
    if move == 'exit':
        break
    elif move in game.board or move not in 'XO':
        game.move(move, player)
        
    elif game.calc_winner() != None:
        print(f'\nWinner: Player {game.calc_winner()}')
    elif game.is_full() == True:
        game.is_game_over()
    else:
        print('\nInvalid Placement')
        continue

    if players == 1:
        players += 1
    else:
        players -= 1
