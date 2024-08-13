# Lecture 5 Topics (zybook 2.11 - 2.13 )
# Boolean expressions and logical operators
# Functions that answer yes/no questions
# Python Tutor: https://pythontutor.com/

# Problem 1: write a function that checks if a number is even
def isEven(num):
    ''' returns True if the num is Even, False otherwise'''
    return num % 2 == 0 


# Problem 2: Is a number within a given range?
def is_inrange(num, min_limit, max_limit):
  ''' returns True if num is in the range [min_limit, max_limit]'''
  pass

a = 11
b = 6
c = -1
print(f"Is {a} between 0 and 10?", is_inrange(a, 0, 10) )
print(f"Is {b} between 0 and 10?", is_inrange(b, 0, 10) )
print(f"Is {c} between 0 and 10?", is_inrange(c, 0, 10) )

# # x = 3
# # y = -1
# # z = 4
# # Common errors involving Boolean expressions!
# # # Which is the following Python expressions returns True when x is less than both y and z
# # # A. x < y and z 
# # # B. x < y and x < z
# # # C. Both are correct


# Problem 3: Does a word contain a vowel?


# word = "erudite"
# # Which a Boolean expression that evaluates to true is=f word contains a vowel and false otherwise
# print(f"Does {word} contain a vowel?", has_vowel("erudite"))
# print(f"Does {word} contain a vowel?", has_vowel(word))
# # Does word contain any of "a" , "e", "i", "o", "u"?


# # Which Boolean expression answers the question: 
# # Does word contain either 'a' or 'e'? (Note: assume word is a string)
# # A. "a" or "e" in word 
# # B. ("a" in word) or ("e" in word) 
# # C. Both A and B are correct
# # print(f"Does {word} contain the letter 'a' or 'e'?")

# # Problem 4: Find the minimum of two numbers (related to zyLab 2.20)


# # # Find the minimum of two numbers
# x = 10
# y = -30
# print(f"min({x}, {y}) is:", min(x, y))

