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
    for i, row in enumerate(board): # i is the index of row in board
       # enumerate(board) is a way of iterating through the board where in each iteration you get the elem (row) and its index (i)
       # Note we could have used range to make this work in which case the loop variable would only be the index and not the value
        print(f" {row[0]} | {row[1]} | {row[2]}")
        if i < 2 :
            print("---+---+---")

    return

board = [['X', '.', 'O'], 
         ['O', '.', '.'], 
         ['.', '.', 'X']]

        