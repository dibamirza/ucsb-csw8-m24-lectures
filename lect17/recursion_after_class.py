# Lecture 17: More practice with recursion
def	print_num_pattern(num, step):
  '''@param num is a positive integer
     @param step is a postive integer
     prints a sequence that follows the example pattern
     print_num_pattern(12, 3) prints
     12 9 6 3 0 -3 0 3 6 9 12 
  '''
  # Base case: write the code to solve the simplest version of the problem
  # writing the code to produce the shortest valid sequence
    # if <cond for the shortest sequence>:
    #     print(num, num-step, num)
    # else:
    #     # Recursive case
    #     # print some number
    #     # call the function
    #     # print another number


def ispalindrome(word):
    '''returns True if the word is a palindrome, otherwise returns False'''
    # Base case
    if len(word) == 0 or len(word) == 1:
        return True
    # Recursive case
    if word[0] == word[-1]:
        return ispalindrome(word[1:-1]) # check that the middle part of the word is a palindrome!!! 
    else:
        return False

  
palindromes = ["civic", "kayak", "level", "madam", "mom", "noon", "racecar"]
other = ["minimum", "sardines", "cake", "eeeaowaeee"]

for word in palindromes:
  print(f"{word:12}: {ispalindrome(word)}")

for word in other:
  print(f"{word:12}: {ispalindrome(word)}")
