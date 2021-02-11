'''
Josh Novac
Lab 25
Python
PDX Code Guild
'''

'''////////////////////////////////////////// INSTRUCTIONS //////////////////////////////////////////
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. 
A newly created account will default to a balance of 0 and an interest rate of 0.1%. 
Implement the initializer, as well as the following functions:
-----------------------------------------------------------------------------------------------
- balance() -- returns the account balance
- deposit(amount) -- deposits the given amount in the account
- check_withdrawal(amount) -- returns true if the withdrawn amount won't put the account in the negative
- withdraw(amount) -- withdraws the amount from the account and returns it
- calc_interest() -- returns the amount of interest calculated on the account
'''

'''////////////////// CLASS & FUNCTIONS //////////////////'''
## create an instance of our class; call the balance() method
class ATM:
    def __init__(self, balance = 0):
        self.__balance = balance
        self.__transactions= []

    ## call the balance() method
    def balance(self):
        return self.__balance

    ## call the deposit(amount) method
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        self.__transactions.append(f"Deposited ${amount}: Current balance ${self.__balance}")

    ## call the withdraw(amount) method
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        self.__transactions.append(f"Withdrew ${amount}: Current balance ${self.__balance}")

    ## call the check_withdrawal(amount) method
    def check_withdrawal(self, amount):
        if self.__balance >= amount:
            return True
        else:
            return False

    ## call the calc_interest() method
    def calc_interest(self):
        accumulate = self.__balance * 0.001
        return accumulate
        self.__transactions.append(f"Interest Accumulated ${amount}: Current balance ${self.__balance}")

    ## call transaction log
    def recent(self, note):
        self.__transactions.append(note)

    ## Add a new method print_transactions() printing out the list of transactions.
    def print_transactions(self):
        recent_transactions = '\n'.join(self.__transactions)
        return recent_transactions

'''/////////////////////////REPL/////////////////////////'''
atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('\nType \'help\' to list commands\nEnter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        note = (f'Current Balance is: ${balance}')
        print(f'\nYour balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? $'))
        atm.deposit(amount) # call the deposit(amount) method
        note = (f'You deposited: ${amount}')
        print(f'\nDeposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw? $'))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            note = (f'You withdrew: ${amount}')
            print(f'\nWithdrew ${amount}')
        else:
            print(str(f'\nInsufficient funds; cannot withdraw amount of ${amount}'))
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'recent':
        print(f'\n\tRECENT TRANSACTIONS\n-----------------------------------\n')
        print(atm.print_transactions())
        print('\n-----------------------------------\n')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('recent   - see recent transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        print('\nThank you for using Python ATM!')
        print(f'\n\t\tRECEIPT\n----------------------------------------\n')
        print(atm.print_transactions())
        print('\n----------------------------------------')
        print('\u00A9 2021 Python ATM, Inc')
        break
    else:
        print('Command not recognized')