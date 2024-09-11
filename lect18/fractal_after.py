# Lecture 18: Using recursion to draw fractal trees
import turtle
import random

jane = turtle.Turtle()
jane.shape("turtle")
jane.width(5)
jane.color("green")
jane.speed(0)
jane.left(90)

def simpleTree(height, branch_len):
    if height == 0: # Base case: smallest possible tree
        jane.forward(branch_len)
##        jane.left(30)
##        jane.forward(branch_len)
##        jane.backward(branch_len)
##        jane.right(60)
##        jane.forward(branch_len)
##        jane.backward(branch_len)
##        jane.left(30)
        jane.backward(branch_len)
        return
    # recursive case
    jane.forward(branch_len)
    jane.left(30)
    simpleTree(height - 1, branch_len)
    jane.right(60)
    simpleTree(height - 1, branch_len)
    jane.left(30)
    jane.backward(branch_len)
    


def fancyTree(height, branch_len, width):
    if height == 0: # Base case: smallest possible tree
        jane.forward(branch_len)
        jane.backward(branch_len)
        return
    # recursive case
    branch_len = branch_len*random.randint(7, 9)/10
    if width > 2:
        width = width - 1
    jane.width(width)
    left_turn = random.randint(20, 50)
    right_turn = random.randint(20, 50)
    jane.forward(branch_len)
    jane.left(left_turn)
    fancyTree(height - 1, branch_len, width)
    jane.right(left_turn + right_turn)
    fancyTree(height - 1, branch_len, width)
    jane.left(right_turn)
    jane.backward(branch_len)
    



jane.up()
jane.backward(300)
jane.down()
fancyTree(8, 100, 8)

