from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    r1c1, r1c2, r1c3 = (board[0][0], board[0][1], board[0][2])
    r2c1, r2c2, r2c3 = (board[1][0], board[1][1], board[1][2])
    r3c1, r3c2, r3c3 = (board[2][0], board[2][1], board[2][2])
    
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {r1c1}   |   {r1c2}   |   {r1c3}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {r2c1}   |   {r2c2}   |   {r2c3}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {r3c1}   |   {r3c2}   |   {r3c3}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    move = int(input("Enter your move: "))
    
    if move in [1,2,3]:
        if board[0][move-1] not in ['O','X']:
            board[0][move-1] = 'O'
    elif move in [4,5,6]:
        if board[1][move-4] not in ['O','X']:
            board[1][move-4] = 'O'
    elif move in [7,8,9]:
        if board[2][move-7] not in ['O','X']:
            board[2][move-7] = 'O'

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_spots = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] not in ['O','X']:
                free_spots.append((row,col))
    
    return free_spots
    
def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    won = False
    
    horiz1 = [(0,0), (0,1), (0,2)]
    horiz2 = [(1,0), (1,1), (1,2)]
    horiz3 = [(2,0), (2,1), (2,2)]
    vert1 = [(0,0), (1,0), (2,0)]
    vert2 = [(0,1), (1,1), (2,1)]
    vert3 = [(0,2), (1,2), (2,2)]
    diag1 = [(2,0), (1,1), (0,2)]
    diag2 = [(0,0), (1,1), (2,2)]

    combos = [horiz1, horiz2, horiz3, vert1, vert2, vert3, diag1, diag2]
    
    for combo in combos:
        count = 0
        for point in combo:
            if board[point[0]][point[1]] == sign:
                count += 1
        if count == 3:
            won = True
            break
    
    return won
        

def draw_move(board):
    # The function draws the computer's move and updates the board.
    move = randrange(9) + 1
    if move in [1,2,3]:
        if board[0][move-1] not in ['O','X']:
            board[0][move-1] = 'X'
    elif move in [4,5,6]:
        if board[1][move-4] not in ['O','X']:
            board[1][move-4] = 'X'
    elif move in [7,8,9]:
        if board[2][move-7] not in ['O','X']:
            board[2][move-7] = 'X'
    

board = [[1,2,3],[4,'X',6],[7,8,9]]

while True:
    
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
    
    display_board(board)
    enter_move(board) # your turn
    if victory_for(board, 'O'):
        print("You win!")
        break
    
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
    
    display_board(board)
    draw_move(board) # cpu's turn
    if victory_for(board, 'X'):
        print("You lost!")
        break
