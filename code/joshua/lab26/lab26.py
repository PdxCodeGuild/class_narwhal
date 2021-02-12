'''
Josh Novac
Lab 26
Python
PDX Code Guild
'''


'''///////////// CLASSES /////////////'''
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self):
        self.board = [' ',' ',' '
                     ,' ',' ',' '
                     ,' ',' ',' ']

    def __repr__(self):
        board = self.board
        return f'{board[0]} | {board[1]} | {board[2]}\n{board[3]} | {board[4]} |{board[5]}\n{board[6]} | {board[7]} | {board[8]}'
    
         ## Work in progress, may change ##

        #example - board.move(x, y, player)
    '''    
    def move(self, x, y, player):
        if x == 0 and y == 0:
            i = '0'
        elif x == 1 and y == 1:
            i = '1'
        elif x == 2 and y == 2:
            i = '2'
        elif x == 3 and y == 3:
            i = '3'
        elif x == 4 and y == 4: 
            i = '4'
        elif x == 5 and y == 5:
            i = '5'
        elif x == 6 and y == 6:
            i = '6'
        elif x == 7 and y == 7:
            i = '7'
        elif x == 8 and y == 8: 
            i = '8'
        else:
            return False
        '''

    def calc_winner(self):
        #### VERTICAL WINS #### (x = horizontal position; y = veritcal position)
        ''' X|-|-  
            X|-|- 
            X|-|- '''
        if self.board[0] == 'x' and self.board[3] == 'x' and self.board[6] == 'x':
            return True
        if self.board[0] == 'y' and self.board[3] == 'y' and self.board[6] == 'x':
            return True
        ''' -|X|- 
            -|X|- 
            -|X|- '''
        if self.board[1] == 'x' and self.board[4] == 'x' and self.board[7] == 'x':
            return True
        if self.board[1] == 'y' and self.board[4] == 'y' and self.board[7] == 'y':
            return True
        ''' -|-|X 
            -|-|X 
            -|-|X '''
        if self.board[2] == 'x' and self.board[5] == 'x' and self.board[8] == 'x':
            return True
        if self.board[2] == 'y' and self.board[5] == 'y' and self.board[8] == 'y':
            return True

        #### HORIZONTAL WINS #### (x = horizontal position; y = veritcal position)
        ''' X|X|X 
            -|-|- 
            -|-|- '''
        if self.board[0] == 'x' and self.board[1] =='x' and self.board[2] == 'x':
            return True
        if self.board[0] == 'y' and self.board[1] == 'y' and self.board[2] == 'y':
            return True
        ''' -|-|- 
            X|X|X
            -|-|- '''
        if self.board[3] == 'x' and self.board[4] == 'x' and self.board[5] == 'x':
            return True
        if self.board[3] == 'y' and self.board[4] == 'y' and self.board[5] == 'y':
            return True
        ''' -|-|- 
            -|-|- 
            X|X|X '''
        if self.board[6] == 'x' and self.board[7] == 'x' and self.board[8] == 'x':
            return True
        if self.board[6] == 'y' and self.board[7] == 'y' and self.board[8] == 'y':
            return True

        #### DIAGONAL WINS #### (x = horizontal position; y = veritcal position)
        ''' X|-|- 
            -|X|- 
            -|-|X '''
        if self.board[0] == 'x' and self.board[4] == 'x' and self.board[8] == 'x':
            return True
        if self.board[0] == 'y' and self.board[4] == 'y' and self.board[8] == 'y':
            return True
        ''' -|-|X 
            -|X|- 
            X|-|- '''
        if self.board[6] == 'x' and self.board[4] == 'x' and self.board[2] == 'x':
            return True
        if self.board[6] == 'y' and self.board[4] == 'y' and self.board[2] == 'y':
            return True

    def is_full(self):
        for i in self.board:
            if ' ' not in self.board:
                return True

    def is_game_over(self):
        if self.calc_winner() == True:
            print('Game Over!')
            print(f'Thank you for playing Python Tic-Tac-Toe!')
            quit()
        elif self.is_full() == True:
            print('Tie Game!')
            print(f'Thank you for playing Python Tic-Tac-Toe!')
            quit()

'''////////////////REPL////////////////'''
def main():

    print('\nPython Tic-Tac-Toe\n')
    player_1 = Player(input('/ PLAYER ONE / - ENTER NAME: ').title(), 'X')
    player_2 = Player(input('// PLAYER TWO // - ENTER NAME: ').title(), 'O')
    print(f'\n{player_1.name}: You are X\'s')
    print(f'{player_2.name}: You are O\'s\n')

    print(f'{player_1.name} gets the first move! ')

main()