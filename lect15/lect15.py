# Lecture 15: Data representation, 5.11 - 5.12

message = "HOWALIVE"
for e in message:
    print(f"{ord(e):x}", end = " ")

print()
# ord(e): give us the ASCII value of that character
# What is the ASCII value that the letter 'H' correspond to? 48

num = 0x10A
print(num)
print(f"{num:b}")

num = 0x48
print(f"{num:b}")
