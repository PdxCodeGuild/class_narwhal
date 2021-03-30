let transactionLi = document.getElementById("transactions");
let transAmount = document.getElementById("amount");
let submitBtn = document.getElementById("submit");
let clearBtn = document.getElementById("clear");
let transTypeBtns = document.querySelectorAll('input[name="transaction"]'); 
let transaction_history = [];
let balance = 0;
let interest = 0.001;
let checkedValue;

submitBtn.addEventListener('click', function(event){
    event.preventDefault();//prevents automatic form submission
    transTypeBtns.forEach(button => {
        if(button.checked){
            checkedValue = button.value;
        }
    })
    //alert(checkedValue);// debug statement

    if(checkedValue === "Deposit"){
        balance += parseFloat(transAmount.value);
        transaction_history.push(`Deposited $${transAmount.value}`);
    }else if(checkedValue === "Withdraw"){
        if(transAmount.value > balance){
            alert("Insufficient funds!");
        }else {
            transaction_history.push(`Withdrew $${transAmount.value}`);
        }
    }else if(checkedValue === "Interest"){
        let temp = balance * interest;
        balance += temp;
        transaction_history.push(`Accumulated $${temp} in interest.`);
    }else if(checkedValue === "Balance"){
        transaction_history.push(`Deposited $${transAmount}`);
    }else if(checkedValue === "History") {
        transactionLi.innerHTML = '';
       for(let i = 0; i < transaction_history.length; ++i){
           transactionLi.innerHTML += `<li>${transaction_history[i]}</li>`;
       } 
    }
})

clearBtn.addEventListener('click', function(event){
    transactionLi.innerHTML = '';
})






// class ATM{
//     constructor(balance=0, interest=0.001, transactions=[]){
//         this.balance = balance;
//         this.interest = interest;
//         this.transactions = transactions;
//     }

//     store_transaction(amount, flag){
//         if(flag === 1){
//             this.transactions.push(`User deposited $${amount}`);
//         }
//         if(flag === 2){
//             this.transactions.push(`User withdrew $${amount}`);
//         }
//     }

//     print_transactions(){
//         alert(this.transactions);
//     }

//     get_balance() {
//         alert(`Your balance is: $${this.balance}`);
//     }

//     withdraw(amount) {
//         this.balance -= amount; 
//         return;
//     }
//     calc_interest() {
//         return this.balance * this.interest;
//     }
//     deposit(amount) {
//         this.balance += amount;
//     }
//     check_withdrawal(amount){
//         return this.balance > amount;
//     }
// }

// let command = '';
// let flag = 0;
// let atm = new ATM();
// alert("Welcome to the ATM application!");
// while(command !== 'exit'){
//     command = prompt("Enter a command (type help for list of commands): ");
//     if(command === 'deposit'){
//         let amount = parseFloat(prompt("How much would you like to deposit?"));
//         atm.deposit(amount);
//         alert(`Deposited $${amount}`);
//         flag = 1;
//         atm.store_transaction(amount, flag);
//     } else if(command === 'withdraw'){
//         let amount = parseFloat(prompt("How much would you like to withdraw?"));
//         if(atm.check_withdrawal(amount)){
//             atm.withdraw(amount);
//             alert(`Withdrew $${amount}`);
//             flag = 2;
//             atm.store_transaction(amount, flag);
//         } else {
//             alert("Insufficient funds!");
//         }
//     } else if(command === 'balance'){
//         atm.get_balance();
//         // alert(`Your balance is: $${bal}`);
//     } else if(command === 'interest'){
//         amount = atm.calc_interest();
//         atm.deposit(amount);
//         alert(`Accumulated $${amount} in interest`);
//     } else if(command === 'help'){
//         alert("Available Commands:\nbalance - displays your balance\ndeposit - deposit money\nwithdraw - withdraw money\ninterest - calculate interest\nhistory - print hisory of transactions\nexit - exit the program"
//         )
//     } else if(command === 'history'){
//         atm.print_transactions();
//     } else if(command === 'exit'){
//         choice = 'exit';
//     } else {
//         alert("Command not recognized");
//     }



// }