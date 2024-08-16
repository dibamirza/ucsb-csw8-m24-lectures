## Lecture 5 - live demo
## Improve the code below using functions

# Big picture of using functions in code
# 1. Given the description of a function and asked to define the function / implement the function
# e.g. Write a function that checks if a number is prime 
# def isPrime(x):
#    ''' describe the function'''
#    Piece of logic 

# 2. Given a monolithic block of code (like the one below), use functions to make it more readable
# Use functions to improve the code

# 3. Given a complex problem (project), figure out how to decompose the problem 
# what functions you actually need to solve this larger problem

# Given this code, imporve this using functions
# input = 'John,Doe,1984,4,1,male'
# tokens = input.split(',')
# firstName = tokens[0]
# lastName = tokens[1]
# birthdate = (int(tokens[2]), int(tokens[3]), int(tokens[4]))
# isMale = (tokens[5] == 'male')
# print('Hi ' + firstName + ' ' + lastName)


## Approach 1
def print_greeting(record):
    '''input:  record is a string of the form firstname, lastname, yob, mob, dob, gender
       output: prints the greeting Hi firstname lastname
       '''
    tokens = record.split(',')
    firstName = tokens[0]
    lastName = tokens[1]
    birthdate = (int(tokens[2]), int(tokens[3]), int(tokens[4]))
    isMale = (tokens[5] == 'male')
    print('Hi ' + firstName + ' ' + lastName)

input = 'John,Doe,1984,4,1,male'
# in = input("Enter a person's record: ")
print_greeting(input)
# print(print_greeting(input)) # don't do this because the function only returns None! 

## Approach 2
# (3) Problem: Given an input string of the form firstname, lastname, yob, mob, dob, gender, print the greeting Hi firstname lastname
# Decompose into smaller sub problems that we can then solve using functions

def tokenize(record):
    '''input:  record is a string of the form firstname, lastname, yob, mob, dob, gender
       returns a tuple that is the tokenized version of record
    '''
    tokens = record.split(',')
    result = (tokens[0], tokens[1], tokens[2:4], tokens[-1])
    return result

# Step 1: Get the input string, hard code or ask the user?
input = 'John,Doe,1984,4,1,male'

# Step 2: Extract each field of the input into a tuple  (firstname, lastname, DOB, gender)
tokens = tokenize(input)

# Step 3: Print the greeting
# output = Hi John Doe
print('Hi ' + tokens[0] + ' ' + tokens[1])

