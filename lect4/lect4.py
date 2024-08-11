# Lecture 5 Topics (zybook 2.11 - 2.13 )
# writing modular code with functions
# Python Tutor: https://pythontutor.com/
# Print vs. return

# DRY!: Don't Repeat Yourself!
# Problem 1: Is a number divisible by another number?
# "stub": skeleton of the function
# Defining the function




# Problem 2: Is a number within a given range?
def is_inrange(num, min_limit, max_limit):
  ''' returns True if num is in the range [min_limit, max_limit]'''
  pass


# Problem 3: Does a word contain a vowel?



# # Problem 4: Find the minimum of three numbers (related to zyLab 2.20)
def min3(x, y, z):
  '''returns minimum of x, y, z'''
  pass
  


# if _name_ == "_main_":
# One approach using if-else and nested if-else statements
a = 10
b = -30
c = 5
print(f"min({a}, {b}, {c}) is:", min3(a, b, c))



# print(f"Is {11} divisible by 3?", is_divisible(11, 3)) # calling the function
# print(f"Is {4} divisible by 3?", is_divisible(4, 3)) # calling the function



# a = 11
# print(f"Is {a} between 0 and 10?", is_inrange(a, 0, 10) )

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
# # A. ("a") or ("e" in word) # Always True because True or anythin is True
# # B. ("a" in word) or ("e" in word) # Correct
# # C. Both A and B are correct
# # print(f"Does {word} contain the letter 'a' or 'e'?")


# word = "erudite"
# # Which a Boolean expression that is true is word contains a vowel
# # false otherwise
# print(f"Does {word} contain a vowel?", has_vowel("erudite"))
# print(f"Does {word} contain a vowel?", has_vowel(word))
# # Does word contain any of "a" , "e", "i", "o", "u"
# # # Is any of the vowels (aeiou) in word

# # # Find the minimum of two numbers
# x = 10
# y = -30
# print(f"min({x}, {y}) is:", min(x, y))

# # # Work to finish on your own zybook 2.13 - 2.20
# # # zyLab 2.14: Area of a circle
# # # zyLab 2.20: min and max of 4 number
# # # SECTION GROUP ACTIVITY: zyLab 2.21: Write a program to calculate U.S. income tax owed (read the description before section)
