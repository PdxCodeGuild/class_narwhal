# ---- Lab 25 ---- #

# - ATM - #

# - Create a Class for the provided REPL - #

# - Version 1 - #

class ATM:
    def __init__(self):
        self.acct_balance = 0
        self.acct_interest = 0.1

    def balance(self):
        self.transactions.append(f'User checked balance: ${self.balance}')
        return self.acct_balance

    def deposit(self, amount):
        self.transactions.append(f'User deposited ${amount}')
        self.acct_balance += amount
    
    def check_withdrawal(self, amount):
        return self.acct_balance > amount

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.transactions.append(f'User withdrew ${amount}')
            self.acct_balance -= amount
            return amount
        else:
            return 'Insufficient Funds.'
    
    def calc_interest(self):
        self.transactions.append(f'User calculated interest: ${ret}')
        interest = round(self.acct_balance + self.acct_balance * self.acct_interest, 2)
        return interest

# - ATM REPL - #

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance:.2f}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawl(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')