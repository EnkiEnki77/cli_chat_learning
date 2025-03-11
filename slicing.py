array = [1, 2, 3, 4, 5, 6]
start = 1
end = 5
step = 2

# The slice operator allows you to copy a section of an array. This is the syntax:
syntax = array[start:end:step]
# print(syntax)

# Start is the index of the first element included
# End is the index of the end of the slice (exclusive)
# Step determines whether items are skipped, and what the pattern is

# Defines starting index and goes to the end of the array
no_end = array[start:]
print(no_end)
# Defines starting index and goes to the end of the array, stepping by 2
no_end_stepped = array[start::step]
print(no_end_stepped)

# Defines ending index and goes from the start of the array
no_start = array[:end]
print(no_start)
# Defines ending index and goes from the start of the array, stepping by 2
no_start_stepped = array[:end:step]
print(no_start_stepped)

# Copies the whole array
whole_array = array[:]
print(whole_array)
# Copies the whole array, stepped by 2
whole_array_stepped = array[::step]
print(whole_array_stepped)
