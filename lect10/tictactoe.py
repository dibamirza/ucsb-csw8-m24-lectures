# tic tac toe game dev
# Lecture 10: Representing components of a tictactoe game in code, nested lists and mutability


# Last lecture we explored the following questions with the help of the AI chatbot
# Today, we'll revisit these questions and discuss it more deeply to learn about
# representing things in code using different types (strings, lists, 2D lists, etc) and the tradeoffs involved
# learning to iterate through nested (or 2D) lists in different ways, indexing, and modifying nested lists

# Prompt: I want to develop a tic-tac-toe game. How should I represent the board, and why?

def mutability():
    '''Explore the tradeoffs between a string vs. list representation of a board, 2D lists, and mutability'''
    sboard = "X.O\nO..\n..X" # string representation # Strings are immutable
    print(sboard)
    # Cannot change a particular character in the board easily if the board is a string!!!

    lboard = ['X', '.', 'O', '\n', 'O', '.', '.', '\n', '.', '.', 'X'] # possible list representation, mutable - can change specific elements
    print(lboard)
    # Write a line of code that changes the '.' in the first row of the board to an 'X'
    lboard[1] = 'X'
    print(lboard)
    lboard[6] ='X'
    print(lboard)
    #lboard[1][2] ='X' # Would it be nicer if I could index into the board this way??????

    matrix = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

    # matrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]] Same as above
    print(matrix[0]) # [1, 2, 3]
    print(matrix[1]) # [4, 5, 6]
    print(matrix[2]) # [7, 8, 9]
    print(matrix[0][2]) #
    matrix[0][2] = 10
    print(matrix)
# Prompt:
# I want to work on three functions related to the tic tac toe game: 
# one that prints the board, another that updates the board, 
# and one that determines whether a winning configuration was attained. 
# Give me the stub of each function in Python

def print_board_v0(board):
    '''prints the board in the following format
        X | . | O 
       ---+---+---
        O | . | .  
       ---+---+---
        . | . | X 
    '''
    for row in board: # row is the loop variable --in the past, loop variables have been an int or a string, 
                      # but here it (row) is a list because each element of the board is a list.
                      # To check that the type of the variable row is a list, print its type within the loop (see next statement)
       # print(type(row)) # Debugging statement!!!!
        print(f" {row[0]} | {row[1]} | {row[2]}")
        print("---+---+---")

    return

def print_board_v1(board):
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
       # Note we could have used range to make this work in which case the loop only gives the index and not the value
        print(f" {row[0]} | {row[1]} | {row[2]}")
        if i < 2 :
            print("---+---+---")

    return

def print_board(board):
    '''prints the board in the following format
        X | . | O 
       ---+---+---
        O | . | .  
       ---+---+---
        . | . | X 
    '''
    # Solve the fencepost problem
    separator = " | "
    divider = "---+---+---"
    for i, row in enumerate(board): # i is the index of row in board
       # enumerate(board) is a way of iterating through the board where in each iteration you get the elem (row) and its index (i)
       # Note we could have used range to make this work in which case the loop only gives the index and not the value
        print(f" {separator.join(row)}")
        if i < 2 :
            print(divider)

    return

board = [['X', '.', 'O'], 
         ['O', '.', '.'], 
         ['.', '.', 'X']]

# board[0][1] = 'X'
print_board(board)
row = board[0]
# print(row)
# print(" | ".join(row))


