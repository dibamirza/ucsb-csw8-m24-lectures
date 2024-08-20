# # By the end of this lecture you should be able to complete zyLab 3.14
# # and complete zyLab 3.18 in three different ways

# # Programming patterns involving loops: Accumulator pattern!!!

# # Problem 1: Write your own implementation of Python's sum function
# def mysum(lst):
#     '''param lst is a list
#         returns the sum of the elements in the lst'''
#     result  = 0
#     for i in range(len(lst)):
#         result = result + lst[i]
    
#     return result

def mysum(lst):
    '''param lst is a list
        returns the sum of the elements in the lst'''
    result  = 0 # A variable that we define outside the loop
    for elem in lst: # elem is the loop variable, iterate through each of the values in the list
        result = result + elem   
    return result

l1 = [1, 5, 7]
l2 = [1, 5, 7, 10]
l3 = [1] * 10
print(f"mysum({l1}) expected: {sum(l1)}, actual = {mysum(l1)}")
print(f"mysum({l2}) expected: {sum(l2)}, actual = {mysum(l2)}")
print(f"mysum({l3}) expected: {sum(l3)}, actual = {mysum(l3)}")


# Problem 2: ZyLab 3.18:Count the number of vowels in a sentence
def countVowels0(sentence):
    '''@param sentence is a string
    returns the number of vowels in the string'''
    result = 0 # initialize outside the for loop
    for letter in sentence:
        if letter == 'a' or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            result = result + 1 # update inside the for loop

    return result # return the result !!!

def countVowels(sentence):
    '''@param sentence is a string
    returns the number of vowels in the string'''
    result = 0
    for letter in sentence:
        if letter in "aeiou":
            result = result + 1

    return result
# This code doesn't work for upper case


word1 = "apple" # number of vowels  = 2 
word2 = ""  # number of vowels = 0
word3 = "Apple"
print("lowercase A: ", word3.lower())
user_text = "Listen, Mr. Adams, calm down."

print(f"countVowels({word1}) expected: 2, actual = {countVowels(word1)}")
print(f"countVowels({word2}) expected: 0, actual = {countVowels(word2)}")
print(f"countVowels({word3}) expected: 2, actual = {countVowels(word3)}")

# # For the above user_text, your program should print 6 because there are 6 vowels


# # Problem 3. Count the number of odd numbers in a list of numbers
def countOddNumber(lst):
    '''@param lst is a list of numbers
        returns the number of odd numbers in the lst'''
    result = 0
    for elem in lst:
        if elem % 2 == 1:
            result = result + 1

    return result 



# # Problem 4: Return a list with only the positive numbers
# def getPositive(lst):
#     '''param lst is a list
#        return a new list that contains only positive numbers
#        in the original lst'''
#     '''lst = [ 10, 5, -2, 7]'''
#     ''' return  [10, 5, 7]'''
#     # one element at a time -> for loop!
#     return [42]
