# tic tac toe game dev
# Lecture 10: Representing components of a tictactoe game in code, Lists and multability


# Last lecture you explored the following questions on your own
# Prompt: I want to develop a tic tac toe game, how should I represent the board and why?
# How do we represent a tictactoe and why?
def mutability():
    '''Explore the tradeoffs between a string vs. list representaton of a board, 2D lists, and mutability'''
    sboard = "X.O\nO..\n..X" # string representation # Strings are immulatble
    print(sboard)
    # Cannot change a particular character in the board easily if the board is a string!!!

    lboard = ['X', '.', 'O', '\n', 'O', '.', '.', '\n', '.', '.', 'X'] # possible list representation, mutable - can change specific elements
    print(lboard)
    # Write a line of code that changes the '.' in the first row of the board to an 'X'
    lboard[1] = 'X'
    print(lboard)
    lboard[6] ='X'
    print(lboard)
    #lboard[1][2] ='X' # Would it be nicer if I can index into the board this way??????

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
# I want to work on three functions related to tic tac toe game, one that prints the board, another that updates the board and one that determines whether a winning configuration was attained. Give me the stub of each function in python

def print_board_v0(board):
    '''prints the board in the following format
        X | . | O 
       ---+---+---
        O | . | .  
       ---+---+---
        . | . | X 
    '''
    for row in board: # row is the loop variable and in the past it has been an int or a string
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
    # Solve the dencepost problem
    for i, row in enumerate(board): # row is the loop variable and in the past it has been an int or a string
       # print(type(row)) # Debugging statement!!!!
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
    # Solve the dencepost problem
    separator = " | "
    divider = "---+---+---"
    for i, row in enumerate(board): # row is the loop variable and in the past it has been an int or a string
       # print(type(row)) # Debugging statement!!!!
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
#print(row)
# print(" | ".join(row))

# Try writing the stub of other functions that would be useful in the game!
def win(board):
    ''' fill in the stub'''

