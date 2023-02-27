#Text based game with AI

#create board, use a grid system to represent the board
#will store X's and O's for the program
#populate board with 4x in range 10
#doing 10 instead of 9, want to have 1 leading space in list
board = [' ' for x in range(10)]

#insert letter into board list at given position
#takes 2 parameters
def insertLetter(letter, position):
    board[position] = letter

#tells if given space is free
#returns true or false value
def freeSpace(position):
    return board[position] == ' '

#displays board to the console
#"board" is a list of 10 strings representing the board (ignore index 0)
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

#tells if given letter has won based on current board
#letter must be X or O
#given a board and a player’s letter, this function returns True if that player has won.
# We use bo instead of board and le instead of letter so we don’t have to type as much.
def winner(bo, le):
            #across the top                                  #across the middle                              #across the bottom                              #down left side                                 #down the middle                                #down right side                                #diagonal                                       #diagonal
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le))

#input move and validating it
def playerMove():
    run = True
    while run:  #keep looping until we get a valid move
        move = input('Select position to place \'X\' (1-9): ')
        try:
            move  = int(move)
            if move > 0 and move < 10:  #makes sure it's a number between 1-9
                if freeSpace(move):  #check if move is valid(not taken)
                    run = False
                    insertLetter('X', move)
                else:
                    print('Error! Slot Taken!')
            else:
                print('Selecct number within range!')
        except:
            print('Enter number!')

#examine and determine which move to make
    #If the current step cannot be completed proceed to the next.
        #1.If there is a winning move take it.
        #2.If the player has a possible winning move on their next turn move into that position.
        #3.Take any one of the corners. If more than one is available randomly decide.
        #4.Take the center position.
        #5.Take one of the edges. If more than one is available randomly decide.
        #6.If no move is possible the game is a tie.
def aiMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] #create list of possible moves
    move = 0
    
    #check for possible winning move to take or to block opponents winning move
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if winner(boardCopy, let):
                move = i
                return move

    #try to take one of the corners
    corners = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners) > 0:
        move = selectRandom(corners)
        return move
    
    #try to take the center
    if 5 in possibleMoves:
        move = 5
        return move

    #take any edge
    edge = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edge.append(i)
    
    if len(edge) > 0:
        move = selectRandom(edge)

    return move

#randomly decide on a move to take given a list of possible positions
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

#will return True if board is full and False if it is not
def fullBoard(board):
    if board.count(' ') > 1:  #since there is always one blank element on board we must use > 1
        return False
    else:
        return True

#call to start the game
def main():
    #main game loop
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