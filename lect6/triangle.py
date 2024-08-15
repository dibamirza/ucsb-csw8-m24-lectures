# Lecture 6
# trangle.py 
# To run this file from the console type: python triangle.py

# Questions from you!
# How do I get started?
# How do I develop a piece of logic for my function or my program ?
# How do I know my code is correct? How do I know if my code is optimal
# Python concepts - if-else , import

# To answer the above questions, we will compose the solution to the following problem using test-driven development!

# Problem: "Triangle Type Checker"
# Problem Statement:
# Write a program that determines the type of a triangle (Equilateral, Isosceles, or Scalene)  based on the lengths of its sides. 
# The program should also check whether the three sides can actually 
# form a valid triangle using the Triangle Inequality Theorem (any two sides of a triangle must be greater than the third side).


# Q1. How do I get started?
# Identify the inputs and outputs of the program
# Inputs - 3 numbers
# Output - Print to terminal one of 4 possibilities: Invalid Triangle, Equilateral, Isosceles, or Scalene

# What are the subproblems?
# sub problem 1. checking if the triangle is valid
# sub problem 2. Given a valid triangle, then figuring out the type (Equilateral, Isosceles, or Scalene)

# Write the stub of each function that would solve each of the sub-problems
# Q2: How do I figure out the logic for my function?
# Test-driven development!
# Come up with logic in small iterative steps by thinking about how we would actually test the function on different inputs

def is_valid_triangle(a, b, c):
    ''' inputs a,b,c are three floating point numbers 
        returns True if the triangle is valid, False otherwise'''
    if (a + c > b) and (b + c > a) and (a + b > c): # a = 5, b = 3, c = 1.  a + c is 6 , b = 3  # Right now it doesn't cover the case  b + c > a
        return True
    else:
        return False


def get_triangle_type(a, b, c):
    ''' inputs a,b,c are three floating point numbers that represent the lengths of the sides of a VALID triangle
        return the type of the triangle, which is a string which is one of Equilateral, Isosceles, or Scalene'''
    # Output is one of 3 possibilities (each is a value that the function returns
    if a == b and b == c: # check for all sides being equal
        return "Equilateral"
    elif a == b or b==c or c==a:   # Any two sides should be equal
        return "Isosceles"
    else:
        return "Scalene"

# print("triangle.py is ", __name__) # when we import this file (triangle.py), __name__ == "triangle" i.e.  the name of this file without the .py extension!
# On the other hand, when we run this file as the "main program", __name__ == "__main__"
# We can use this fact to conditionally execute the code below. That way when we are testing the individual functions, the program doesn't stall by waiting for user input

if __name__ == "__main__":
    x = float(input("Enter the length of the first side: "))
    y = float(input("Enter the length of the second side: "))
    z = float(input("Enter the length of the third side: "))

    if (is_valid_triangle(x, y, z) == False ):
        print("Not a valid Triangle!")
    else:
        result = get_triangle_type(x, y, z)
        print(result)






