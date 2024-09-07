# Lecture 16: Recursion, zybook 6.1 - 6.3

def fac(n):
    """
    returns the factorial of n
    """
    pass

def sumListRecursive(lst):
    ''' :param lst is a list containing integer values
        returns the sum of the elements in a list lst'''
    '''lst: [ 1, 2, 3, 5] returns 11'''
    
    # Writing the base case
    # 1. What is the simplest input?
  
    # 2. What should the result be for the simplest input?
  
    # Write the recursive description

    return 42

# sumListRecursive([10]) 


# sumListRecursive([10, 20])


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




#zybook inclass activity 6.7
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



    # To writing the recursive case
    # Describe the solution for the given input in terms of the solution to a smaller input 

    # Recursive case


# reverseDigits(21)


# reverseDigits(508)


# reverseDigits(1209508)



#zybook 6.1
def countDown(n):
    ''' print values n n-1 n-2 ... 1 Go!
        n = 3
        print 3 2 1 Go!
    '''

    
    
