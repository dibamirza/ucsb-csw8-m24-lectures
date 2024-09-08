# Lecture 14: Working with files, zybook 5.8 and 5.9
# Work to complete zyLab 5.13 and 5.14.
# sentence = "Hi there"
# # Create an example text file with a message : message.txt

# Read the contents of the file in two different ways
# Open the file
myfile = open("message.txt", 'r')  # myfile is a file oject

# Read its content : one way
all = myfile.read() # all is a string that contains the content the file
word_list = all.split()
print(all)
print("There are ", len(word_list), "words in message.txt")

# Close the file
myfile.close()


# Reading from file: another way
myfile = open("message.txt", 'r')  
print(type(myfile))
for line in myfile:
  #line is a string
  print(line.rstrip()) # the loop variable line is a string
  print(line.lower())
myfile.close()

# Write a message to a file
myfile = open("new_message.txt", 'w')
myfile.write("You will learn Python! Resistance is futile!")
myfile.close()
# Count the number of words in the English Dictionary

myfile = open("words.txt", 'r')
num_words = 0
for line in myfile:
  num_words+=1

print("There are", num_words, "in the English dictionary")

myfile.close()

Filter the words in the dictionary that start with the letters "pig"
A. Very confident
B. Somewhat confident
C. Not at all

myfile = open("words.txt", 'r')

for line in myfile:
  if line[0:3].lower() == "pig":
    print(line.strip())

myfile.close()

# Learning to speak in piglatin

def indexoffirstvowel(word):
  '''return the index of the first vowel in word'''
  vowels = "aeiou"
  result = []
  for vowel in vowels:
    ind = word.find(vowel)
    if ind !=-1:
      result.append(ind)
    
  # result is a list of indices
  return min(result)


def piglatin(word):
  '''
  @param word is a string
  returns the Pig Latin equivalent of the string word
  if the word starts with a consonent, 
     move the consonent to the end of the word and add the ending 'ay'
  if the word starts with a vowel, just add the ending 'way'
  if the word starts with a cluster of consonents, 
      move the cluster to the end of the word and add the ending 'ay'
  '''
  # What is the equivalent of Pig? igpay
  # What is the equivalent of Latin? atinlay
  # What is the equivalent of it? itway
  # School -> hoolschay
  result = ""

  # great 
  if word[0].lower() not in "aeiou":
    ind = indexoffirstvowel(word)
    result = word[ind:] + word[0:ind].lower() + "ay"
  else:
    result = word + "way"
  return result

# great :  indexoffirstvowel is 2
# day : indexoffirstvowel 1

# Convert a few example sentences to piglatin
sentence = "It is a great day"
expected = "Itway isway away eatgray ayday"
print(sentence)
word_list = sentence.split()
for word in word_list:
  print(piglatin(word), end = " ")

print()
print("xylophone")
print(piglatin("xylophone"), end = " ")

# Convert all the English words that start with "ply" to piglatin and store them in a file called piglatinwords.txt

myfile = open("words.txt", 'r')

for line in myfile:
  #if line[0:3].lower() == "ply":
  print(f"{line.rstrip():15} : {piglatin(line.rstrip())}")

myfile.close()
