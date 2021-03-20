let choice = 'yes';
let total = 0;
let card = '';
alert('Let\'s play some blackjack shall we?!')

while(choice === 'yes'){

    for(let i = 0; i < 3; ++i){
        if(i === 0){
            card = prompt('What\'s your first card?');
        } else if(i === 1){
            card = prompt('What\'s your second card?');
        } else{
            card = prompt('What\'s you third card?');
        }

        if(card === 'A'){
            total += 1;
        } else if(card === 'J' || card === 'Q' || card === 'K'){
            total += 10;
        } else{
            total += parseInt(card)
        }
        console.log(total);
    }
    if(total < 17){
        alert('Hit!');
    } else if(total >= 17 && total < 21){
        alert('Stay!');
    }else if(total === 21){
        alert('Blackjack!!!!');
    } else{
        alert('Ya already busted sucka!');
    }
    choice = prompt('Would you like play again (yes/no)?');
    total = 0
}