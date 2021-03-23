let gameActive = true;
let currentPlayer = "X";
let gameState = [
    '','','','','','','',
    '','','','','','','',
    '','','','','','','',
    '','','','','','','',
    '','','','','','','',
    '','','','','','','',
]
function EveryNth(start, end, nth) {
    let gameSlice = gameState.slice(start,end+1);
    var winPlane = gameSlice.filter((e,i) => i % nth === 0).join('');
    console.log(winPlane);
    if (winPlane.indexOf('XXXXX') > -1) {
        return 1;
    }
    if (winPlane.indexOf('OOOOO') > -1) {
        return 2;
    }
    return 0;
}
let winCons = [
    [2,23,7],
    [1,29,7],
    [0,35,7],
    [6,41,7],
    [12,40,7],
    [18,39,7],
    [3,18,5],
    [4,24,5],
    [5,30,5],
    [11,36,5],
    [17,37,5],
    [23,38,5],
    [0,5,1],
    [6,11,1],
    [12,17,1],
    [18,23,1],
    [24,29,1],
    [30,35,1],
    [36,41,1],
    [0,36,6],
    [1,37,6],
    [2,38,6],
    [3,39,6],
    [4,40,6],
    [5,41,6],
]

function CellPlayed(clickedCell, clickedCellIndex) {
    gameState[clickedCellIndex] = currentPlayer;
    clickedCell.innerHTML = currentPlayer;
    for (let i =0; i <=23; i++) {
        let winCon = winCons[i];
        let win = EveryNth(winCon[0],winCon[1],winCon[2]);
        if (win == 1) {
            gameActive = false;
            RestartGame();
        }
        if (win == 2) {
            gameActive = false;
            RestartGame();
        }
    }
}
function CellClick(clickedCellEvent) {
    const clickedCell = clickedCellEvent.target;
    const clickedCellIndex = parseInt(clickedCell.getAttribute('data-cell-index'));
    // console.log(clickedCellIndex);
    if (gameState[clickedCellIndex] !== '' || !gameActive) {
        return;
    }
    ResultValidation();
    CellPlayed(clickedCell, clickedCellIndex);
}
function ChangePlayer() {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
}
function ResultValidation() {
    ChangePlayer();
}
function RestartGame() {
    gameActive = true;
    currentPlayer = "X";
    gameState = [
        '','','','','','','',
        '','','','','','','',
        '','','','','','','',
        '','','','','','','',
        '','','','','','','',
        '','','','','','','',
    ];
    document.querySelectorAll('.cell').forEach(cell => cell.innerHTML = "");
}
document.querySelectorAll('.cell').forEach(cell => cell.addEventListener('click', CellClick));