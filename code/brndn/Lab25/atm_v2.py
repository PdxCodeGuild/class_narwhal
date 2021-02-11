'''
=-=-= Lab 25 10 Feb 2021 =-=-=
=-=-=-=-=- ATM V2 -=-=-=-=-=-=
=-=-=- Composer: brndn =-=-=-=
'''

class ATM:
    def __init__(self,balance=0,interest=0.1):
        self.atm_balance = balance
        self.interest = interest
        self.xaction_history = []

    def balance(self):                    #returns the account balance
        return self.atm_balance

    def deposit(self,amount):             #deposits the given amount in the account
        self.atm_balance += amount
        self.xaction_history.append(f'Deposited ${amount}')

    def check_withdrawal(self,amount):    #returns true if the withdrawn amount won't put the account in the negative
        if self.atm_balance >= amount:
            return True

    def withdraw(self,amount):            #withdraws the amount from the account and returns it
        self.atm_balance -= amount
        self.xaction_history.append(f'Withdrew ${amount}')
        return amount       

    def calc_interest(self):              #returns the amount of interest calculated on the account
        interest = self.atm_balance * self.interest
        return interest

    def print_transactions(self):
        history = '\n'.join(xaction for xaction in self.xaction_history)
        return history

atm = ATM()
print('Welcome to the ATM')
while True:
    command = input('\nEnter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'\nYour balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('\nHow much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'\nDeposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('\nHow much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'\nWithdrew ${amount}')
        else:
            print('\nInsufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'\nAccumulated ${amount} in interest')
    elif command == 'history':
        print(f'\n{atm.print_transactions()}')
    elif command == 'help':
        print('\nAvailable commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('history  - get transaction history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('\nCommand not recognized')
