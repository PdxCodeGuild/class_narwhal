# Tic Tac Toe
# Richard Farr 
# Adapted from a book I bought a few years back and did not read
# Non Object Oriented Approach
# Will use later to help do the same thing but in an OOJ approach

import random

def drawBoard(board):
    # Print out a board
    print(board[7] + '|' + board[8] + '|' + board[9] )
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6] )
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3] )

def inputPlayerLetter():
    # Lets player choose either X or O
    # Player is first item in list & computer is 2nd item
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to be X or O? ")
        letter = input().upper()

        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
        
def whoGoesFirst():
    # Randomly pick which player goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a players letter, this will return True if the player has won
    # bo means board, le means letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom

    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right

    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagnol
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagnol

def getBoardCopy(board):
    # Make a copy of the board and return it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # return true if the space is empty
    return board[move] == " "

def getPlayerMove(board):
    # Let the player enter their move
    move = " "
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1 - 9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # returns a valid move given the current board
    # returns None if there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and a computer letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Below are the steps to control the playing logic of the computer

    # 1. Check if its possible to win in the next move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # 2. Check if the other player could win on the next move and block them
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # 3. Try to take one of the corners, if one is open
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # 4. Try to take the center
    if isSpaceFree(board, 5):
        return 5

    # 5. Move one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # return True if every space on the board that has been taken, otherwise return False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("Welcome to Tic-Tac-Toe!")

while True:
    # Reset the board
    theBoard = [" "] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The " + turn + " will go first.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Players Turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Well done, You won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'computer'

        else:
            # Computers Turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The computer has beaten you, you lose.")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
