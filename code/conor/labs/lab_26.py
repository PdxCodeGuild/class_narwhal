# ---- Lab 26 ---- #

# - Tic Tac Toe - #

class Player:
    def __init__(self, name, token):
        self.name = player_name
        self.token = token

class Game:
    def __init__(self):
        self.board = ['', '', '', '', '', '', '', '', '']
        print(self.board[2])
    def __repr__(self):
        display = f"_{self.board[0]}_|_{self.board[1]}_|_{self.board[2]}_" + '\n' + f"_{self.board[3]}_|_{self.board[4]}_|_{self.board[5]}_" + '\n' + f"_{self.board[6]}_|_{self.board[7]}_|_{self.board[8]}_"  
        return display

    def move(self, user_num, player):
        user_num = user_num - 1:
            self.board[user_num] = player.token
    
    def calc_winner(self):
        if self.board[0] == self.board[1] == self.board[2]:
            return 'Winner!'
        elif self.board[0] == self.board[3] == self.board[6]:
            return 'Winner!'
        elif self.board[0] == self.board[4] == self.board[8]:
            return 'Winner!'
        elif self.board[1] == self.board[4] == self.board[7]:
            return 'Winner!'
        elif self.board[2] == self.board[5] == self.board[8]:
            return 'Winner!'
        elif self.board[3] == self.board[4] == self.board[5]:
            return 'Winner!'
        elif self.board[6] == self.board[4] == self.board[2]:
            return 'Winner!'
        elif self.board[6] == self.board[7] == self.board[8]:
            return 'Winner!'

    def is_full(self):
        for a in self.board:
            if a == '':
                return False
        return True

    def is_game_over(self):
        return self.calc_winner() or self.is_full()



# print('Welcome to Tic-Tac-Toe')


player_1_name = Player(input("What is Player 1's name? "))
Player_2_name = Player(input("What is Player 2's name? "))

