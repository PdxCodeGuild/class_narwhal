class Game:

    def __init__(self):
        board = [[ '' for col in range(0,3)] for row in range(0,3)]

    
    def move(self, x, y, player):
        pass

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
    name1 = input("Player 1 please enter your name: ")
    token1 = input(f"{name1} Please choose whether you would like to be X's or O's (type X or O)")
    name2 = input("Player 2 please enter your name: ")
    if token1 == 'X': 
        token2 = 'O'
    else:
        token2 = 'X'
    player1 = Player(name1, token1)
    player2 = Player(name2, token2)
    choice = ''

    while choice != 'exit':
        if choice == 'move':
            pass
        elif choice == '':
            pass

main()