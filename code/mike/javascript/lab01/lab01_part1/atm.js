/* Lab 23 ATM
class ATM:

    def __init__(self):
        self.balance = 0
        self.transactions = []

    def acct_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"user deposited ${amount}")

    def check_withdrawal(self, amount):
        return self.balance >= amount

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"user withdrew ${amount}")

    def calc_interest(self):
        interest = self.balance * .001
        return interest

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.acct_balance() # call the balance() method
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
    elif command == 'transactions':
        atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - list of transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
*/



class ATM {
    constructor(balance = 0) {
        this.balance = balance
        this.transactions = transactions   
    }
    
    acct_balance() {
        return this.balance
    }
    acct_transactions() {
        return this.transactions
    }
    deposit(amount) {
        this.balance += amount
        this.transactions.push(`\nuser deposited $${amount}`)
    }
    check_withdrawal(amount) {
        return this.balance >= amount
    }
    withdraw(amount) {
        this.balance -= amount
        this.transactions.push(`\nuser withdrew $${amount}`)
    }
    calc_interest() {
        let interest = this.balance * .001
        return interest
    }
    print_transactions() {
        for (let transaction in this.transactions){
            alert(transaction)
        }
    }
}

alert("Welcome to the ATM")

let balance = 0
let transactions = []
let atm = new ATM()
while (true){
    let command = prompt("Enter a command: ")
    if (command === 'balance'){
        let balance = atm.acct_balance()
        alert(`Your balance is $${balance}`)
    } else if (command === 'deposit'){
        let amount = parseInt(prompt("How much would you like to deposit? "))
        atm.deposit(amount)
        alert(`Deposited $${amount}`)
    } else if (command === 'withdraw'){
        let amount = parseInt(prompt("How much would you like to withdraw? "))
        if (atm.check_withdrawal(amount)){
            atm.withdraw(amount)
            alert(`Withdrew $${amount}`)
        } else {
            alert("Insufficient Funds")
        }
    } else if (command === 'interest'){
        let amount = atm.calc_interest()
        atm.deposit(amount)
        alert(`Accumulated $${amount} in interest`)
    } else if (command === 'transactions') {
        alert(atm.transactions)
    } else if (command === 'help'){
        alert('Available commands:')
        alert('balance - get the current balance')
        alert('deposit - deposit money')
        alert('withdraw - withdraw money')
        alert('interest - accumulate interest')
        alert('transactions - list of transactions')
        alert('exit - exit the program')
    } else if (command === 'exit'){
        break
    } else {
        alert("Command not recognized. Type 'help' for assistance.")
    }
}
