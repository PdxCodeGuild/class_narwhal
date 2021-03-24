let card1 = document.getElementById("card1");
let card2 = document.getElementById("card2");
let card3 = document.getElementById("card3");
let resultLi = document.getElementById("result");
let adviceBtn = document.getElementById("advice");
let clearBtn = document.getElementById("clear")





adviceBtn.addEventListener('click', function(event) {
    let result = parseInt(card1.value) + parseInt(card2.value) + parseInt(card3.value);

    if(result <= 17){
        resultLi.innerHTML = "Hit!";
    } else if(result >=17 && result <= 21){
        resultLi.innerHTML = "Stay!";
    } else {
        resultLi.innerHTML = "Busted!";
    }
})

clearBtn.addEventListener('click', function(event) {
    resultLi.innerHTML = " ";
})


// let choice = 'yes';
// let total = 0;
// let card = '';
// alert('Let\'s play some blackjack shall we?!')

// while(choice === 'yes'){

//     for(let i = 0; i < 3; ++i){
//         if(i === 0){
//             card = prompt('What\'s your first card?');
//         } else if(i === 1){
//             card = prompt('What\'s your second card?');
//         } else{
//             card = prompt('What\'s you third card?');
//         }

//         if(card === 'A'){
//             total += 1;
//         } else if(card === 'J' || card === 'Q' || card === 'K'){
//             total += 10;
//         } else{
//             total += parseInt(card)
//         }
//         console.log(total);
//     }
//     if(total < 17){
//         alert('Hit!');
//     } else if(total >= 17 && total < 21){
//         alert('Stay!');
//     }else if(total === 21){
//         alert('Blackjack!!!!');
//     } else{
//         alert('Ya already busted sucka!');
//     }
//     choice = prompt('Would you like play again (yes/no)?');
//     total = 0
// }