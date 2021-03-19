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
        }
    }
}