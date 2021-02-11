class ATM:

    def __init__(self, bal=0):
        self.bal = bal
    # def print_transactions(self, flag, amount):
    #     transactions = []
    #     if flag == 1:
    #         transactions.append(f"user deposited ${amount}")
    #     if flag == 2:
    #         transactions.append(f"user withdrew ${amount}")

        
    def balance(self):
        return self.bal
    def withdraw(self,amount):
        self.bal -= amount
        return
    def calc_interest(self):
        interest = self.bal * 0.01
        return interest
    def deposit(self, amount):
        self.bal += amount
        return
    def check_withdrawal(self, amount):
        if self.bal - amount < 0:
            return False
        return True


atm = ATM() # create an instance of our class
transactions = []
print('Welcome to the ATM')
while True:
    command = input('Enter a command (type help for list of commands): ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':                                          ## Modify for print_transactions()
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
        transactions.append(f"user deposited ${amount}")
        #flag = 1
        #atm.print_transactions(flag, amount)
    elif command == 'withdraw':                                         ## Modify for print_transactions()
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
            transactions.append(f"user withdrew ${amount}")
            # flag = 2 
            # atm.print_transactions(flag, amount)
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == "history":
        print(transactions)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('history  - see history of transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')