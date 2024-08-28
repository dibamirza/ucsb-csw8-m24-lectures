# Lecture 12: References and list comprehensions (zyBook 4.14 - 4.16)
# In class activity: Challenge activity: 4.14.2: List comprehensions.

# Last lecture, we coded the play() function using while loops
# Representation!!
# Board: 2D list
# Player: string (Player1 = 'X' and  Player2 = 'O')
# Current player: string 'X' or 'O'
# Move: Tuple of ints (row, col) 

# Pseudo code for the play() function 

# Initialize the board - empty board
# Select player 1 and player 2
# Select the current player
# As long as the game is not over, repeat these steps: # need to use a loop!!!!
#    Print the board to terminal
#    Ask the current player to make a move (getting input for the move)
#    Update the board with the current player's move
#    Print the status of the board after the player made the move
#    If the game resulted in a 'Win' or a 'Draw' then end the game
#    else switch to the next player

def print_board(board):
    '''prints the board in the following format
        X | . | O 
       ---+---+---
        O | . | .  
       ---+---+---
        . | . | X 
    '''
    # Solve the fencepost problem
    for i, row in enumerate(board):# i is the index of row in board
       # enumerate(board) is a way of iterating through the board where in each iteration you get the elem (row) and its index (i)
       # Note we could have used range to make this work in which case the loop variable would only be the index and not the value
        print(f" {row[0]} | {row[1]} | {row[2]}")
        if i < 2 :
            print("---+---+---")

    return

def play():
    # Initialize the board
    board = [['.'] * 3] * 3
    # print_board(board)

    # Select the current player
    current_player = 'X'

    gameover = False

    while not gameover:
        print_board(board)
        move = input(f"Enter player {current_player}'s move (row, col): ")
        # We need to eventually convert the string to a 2-tuple
        # Update the board with the current player's move
        # print_board(board)
        # status = get_status(board) # returns 'Win' , 'Draw', 'Go'
        status = 'Go' # 'Win' or 'Draw'
        if status == 'Win' or status == 'Draw':
            gameover = True
        else:
            # Switch to the next player
            if current_player == 'X':
                current_player = 'O' # Switch to player 'O'
            else:
                current_player = 'X' # Switch to player 'X'

    print("end game")
