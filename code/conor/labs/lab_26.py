# ---- Lab 26 ---- #

# - Tic Tac Toe - #

class Player:
    def __init__(self, player_1, token):
        self.name = player_1
        self.token = token
    def __str__(self):
      return self.name

class Game:
    def __init__(self, player_1, player_2):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.player_1 = player_1
        self.player_2 = player_2

    def __repr__(self):
        display = f'''
            _{self.board[0]}_|_{self.board[1]}_|_{self.board[2]}_
            _{self.board[3]}_|_{self.board[4]}_|_{self.board[5]}_
            _{self.board[6]}_|_{self.board[7]}_|_{self.board[8]}_
        '''
        return display

    def move(self, user_num, player):
        user_num = user_num - 1
        if self.board[user_num] != ' ':
            return print('''
            Hey! No Cheating!
            ''')
        else:
            self.board[user_num] = player.token
        print(self.__repr__())

    def calc_winner(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != ' ' and self.board[1] != ' ' and self.board[2] != ' ':
            return True
        elif self.board[0] == self.board[3] == self.board[6] and self.board[0] != ' ' and self.board[3] != ' ' and self.board[6] != ' ':
            return True
        elif self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' ' and self.board[4] != ' ' and self.board[8] != ' ':
            return True
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' ' and self.board[4] != ' ' and self.board[7] != ' ':
            return True
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' ' and self.board[5] != ' ' and self.board[8] != ' ':
            return True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != ' ' and self.board[4] != ' ' and self.board[5] != ' ':
            return True
        elif self.board[6] == self.board[4] == self.board[2] and self.board[6] != ' ' and self.board[4] != ' ' and self.board[2] != ' ':
            return True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != ' ' and self.board[7] != ' ' and self.board[8] != ' ':
            return True
        else:
            return False

    def is_full(self):
        for a in self.board:
            if a == ' ':
                return False
        return True

    def is_game_over(self):
        if self.calc_winner() == True:
            print(f'''
            {current_player} won that one.
            ''')
            return True
        elif self.is_full():
            print('''
            Game board is full! Everyone\'s a loser!
            ''')
            return True
        return False

print('''
Welcome to Tic-Tac-Toe''')

while True:
    player_name = input('''
    Player 1, what is your name? ''')
    player_token = input('''Would you like 'X' or 'Y'? ''')
    player_1 = Player(player_name, player_token)

    player_name2 = input('''
    Player 2, what is your name? ''')
    player_token2 = input('''Would you like 'X' or 'Y'? ''')
    player_2 = Player(player_name2, player_token2)


    tic = Game(player_1, player_2)
    current_player = ''

    while True:
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1
        print(f"""
        Yo {current_player.name}! It's yo turn!""")
        user_num = int(input('Select a box, foo! '))
        tic.move(user_num, current_player)
        if tic.is_game_over() == True:
            break      
    again = input("""
    Ya'll wanna go again? """)
    if again == 'no':
        print('''
        Deuces''')
        break

