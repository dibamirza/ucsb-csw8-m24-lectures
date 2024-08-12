# Lecture 5 Topics (zybook 2.11 - 2.13 )
# Print vs. return, developing code iteratively with functions, boolean expressions and logical operators
# Python Tutor: https://pythontutor.com/
# Print vs. return

# Problem 1: write a function that checks if a number is even
# stub of the function

def isEven(num):
    ''' returns True if the num is Even, False otherwise'''
    return num % 2 == 0 


# Problem 2: Is a number within a given range?
def is_inrange(num, min_limit, max_limit):
  ''' returns True if num is in the range [min_limit, max_limit]'''
  pass

a = 11
print(f"Is {a} between 0 and 10?", is_inrange(a, 0, 10) )


# Problem 3: Does a word contain a vowel?



# # Problem 4: Find the minimum of three numbers (related to zyLab 2.20)
def min3(x, y, z):
  '''returns minimum of x, y, z'''
  pass
  
# One approach using if-else and nested if-else statements
a = 10
b = -30
c = 5
print(f"min({a}, {b}, {c}) is:", min3(a, b, c))



# # Be careful about using logic operators in Boolean expression
# # Common errors!
# # # x less than y and z
# # # (x < y) and (z) # incorrect
# # # x < y and x < z # correct
# # x = 3
# # y = -1
# # z = 4

# # # x < (y and z) # incorrect
# # # 3 < (-1 and 4)
# # # 3 < 4
# # # True

# # Which Boolean expression answers the question:
# # Is 'a' or 'e' in word? (Note: word could be anything!)
# # A. ("a") or ("e" in word) 
# # B. ("a" in word) or ("e" in word) 
# # C. Both A and B are correct
# # print(f"Does {word} contain the letter 'a' or 'e'?")


# word = "erudite"
# # Which a Boolean expression that evaluates to true is=f word contains a vowel and false otherwise
# print(f"Does {word} contain a vowel?", has_vowel("erudite"))
# print(f"Does {word} contain a vowel?", has_vowel(word))
# # Does word contain any of "a" , "e", "i", "o", "u"
# # # Is any of the vowels (aeiou) in word

# # # Find the minimum of two numbers
# x = 10
# y = -30
# print(f"min({x}, {y}) is:", min(x, y))

