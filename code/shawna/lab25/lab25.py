class ATM:

    def __init__(self, act_balance = 0, interest_rate = .002):
        self.act_balance = act_balance
        self.interest_rate = interest_rate
        self.log = []

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

    def log(self):
        
        



atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
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