'''
Lab 26
Tic Tac Toe
'''

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self):
        self.board = [[' ' for a in range(3)] for b in range(3)]

    def __repr__(self):

        layout = ''
        for line in self.board:
            layout += '|'.join(line)
            layout += '\n'
        return layout

    def move(self, x, y, player):
        if self.board[y][x] == ' ':
            self.board[y][x] = player
        else:
            print('Invalid Move')

    def calc_winner(self):
        if self.board[0][0] == self.board[1][0] == self.board[2][0] == 'X': 
            return 'Player X Wins!'
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'X':
            return 'Player X Wins!'
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'X':
            return 'Player X Wins!'
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] == 'X':
            return 'Player X Wins!'
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == 'X':
            return 'Player X Wins!'
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == 'X':
            return 'Player X Wins!'
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X':
            return 'Player X Wins!'
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] == 'X':
            return 'Player X Wins!'
        if self.board[0][0] == self.board[1][0] == self.board[2][0] == 'O': 
            return 'Player O Wins!'
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'O':
            return 'Player O Wins!'
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'O':
            return 'Player O Wins!'
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] == 'O':
            return 'Player O Wins!'
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == 'O':
            return 'Player O Wins!'
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == 'O':
            return 'Player O Wins!'
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O':
            return 'Player O Wins!'
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] == 'O':
            return 'Player O Wins!'


    def is_full(self):
        for line in self.board:
            for square in line:
                if square == ' ':
                    return False
        print('It\'s a tie!')
        return True


    def is_game_over(self):
        if self.is_full() == True:
            print(self.is_full())
            return True
        if self.calc_winner() != None:
            print(self.calc_winner())
            return True
        return False



if __name__ == "__main__":

    board = Game()

    board_dict = {'1':(0,0), '2':(1,0), '3':(2,0),
                  '4':(0,1), '5':(1,1), '6':(2,1),
                  '7':(0,2), '8':(1,2), '9':(2,2)}

    print(board)

    while True:
        player_one = 'X'
        player_two = 'O'
        
        move = input('Player One enter your move: ')
        x, y = board_dict[move]
        move = board.move(x, y, player_one)
        print(board)
        if board.is_game_over() == True:
            break
       

        move = input('Player Two enter your move: ')
        x, y = board_dict[move]
        move = board.move(x, y, player_two)
        print(board)
        if board.is_game_over() == True:
            break

    print(board.is_game_over())
