import random

current_player = "X"
free_field = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
def switch_user():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player= "X"
        
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+---+---+---+")
    for row in range(3):
        print("| ", end = "")
        for col in range(3):
            print(board[row][col], end = " | ")
        print("\n+---+---+---+")

    # print(free_field)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    move = int(input("Enter your move: "))
    global current_player
    global free_field
    
    if free_field[move-1] != "X" or free_field[move-1] != "O":
        board[free_field[move-1][0]][free_field[move-1][1]] = current_player
        free_field[move-1] = current_player


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == sign:
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return board[0][2]

    global free_field
    # for item in free_field:
    #     if item != X

    return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        move = random.randint(1, 9)
        global current_player
        global free_field
        
        draw = True
        for item in free_field:
            if item !="X" and item !="O":
                draw = False
                break

        if draw:
            print("MATCH DRAW")
            exit(0)


        if (free_field[move-1] != 'X') and  (free_field[move-1] != "O"):
            print("Computer's move: ", move)
            board[free_field[move-1][0]][free_field[move-1][1]] = current_player
            free_field[move-1] = current_player
            break


board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

display_board(board)
print("\n--------------------------------------------------------------")
while True:
    enter_move(board)
    display_board(board)
    victor = victory_for(board, current_player)
    if victor != None:
        print(victor, " Wins!")
        break
    switch_user()
    print("\n--------------------------------------------------------------")
    draw_move(board)
    display_board(board)
    victor = victory_for(board, current_player)
    if victor != None:
        print(victor, " Wins!")
        break
    switch_user()
    print("\n--------------------------------------------------------------")