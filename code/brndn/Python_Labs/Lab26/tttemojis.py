'''
=-=-= Lab 26 11 Feb 20201 =-=-=
=-=-=-=-= Tic Tac Toe =-=-=-=-=
=-=-=- Composer: brndn -=-=-=-=
'''

class Player:
    def __init__(self,name,token):
        self.name = name
        self.token = token
        #if self.name == 1:
        #    self.token1 = token
        #if self.name == 2:
        #    self.token2 = token
            

class Game:
    def __init__(self,player1,player2,board='0 |1 |2 \n3 |4 |5 \n6 |7 |8 '):
        super().__init__()
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def __repr__(self):
        return '\033[4m'+self.board[0:17]+'\033[0m'+self.board[17:26]
        
    def choose_token(self,name,token):
        emoji = {
            1: '\N{THUMBS UP SIGN}',
            2: '\N{CACTUS}'
        }
        self.name = name
        self.token = emoji[token]
        
    def move(self,place,player):
        self.name = player#self.token = player
        self.board = self.board.replace(place + ' ', self.token)
    
    def calc_winner(self):
        win = self.board.replace('\n','').replace('|','').replace(' ','').replace(0,'X').replace(0,'O')
        won = win[::4],win[2:8:2],win[::3],win[1::3],win[2::3],win[0:3],win[3:6],win[6:9]
        if 'XXX' in won:
            return 1
        elif 'OOO' in won:
            return 2

    def is_full(self):
        return ''.join(sorted(self.board.replace('\n','').replace('|',''))) == 'OOOOXXXXX'

    def is_game_over(self):
        if self.is_full() == True or self.calc_winner() == 1 or self.calc_winner() == 2:
            return True

    def reset_board(self):
        self.board = '0 |1 |2 \n3 |4 |5 \n6 |7 |8 '

tokens = '1:\N{THUMBS UP SIGN}\n2:\N{CACTUS}'
players = 1
while True:
    player_1_name = input("Player 1, your name? ")
    player_2_name = input("Player 2, your name? ")
    # game.choose_token(1,int(input(f'\n- Player 1 -\nSelect Token:\n{tokens}\n>>> ')))
    # game.choose_token(2,int(input(f'\n- Player 2 -\nSelect Token:\n{tokens}\n>>> ')))
    player_1_token = tokenfunction
    player_2_token = tokenfunction
    player1 = Player(player_1_name, player_1_token)
    player2 = Player()
    game = Game(player1, player2)
    print(f'\n{game.__repr__()}')

    move = input(f'\n- Player {players} -\nPlace Token: >>> ')
    if move == 'exit':
        break
    if move in game.board and move not in 'XxOo':
        game.move(move, players)
    else:
        print('\n- Invalid Placement -')
        continue   
    if game.calc_winner() != None:
        print(f'\n{game.__repr__()}')
        print(f'\n- Winner: Player {game.calc_winner()} -')
    if game.is_game_over() == True:
        print('\n- Game Over -')
        game.reset_board()
        players = 1
        continue
    
    if players == 1:
        players += 1
    else:
        players -= 1


