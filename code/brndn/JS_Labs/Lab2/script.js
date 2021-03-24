// JS Lab1-3 19 Mar 21
// Python Lab26 Tic-Tac-Toe

/* 
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
    valid_move(move_to) {
        this.move_to = move_to;
        let valid_moves = '012345678';
        if (valid_moves.indexOf(move_to)) {
            return this.board.indexOf(this.move_to);
        }
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
    nowinner() {
        // returns if board is full with no winners
        let full_board = 'OOOOXXXXX'
        let B = this.board.replace('\n','').replace('\n','').replace('|','').replace('|','').replace('|','').replace('|','').replace('|','').replace('|','');
        let Bsplt = B.split('');
        let Bsrt = Bsplt.sort();
        // let srtdB = Bsrtd.join('');
        // alert(Bsplt.indexOf(full_board) >= 0);
        if (Bsplt.indexOf(full_board) >= 0) {
            return true;
        } else {
            return false;
        }
    }
}

let game = new Game();
let player1 = new Player(1).token();
let player2 = new Player(2).token();

Loop: while (true) {
    // player one turn
    let player1_move = prompt(`('end' to end)\n\n${game.board}\n\nPlayer One`);
    if (player1_move == "end") {
        break Loop;
    }
    if (game.valid_move(player1_move) > -1) {
        game.move(player1, player1_move);
    }
    if (game.winner() == 1) {
        alert('Player One Wins!');
        break Loop;
    }
    if (game.nowinner() == true) {
        alert('No Winner');
        break Loop;
    }
// player two turn
    let player2_move = prompt(`('end' to end)\n\n${game.board}\n\nPlayer Two`);
    if (player2_move == "end") {
        break Loop;
    }
    game.move(player2, player2_move);
    if (game.winner() == 2) {
        alert('Player Two Wins!');
        break Loop;
    }
} */

let gameActive = true;
let currentPlayer = "X";
let gameState = ["", "", "", "", "", "", "", "", ""];

function CellPlayed(clickedCell, clickedCellIndex) {
    gameState[clickedCellIndex] = currentPlayer;
    clickedCell.innerHTML = currentPlayer;
}
function ChangePlayer() {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
}
const winCons = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];
function ResultValidation() {
    let roundWon = false;
    for (let i = 0; i <= 7; i++) {
        const winCon = winCons[i];
        let a = gameState[winCon[0]];
        let b = gameState[winCon[1]];
        let c = gameState[winCon[2]];
        if (a === '' || b === '' || c === '') {
            continue;
        }
        if (a === b && b === c) {
            roundWon = true;
            break
        }
    }
    if (roundWon) {
        gameActive = false;
        RestartGame();
        return;
    }
    let roundDraw = !gameState.includes("");
    if (roundDraw) {
        gameActive = false;
        RestartGame();
        return;
    }
    ChangePlayer();
}
function CellClick(clickedCellEvent) {
    const clickedCell = clickedCellEvent.target;
    const clickedCellIndex = parseInt(clickedCell.getAttribute('data-cell-index'));
    if (gameState[clickedCellIndex] !== "" || !gameActive) {
        return;
    }
    CellPlayed(clickedCell, clickedCellIndex);
    ResultValidation();
}
function RestartGame() {
    gameActive = true;
    currentPlayer = "X";
    gameState = ["", "", "", "", "", "", "", "", ""];
    document.querySelectorAll('.cell').forEach(cell => cell.innerHTML = "");
}

document.querySelectorAll('.cell').forEach(cell => cell.addEventListener('click', CellClick));