# Lecture 3 - Division and modulo operators, Storing ordered sequences, zybook 1.18 - 1.21

# Ex. 1 Write a python program that reads in a number and determines if the number is even or odd
# print False if the number is even  
# print True if the number is odd  

# Input : number, integer 
# Output: True (if number is odd), False (if number is even)

# (5, "Is 5 odd? True")
# (24, "Is 24 odd? False")
# (127, "Is 127 odd? True")

num = int(input("Enter a number: "))
# need an expression that evaluates to True for the number 5
result = num % 2
print("Is ", num, "odd ? ", result  == 1)


# Ordered Sequences
# strings are a sequence of characters  "spam"
food = 'spam'
# Lists" ordered sequence of any type  
grocery = ['spam', 'milk', 'eggs', 'apple']

# why do we need lists?

item1 = 'spam'
item2 = 'milk'
item3 = 'eggs'
item4 = 'apple'

# The trouble with not using lists is that we need to come up with different variables to store each thing

# Index vs Value
print(food[0])
print(food[1])
print(food[-1])

# >>> food[-6]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range

# List: we can change the value of any element 
grocery[0] = 'flour'
student = ('John', 'Doe', "A384387437484")
# cannot change the individual elemens of the tuple
# student[0] = 'Diba': give us an error 


cone_snails = ["purple", "blue", "green"]
print(cone_snails[1])
print(cone_snails[1] == "orange")
cone_snails[1] = "orange"
print(cone_snails)
crab_legs = ("red",) * 10 
octapus_arms = ["purple"] * 8

