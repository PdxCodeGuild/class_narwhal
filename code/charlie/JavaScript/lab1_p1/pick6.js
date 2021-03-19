function compareNumbers(a, b){
    return a - b;
}
function pick6(){
    let temp = [];
    for(let i = 0; i < 6; ++i){
        let num = Math.random() * 100;

        if(num >= 1){
            temp[i] = Math.floor(num);
        } else{
            temp[i] = Math.ceil(num);
        }
    }
    // console.log(temp);
    temp.sort(compareNumbers);
    // console.log(temp);
    return temp;
}

function num_matches(my_nums, win_nums, winnings){
    let matches = 0;
    
    for(let i = 0; i < 6; ++i){
        if(my_nums[i] === win_nums[i]){
            ++matches;
        }
    }

    return winnings.payout[matches];    
}

let balance = 0;
let earnings = 0;
let expenses = 0;
let winnings ={
    payout: [0, 4, 7, 100, 50000, 1000000, 25000000]
    
};
let my_nums = pick6();
let win_nums = pick6();

for(let i = 0; i < 100000; ++i){
    earnings += num_matches(my_nums, win_nums, winnings);
    balance -= 2;
    expenses += 2;
    my_nums = pick6();
    win_nums = pick6();
}

let ROI = (earnings - expenses)/expenses;
balance += earnings;
alert(`Earnings = ${earnings}`);
alert(`Your balance after 100,000 plays = ${balance}`);
alert(`Your ROI for this round = ${ROI}`);

//alert(`Here are your random numbers for the lotto6: ${my_nums}`)