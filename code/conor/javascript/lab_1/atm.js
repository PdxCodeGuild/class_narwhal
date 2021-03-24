// Python Lab 25

// ATM

// Version 1

// class ATM {
//     constructor(balance = 0) {
//         this.balance = balance
//         this.interest = 0.1
//         this.transactions = transactions   
//     }
    
//     acct_balance() {
//         return this.balance
//     }

//     acct_transactions() {
//         return this.transactions
//     }

//     deposit(amount) {
//         this.balance += amount
//         this.transactions.push(`Deposited $${amount}`)
//     }

//     check_withdrawal(amount) {
//         return this.balance >= amount
//     }

//     withdraw(amount) {
//         this.balance -= amount
//         this.transactions.push(`Withdrew $${amount}`)
//     }

//     calc_interest() {
//         let interest = this.balance * this.interest
//         return interest
//     }
    
//     print_transactions() {
//         for (let transaction in this.transactions){
//             alert(transaction)
//         }
//     }
// }

// alert("Welcome to the ATM")

// let balance = 0
// let transactions = []
// let atm = new ATM()

// while (true){

//     let command = prompt("What would you like to do today: ")

//     if (command === 'balance'){
//         let balance = atm.acct_balance()
//         alert(`Your balance is $${balance}`)

//     } else if (command === 'deposit'){
//         let amount = parseInt(prompt("How much are you depositing? "))
//         atm.deposit(amount)
//         alert(`Deposited $${amount}`)

//     } else if (command === 'withdraw'){
//         let amount = parseInt(prompt("How much do you want? "))
//         if (atm.check_withdrawal(amount)){
//             atm.withdraw(amount)
//             alert(`You withdrew $${amount}`)

//         } else {
//             alert("You're too broke for that")
//         }

//     } else if (command === 'interest'){
//         let amount = atm.calc_interest()
//         atm.deposit(amount)
//         alert(`You have accumulated $${amount} in interest`)

//     } else if (command === 'transactions') {
//         alert(atm.transactions)

//     } else if (command === 'help'){
//         alert('Available commands:')
//         alert('balance - get the current balance')
//         alert('deposit - deposit money')
//         alert('withdraw - withdraw miney')
//         alert('interest - accumulated interest')
//         alert('transactions - print transaction history')
//         alert('exit - exit the program')

//     } else if (command === 'exit'){
//         alert('Goodbye!')
//         break

//     } else {
//         alert("Command not recognized. Type 'help' for assistance.")
//     }
// }

// Version 2

class ATM {
    constructor(balance = 0) {
        this.balance = balance
        this.interest = 0.1
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
        this.transactions.push(`Deposited $${amount}`)
    }

    check_withdrawal(amount) {
        return this.balance >= amount
    }

    withdraw(amount) {
        this.balance -= amount
        this.transactions.push(`Withdrew $${amount}`)
    }

    calc_interest() {
        let interest = this.balance * this.interest
        return interest
    }
    
    print_transactions() {
        for (let transaction in this.transactions){
            results.textContent = transaction
        }
    }
}


let balanceButton = document.getElementById("balancebutton")
let depositButton = document.getElementById("depositButton")
let withdrawalButton = document.getElementById("withdrawalButton")
let interestButton = document.getElementById("interestButton")
let transactionsButton = document.getElementById("transactionsButton")
let results = document.getElementById("results")

let balance = 0
let transactions = []
let atm = new ATM()

balanceButton.addEventListener("click", function(){
    let balance = atm.acct_balance();
    results.innerText = `Your balance is $${balance}`;
})

depositButton.addEventListener("click", function(event){
    let amount = parseInt(prompt("How much are you depositing? "));
    atm.deposit(amount);
    results.innerText = `Deposited $${amount}`;
})

withdrawalButton.addEventListener("click", function(){
    let amount = parseInt(prompt("How much would you like to withdraw? "));
    if (atm.check_withdrawal(amount)){
        atm.withdraw(amount);
        results.innerText = `You withdrew $${amount}`;
    } else {
        results.innerText = "You too broke for that, homie";
    }
})

interestButton.addEventListener("click", function(){
    let amount = atm.calc_interest();
    atm.deposit(amount);
    results.innerText = `You've recieved $${amount} in interest`;
})

transactionsButton.addEventListener("click", function(){
    results.innerText = atm.transactions;
})