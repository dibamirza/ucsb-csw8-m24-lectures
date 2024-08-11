
# Lecture 2 - Variables, operator = vs operator ==, sequences in Python
# This is the editor and the place we write programs

# Problem : Program that prints a personalized greeting!
user_name = input("Enter your name: ") # user_name is a variable 

''' Type your code here. '''
print("Hello" + "o" * 5, user_name, "!")
print("Did you know that light takes", 149597870700 / (3 * 10 ** 8) / 60, " mins to reach the earth!")

# Varibale is a name for a piece of data
x = 41 # x is assigned the value 41 or x stores the value 41, 41 is stored in x
y = x + 1 # what is the value stored in y ? 42 

### In Math x = 41 OR 41 = x and both work!
## 41 = x # Error

age = 41 
age_1 = 41
age_2 = 42

print(x)
x = y
print(y)
print(x)
x = z # Python is first going to look for the value of z , z was never asssigned a value and so it throws 

# Problem 1 : Write a program to calculate the time it takes for light to reach the reach from the sun
# Improved the program we wrote from lecture 1 to make it more readable.

distance_to_sun = 149597870700
speed_of_light = 3 * 10 ** 8

print("Light takes",  distance_to_sun / speed_of_light/ 60, " mins to reach the earth!")


# Problem 2 : Write a program to calculate the time it takes to travel a given distance at a given speed
# What are the inputs and what are the types of the input?
distance = int(input("Enter the distance(m): "))
speed = int(input("Enter the speed (m/s): "))

time = distance / speed # Expect distance and speed to be integers
print("The time it takes to travel", distance , " meters at ", speed, " (m/s) is : ", time)
