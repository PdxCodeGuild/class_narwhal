import math 



class Account:
    def __init__(self, running_balance = 0):
        self.running_balance = running_balance

    def balance(self):
        return self.running_balance

    
    def desposit(self,amount):
        desposit = int(amount) + self.running_balance
        return desposit


    def check_withdrawl(self,amount):
        return self.running_balance > amount


    def withdraw(self,amount):
        withdraw = int(amount) - self.running_balance 
        return withdraw


    def calc_interest(self):
        calc_interest = (self.running_balance + self.running_balance * 0.1, 2)
        return calc_interest
        
        

    #def begin_balance(self,start):
            #start = 0
            #self.begin_balance += start
            #print(begin_balance)


    #def deposit(self, balance):
            #deposit = deposit + balance
            #print(deposit)
    
    #def check_withdrawl(self,balance):
            #check_withdrawl = deposit - check_withdrawl
            #print(check_withdrawl)



atm = Account() # create an instance of our class
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