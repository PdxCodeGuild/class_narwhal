
'''
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. 
A newly created account will default to a balance of 0 and an interest rate of 0.1%. 
Implement the initializer, as well as the following functions:

balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account
'''


class ATM:
    def __init__(self, x, y):
        self.x = x
        self.y = y




'''
Version 2
Have the ATM maintain a list of transactions. 
Every time the user makes a deposit or withdrawal, 
add a string to a list saying 'user deposited $15' or 'user withdrew $15'. 
Add a new method print_transactions() to your class for printing out the list of transactions.
'''