

class PLayer:
    def __init__(self, player_name):
       self.name = player_name

    def token (self, token):
        self.token = 'X' or 'O'
        return token


class Board:
    def __init__(self):
        self.squares = [" ","X","O","X"," "," "," ", " ", " ",]
        
    
    def show_board(self):
        print(self.squares)



board = Board()
board.show_board()

    





