# Lecture 16: Recursion, zybook 6.1 - 6.3
# Homework: Finish CAs for 6.1 - 6.3 (at least one CA per section). Attempt zyLab 6.6 before tomorrow's lecture. 

# Review of function calling another function: defining functions vs. calling functions

# Defined function happy
def happy(message):
    print(message)

# Defined function sing
def sing(P, msg):
    # P = "Fred", msg = "Happy Birthday to you!"
    happy(msg) # call to happy
    happy(msg) # call to happy
    print("Happy Birthday dear " + P + "!")
    happy(msg) # call to happy

# main
# sing("Fred", "Happy Birthday to you!") # call to sing ! 
####################
# What is the output?

# A. Happy Birthday to you!

# B. Happy Birthday dear Fred!

# C. Happy Birthday to you!
#    Happy  Birthday to you!

# D. Happy Birthday to you!
#    Happy  Birthday to you!
#    Happy Birthday dear Fred!
#    Happy Birthday to you!

# E. Error: cannot call happy() function inside sing() function


#zybook CA 6.1.1
# Write a statement that calls the recursive function backwards_alphabet() with input starting_letter.
def backwards_alphabet(curr_letter):
    ''' f e d c b a'''
    if curr_letter == 'a':
        print(curr_letter)
    else:
        print(curr_letter)
        prev_letter = chr(ord(curr_letter) - 1)
        backwards_alphabet(prev_letter)

starting_letter = 'f'
# backwards_alphabet(starting_letter) # calling function
# backwards_alphabet('f')

## Recursion: strategy for solving problems
## Process is to describe the problem in terms of a simpler version of itself!!!
## How do we design a recursive function???!!!! 

### n! = n * (n-1)!, n > 1
###   =  1, n = 1
def fac(n):
    """
    returns the factorial of n
    """
     # Solution to for the simplest input (base case)
     # What is simplest value of the input n for which the answer is straightforward
     # Base case !!
    if n == 1:
        return 1
    
    # Recursive case !!! 
    return n * fac(n-1)

# print(f"{fac(1) = }")
# print(f"{fac(2) = }")
# print(f"{fac(3) = }")
# print(f"{fac(4) = }")





#zybook PA 6.1
def countDown(n):
    ''' print values n n-1 n-2 ... 1 Go!
        n = 3
        print 3 2 1 Go!
        5 4 3 2 1 Go!
        n = 1, output: 1 Go! (Base case)
    '''
    # Base case
    if n == 1:
        print("1 Go!")
        return

    # Recursive case!! (only think of input 2)
    # Recognize 
    print(n, end = " ")
    countDown(n-1)

# countDown(1) # 1 Go!
# countDown(2) # 2 1 Go! Solution: print 2, then call countDown(1)
# countDown(3) # 3 2 1 Go! Solution: print 3, call countDown(2)
# countDown(100)





def sumListRecursive(lst):
    ''' :param lst is a list containing integer values
        returns the sum of the elements in a list lst'''
    '''lst: [ 1, 2, 3, 5] returns 11'''
    
    # Writing the base case
    # 1. What is the simplest list that you can think of?
    # lst = [100]
    # List with 1 element, sum of all the elements would just be lst[0]

    # What about the empty list?
    # lst = []
    # What is sum of all the elements of an empty list? 
    # Base case!!! 
    if len(lst) ==0:
        return 0

    if len(lst) == 1:
        return lst[0]
  
    return lst[0] + sumListRecursive(lst[1:]) # sum of the elements of a list is the element at index 0 + sum of the elements of the rest of the list!!!!

    # Recursive case!!!
    # 2. What should the result be for the simplest list?
  
    # Write the recursive description
    # Is this a correct way of describing the solution for input [10, 20]??
    # 
    # Modify the code so that it works on any list of length 2......
    # return 42


print(f"{sumListRecursive([])=}")
print(f"{sumListRecursive([10])=}") 
print(f"{sumListRecursive([20])=}") 
print(f"{sumListRecursive([5])=}") 
print(f"{sumListRecursive([10, 20])=}") #  10 + 20 , 10 + sumListRecursive([20])
print(f"{sumListRecursive([20, 30])=}")
print(f"{sumListRecursive([10]*10)=}")



# sumListRecursive([50, 10, 20])

    

##print("sumListRecursive([]):", sumListRecursive([]))
##print("sumListRecursive([10]):", sumListRecursive([10]))
##print("sumListRecursive([100]):", sumListRecursive([100]))
##print("sumListRecursive([200]):", sumListRecursive([200]))
##print("sumListRecursive([10, 20]):", sumListRecursive([10, 20]))
## print("sumListRecursive([50, 10, 20]):", sumListRecursive([50, 10, 20]))


# Approach for an iterative solution that uses loops is quite different
def sumListIterative(lst):
    ''' :param lst is a list containing integer values
        returns the sum of the elements in a list lst'''
    '''lst: [ 1, 2, 3, 5] return 11'''
    result = 0
    for elem in lst:
        result+=elem
    return result





#zybook inclass activity
def reverseDigits( num ):
    """
    Reverse the digits of an 
    integer >0, using recursion.
    Return a string that contains
    the reversed number.
    Returns None if num < 0.
    
    num : 126
    returns: "621"
    num: 10567
    returns:"76501"
    """
    # The first two questions pertain to writing the base cases(s)
    # 1. What is/are the simplest input(s)?
    # 2. What should the answer be for the simplest input(s)?
    if num < 10 and num >=0:
        return str(num)


    # To writing the recursive case
    # Describe the solution for the given input in terms of the solution to a smaller input 

    # Recursive case

    # Get the units place of the given number
    last_digit = num % 10
    # Get the first (n-1) digits of the given number
    # Get the rest of the number after dropping the units digit
    first_n_minus1_digits = num // 10
    # '8' + reverseDigits(120950)
    return str(last_digit) + reverseDigits(first_n_minus1_digits)



# Base case !!! Simplest input(s)

# reverseDigits(9) # Output: "9"
print(f"{reverseDigits(9)=}")
print(f"{reverseDigits(7)=}")
# reverseDigits(21) # Output???? "12"


# reverseDigits(508) # Ouput??? "805"
# Find the solution for the recursive case
# reverseDigits(120950) # returns '059021'
# reverseDigits(209508) # returns '805902'
# Assume your code works for a 6 digit number!!! 
# reverseDigits(1209508) # '8059021'
                         # '8' + '059021'
                         # '8' + reverseDigits(120950)
                         # 

print(f"{reverseDigits(1209508) = }")
# Homework: Attempt zyLab 6.6 before tomorrow's lecture. Finish CAs for 6.1 - 6.3
