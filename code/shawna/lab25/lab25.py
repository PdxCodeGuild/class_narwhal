class ATM:

    def __init__(self, act_balance = 0, interest_rate = .002):
        self.act_balance = act_balance
        self.interest_rate = interest_rate
        self.log_file = []

    def balance(self):
        return self.act_balance

    def deposit(self, amt = 0):
        self.act_balance += amt
        return amt

    def check_withdrawal(self, amt):
        return self.act_balance > amt

    def withdraw(self, amt):
        self.act_balance -= amt
        return amt
    
    def calc_interest(self):
        return round(self.act_balance * self.interest_rate, 2)

    def log(self, msg):
        self.log_file.append(msg)
    
    def print_transactions(self):
        receipt = '\n'.join(self.log_file)
        return receipt
        

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        msg = (f'Account balance is ${balance}')
        atm.log(msg)
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        msg = (f'User deposited ${amount}')
        atm.log(msg)
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            msg = (f'User withdrew ${amount}')
            atm.log(msg)
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        msg = (f'Account interest of {amount} has been added to the balance')
        atm.log(msg)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('log - print transaction log')
        print('exit     - exit the program')
    elif command == 'log':
        print( "-" * 30)
        print(atm.print_transactions())
        print( "-" * 30)
    elif command == 'exit':
        balance = atm.balance() # call the balance() method
        print(f'Thank you. Your final balance is ${balance}')
        break
    else:
        print('Command not recognized')