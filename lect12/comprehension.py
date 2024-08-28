# Lecture 12: References and list comprehensions (zyBook 4.14 - 4.16)
# In class activity: Challenge activity: 4.14.2: List comprehensions.


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

board = [['.'] * 3] * 3



# # Problem: Return a list with only the positive numbers
# def getPositive(lst):
#     '''param lst is a list
#        return a new list that contains only positive numbers
#        in the original lst'''
#     '''lst = [ 10, 5, -2, 7, -9, 10]'''
#     ''' return  [10, 5, 7, 10]'''
#     # one element at a time -> for loop!
#     return [42]