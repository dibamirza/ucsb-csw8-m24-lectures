# Lecture 4: Functions
# Lecture 4: Functions
# Make or write a function 
# Defining a function
def f(x):
    ''' describe what the function does'''
    # Write code that makes up this function
    # Any code we write here is part of the body of the function
    result = x * 2
    print(result) # Inside the function
    return result # This marks the end of the function

def dbl(x):
    '''returns double  of its input, x '''
    return 2*x
    # Code after the return statement that is "inside the function" will not be executed or run
    print(2*x)
    x = 5


# x = 2 # Outside the function
# print(2**x)
print("Hello, I am code that is outside the function")
y = "Hello"
# Call the function: using the function 
# Give it a specific input, functon will return an output
# function calls!

# If we just call the function in the program like below, the return value is not automatically printed
# Output of the function is the value that it returns! 
# We can use that value in an expression, store it in a variable or print it to output!
res1 = dbl(30) + 5  # Use it in an expression
res2 = dbl(40)
res3 = dbl(13)
res4 = dbl(y)
print( res1, res2, res3, res4)

print("dbl(21) : ", dbl(21)) # calling the function!


def meaningOfLife():
    '''returns 42'''
    return 42

print(meaningOfLife())


# Problem : write a program that checks if a number is even
# stub of the function
def isEven(num):
    ''' returns True if the num is Even, False otherwise'''
    return num % 2 == 0 


# read in a number
#x = input ("Enter a number")
x = 43
# check if its even
# print the result
print("Is", x ,"even? ", isEven(x))
print("Is", 42 ,"even? ", isEven(42))

