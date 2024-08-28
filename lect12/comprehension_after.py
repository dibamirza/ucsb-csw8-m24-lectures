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
print_board(board)
board[1][1] = 'X'
#print_board(board) # Bug was that when changing in a single cell, actually three cells got modified!!!!

# Correct way of initializing the board
# To build up the list we used the accumulator pattern
new_board = [] # initialize 
row = ['.']* 3 # ['.', '.', '.']
for i in range(3):
    new_board.append(row[:]) # Stack on a new element in the list (the element is a list !!!) row[:] ----  copy of the the list row
    
# print_board(new_board)

# new_board[1][1] = 'X'
# print_board(new_board)

# How should I use this to index into the board 
new_board[1][2] = 'O'

def convert_0():
    # Goes from move = "1, 2" to move = (1, 2)
    move = "1, 2"
    lst = move.split(",")
    print(f"lst: {lst}") # ["1", "2"]
    # Problem: convert a list of strings ["1", "2"] to a list of ints [1, 2]
    new_lst = []
    for elem in lst:
        new_lst.append(int(elem)) # elem would be "1"  Should we be appending "1" or 1
    print(new_lst)
    # Player's move is a tuple (1, 2)
    move = tuple(new_lst)

def convert_1():
  # List comprehension!!!!
  # Compact way to build a list from an existing list [expr for i in old_list]
  # This code converts the string "1, 2" to the list [1, 2]
  move = "1, 2"
  # convert a list of strings to a list of ints in one line!!
  new_lst = [int(elem) for elem in move.split(",")]

  # Note new_lst was built using list comprehension!!
  print("Old list:", move.split(","))
  print("New list: ", new_lst)
  # We can now index into the board to change it
  # row value is in move[0]
  # col value is in move[1]
  new_board[move[0]][move[1]] ='O'

def convert_2():
  # A more compact version of convert_1()
  move = "1, 2"
  print("move before:", move)
  move = tuple([int(elem) for elem in move.split(",")])
  print("move after:", move)

# Practice with accumulator pattern from lecture 8
# Problem: Return a list with only the positive numbers
def getPositive(lst):
    '''param lst is a list
       return a new list that contains only positive numbers
       in the original lst'''
    ''' lst = [ 10, 5, -2, 7, -9, 10]'''
    ''' return  [10, 5, 7, 10]'''
    # we need to build a list one element at a time -> for loop!

    result = [] # initialize result to empty list
    for elem in lst:
        if elem > 0:
            result.append(elem) # Update result
    return result


print(getPositive([ 10, 5, -2, 7, -9, 10]))
