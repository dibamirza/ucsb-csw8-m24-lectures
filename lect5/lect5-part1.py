# Lecture 5: part 1

## Print vs. return
def f(x):
   return x*2

def g(x):
   print(x*2)


## Q2
def add(x, y):
    return x + y

result = add(5, 7) 
print(f'add(5, 7) is {result}')
result = add('Tora', 'Bora')
print(f"add('Tora', 'Bora') is {result}")
