# You can declare arguments both by name and by position

def add(num1, num2):
    return num1 + num2

# Positional arguments
print(add(1, 2))

# Named arguments
print(add(num2=1, num1=2))

# Lists all params for a function
help(add)