
'''
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. 
A newly created account will default to a balance of 0 and an interest rate of 0.1%. 
Implement the initializer, as well as the following functions:



'''


class ATM:
    def __init__(self, initial_balance = 0):
        self.acct_balance = initial_balance
        self.history = []

    interest_rate = 0.001
    
    # balance() returns the account balance
    def balance(self):
        return self.acct_balance

    # deposit(amount) deposits the given amount in the account
    def deposit(self, amount):
        self.acct_balance = self.acct_balance + amount
        self.history.append(f'Deposited ${amount}')
        return amount

    # check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        if self.acct_balance > amount:
            return True
        else:
            return False

    # withdraw(amount) withdraws the amount from the account and returns it
    def withdraw(self, amount):
        if self.check_withdrawal(amount) == True:
            self.acct_balance = self.acct_balance - amount
            self.history.append(f'Withdrew ${amount}')
            return amount

    # calc_interest() returns the amount of interest calculated on the account
    def calc_interest(self, amount):
        interest = round(self.acct_balance * self.interest_rate, 2)
        return interest

    def print_transactions(self):
        history = '\n'.join(action for action in self.history)
        return history

    
    
        




'''
Version 2
Have the ATM maintain a list of transactions. 
Every time the user makes a deposit or withdrawal, 
add a string to a list saying 'user deposited $15' or 'user withdrew $15'. 
Add a new method print_transactions() to your class for printing out the list of transactions.
'''