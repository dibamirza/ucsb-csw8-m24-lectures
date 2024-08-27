# Lecture 11: Problem decomposition, while loops, while vs. for loops (zyBook 4.9 - 4.13)
# In class activity: Challenge activity: 4.12.2: Simon says.

def print_board(board):
    '''prints the board in the following format
        X | . | O 
       ---+---+---
        O | . | .  
       ---+---+---
        . | . | X 
    '''
    # Solve the fencepost problem
    for i, row in enumerate(board): # row is the loop variable and in the past it has been an int or a string
       # print(type(row)) # Debugging statement!!!!
        print(f" {row[0]} | {row[1]} | {row[2]}")
        if i < 2 :
            print("---+---+---")

    return

board = [['X', '.', 'O'], 
         ['O', '.', '.'], 
         ['.', '.', 'X']]

        