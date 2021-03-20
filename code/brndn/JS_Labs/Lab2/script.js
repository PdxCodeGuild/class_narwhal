// JS Lab1-3 19 Mar 21
// Python Lab26 Tic-Tac-Toe


class Player {
    constructor(player=0) {
        this.player = player;
    }
    token() {
        if (this.player == 1) {
            return 'X';
        } else if (this.player == 2) {
            return 'O';
        }
    }
}

// alert(player1.token());
// alert(player2.token());

class Game {
    constructor(board='0|1|2\n3|4|5\n6|7|8') {
        this.board = board;
    }
    move(piece, place) {
        // puts a 'piece' at a 'place' on the board.
        this.piece = piece;
        this.place = place;
        this.board = this.board.replace(this.place, this.piece);
    }
    winner() {
        // returns 1 for player one, 2 for player two, or 0 for none.
        let B = this.board.replace('\n','').replace('\n','').replace('|','').replace('|','').replace('|','').replace('|','').replace('|','').replace('|','');
        let wins = [`${B[0]}${B[1]}${B[2]}`,
                    `${B[3]}${B[4]}${B[5]}`,
                    `${B[6]}${B[7]}${B[8]}`,
                    `${B[0]}${B[3]}${B[6]}`,
                    `${B[1]}${B[4]}${B[7]}`,
                    `${B[2]}${B[5]}${B[8]}`,
                    `${B[0]}${B[4]}${B[8]}`,
                    `${B[2]}${B[4]}${B[6]}`];
        if (wins.indexOf('XXX') >= 0) {
            var the_winner = 1;
        } else if (wins.indexOf('OOO') >= 0) {
            var the_winner = 2;
        } else {
            var the_winner = 0;
        }
        return the_winner;
    }
}

let game = new Game();
let player1 = new Player(1).token();
let player2 = new Player(2).token();

Loop: while (true) {

    let player1_move = prompt(`('end' to end)\n\n${game.board}\n\nPlayer One`);
    if (player1_move == "end") {
        break Loop;
    }
    game.move(player1, player1_move);
    if (game.winner() == 1) {
        alert('Player One Wins!');
        break Loop;
    }
    let player2_move = prompt(`('end' to end)\n\n${game.board}\n\nPlayer Two`);
    if (player2_move == "end") {
        break Loop;
    }
    game.move(player2, player2_move);
    if (game.winner() == 2) {
        alert('Player Two Wins!');
        break Loop;
    }
}