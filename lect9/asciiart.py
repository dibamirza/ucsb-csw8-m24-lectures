# By the end of this lecture you should be able to complete
# ZyLab 4.5 (nested loops)
# ZyLabs 4.11 and 4.12 (Accumulator pattern)

# Nested Loops, practice problems with ASCII Art
# # 1. Draw a rectangle, given its width and height
# # 2. Draw the letter C, given its width and height

# Review of the accumulator pattern

def message():
    '''What does this function return?'''
    sentence_list = ['Hello', 
                     'fellow coder!',
                     'Remember to take short breaks when coding!']
    result = ""
    for elem in sentence_list:
        result += elem + "\n"
    
    return result

# print(message())

# 1. Write a function that returns a rectangle of *'s', given its width and height

def getLine(num):
    '''returns a single row of num stars followed by a newline'''
    result = ""
    # We want the loop to run num times
    for i in range(num):
        result+='*'
    result+="\n"
    return result


def getRectangle_v0(width, height):
    '''returns a string representing a 
        rectangle of *s with given width and height'''
    result = ""
    for j in range(height):
        result+=getLine(width)
    return result

def getRectangle_v1(width, height):
    '''returns a string representing a 
        rectangle of *s with given width and height'''
    result = "" #Initialize the output
    for i in range(height):
        # We want the loop to run num times
        for j in range(width):
            result+='*'
        result+="\n"
       # print(result)
    return result


# print(getLine(3))
print(getRectangle_v1(3, 4), end = "")


# 2. Write a function that returns a string representing the letter C, given its width and height
def getC(width, height):
    '''returns a string representing the letter C 
     using *s with given width and height'''
    result = "" #Initialize the output
    for i in range(height):
        # We want the loop to run num times
        for j in range(width):
            if  i == 0 or i == (height - 1) or j == 0:
                result+='*'
            else :
                result+=' '
        result+="\n"
       # print(result)
    return result

print("Printing out a C")

print(getC(3, 4))
print(getC(10, 4))
# Let's use the AI tutor duck to understand the purpose of this nested loop
# Prompt: Explain what this code is doing.
# for i in range(2):
#    for j in range(3):
#       print(i, j)
# Prompt: Can you explain with an example how the above code can be useful to draw the letter C using stars and spaces?
