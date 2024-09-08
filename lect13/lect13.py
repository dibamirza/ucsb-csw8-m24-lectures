# Lecture 13: Dictionaries

# Creating a dictionary
invert_age = {"Ana" : 3, "Bob": 2, "Rya": 5}
person = input("Enter a name: ")
# person = "Ana"
# Given a key, get the value
if person in invert_age:
  print(f"{person} is {invert_age[person]}")
else:
  print(person, "is not in the database")
  age = int(input("Enter age to add them: "))
  invert_age[person] = age

food = ['bread', 'butter', 'jam', 'egg']
for elem in food:
  print(elem)

print("Iterating through a dictionary")
for key in invert_age:
  print(key, "is", invert_age[key])


for (key, value) in invert_age.items():
  print(key, "is", value)


# Given an age, find all the people that are older than that age
def getAllOlder(age, age_dict):
  '''
  @param age is an int
  @param age_dict is a dictionary of names and ages
  Given an age, return a list of all the people 
  that are older than that age
  '''
  result = []
  for person in age_dict:
    if age_dict[person] > age:
      result.append(person)

  return result

age = 2
invert_age = {"Ana" : 3, "Bob": 2, "Rya": 5}
x = getAllOlder(age, invert_age)
print(x)



# Check if a key is / is not  in the dictionary
print(person in invert_age) # True or False (useful when writing if statements)

# Add a new element to the dictionary
invert_age[person] = age

# Given a key, update its value in the dictionary
invert_age["Ana"] = 1

# Delete an element of the dictionary
del invert_age["Ana"] # Removes the pair Ana: 3, so the dictionary has one less element


def new_sighting(kinds, counts, sighting):
  '''
   @param kinds is a list of strings (bird names)
   @param counts is a list of the integers (count of each bird)
   @param sighting is a string (a bird that was sighted)
   Update the parallel lists kinds and counts to 
   add the new sighting
  '''
  if sighting not in kinds:
    kinds.append(sighting)
    counts.append(0) # Missing code
  ind = kinds.index(sighting)
  counts[ind] += 1


# kinds = ['falcon', 'owl', 'hawk', 'eagle']
# counts = [1, 5, 2, 11]
kinds = []
counts = []

new_sighting(kinds, counts, "owl")
# Expect to get 
# kinds = ["owl"]
# counts = [1]
print(kinds)
print(counts)



