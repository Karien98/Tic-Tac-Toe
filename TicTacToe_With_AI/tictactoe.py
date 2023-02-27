#Text based game with AI

board = [' ' for x in range(10)]

def insertLetter(letter, position):
    board[position] = letter

def freeSpace(position):
    return board[position] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le))

def playerMove():
    run = True
    while run:  
        move = input('Select position to place \'X\' (1-9): ')
        try:
            move  = int(move)
            if move > 0 and move < 10:  
                if freeSpace(move):#check if move is valid(not taken)
                    run = False
                    insertLetter('X', move)
                else:
                    print('Error! Slot Taken!')
            else:
                print('Selecct number within range!')
        except:
            print('Enter number!')

def aiMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]#create list of possible moves
    move = 0
    
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if winner(boardCopy, let):
                move = i
                return move

    corners = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners) > 0:
        move = selectRandom(corners)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move

    edge = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edge.append(i)
    
    if len(edge) > 0:
        move = selectRandom(edge)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def fullBoard(board):
    if board.count(' ') > 1:#since there is always one blank element on board we must use > 1
        return False
    else:
        return True


def main():
    print('Welcome to Tic Tac Toe! Give me a high, give me a low, give me 3 in a row!')
    printBoard(board)

    while not(fullBoard(board)):
        if not(winner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('O\'s the WINNER!!')
            break

        if not(winner(board, 'X')):
            move = aiMove()
            if move == 0:
                print('Tie! No more moves.')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('X\'s the WINNER!!')
            break

    if fullBoard(board):
        print('Tie! No more moves.')

while True:
    answer = input('Start Match? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('*************************************')
        main()
    else:
        break
