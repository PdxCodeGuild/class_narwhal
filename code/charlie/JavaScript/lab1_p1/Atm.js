class ATM{
    constructor(balance=0, interest=0.001){
        this.balance = balance;
        this.interest = interest;
    }

    balance() {
        return this.balance;
    }

    withdraw(amount) {
        this.balance -= amount; 
        return;
    }
    calc_interest() {
        return this.balance * this.interest;
    }
    deposit(amount) {
        this.balance += amount;
    }
    check_withdrawal(amount){
        return this.balance > amount;
    }
}

let atm = new ATM();