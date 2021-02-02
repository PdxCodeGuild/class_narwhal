########### Lab 14 - Blackjack Advice ##############

def main():

    choice = 'yes'
    total = 0
    cards = ''
    print( 'let\'s play some Backjack shall we?!')

    while choice == 'yes':
        
        for i in range(3):
            if i == 0:
                cards = input('what\'s your first card? ')
            elif i == 1:
                cards = input('what\'s your second card? ')
            else:
                cards = input('what\'s your third card? ')

            if cards == 'A':
                total += 1
                continue
            if cards == 'J' or cards == 'Q' or cards == 'K':
                total += 10
                continue
        
            cards = int(cards)
            total += cards
            cards = str(cards)
            
        if total < 17:
            print('Hit!')
        elif total >= 17 and total < 21:
            print('Stay')
        elif total == 21:
            print('Blackjack!!!')
        else:
            print('Already busted!')
        choice = input('Would you like to play again (yes/no)? ')
        total = 0

main()