testable = {}
testable["September"] = "16C"
# You can access a value in a dictionary by its key through bracket notation.
print(testable["September"])

# However, if you try to access a key that doesnt exist youll get a keyerror exception
# print(testable["October"])

# To avoid the exception, use the get method, it returns None if a key doesnt exist.
print(testable.get("October"))

# Or you can define what the return should be:
print(testable.get("October", "No month present"))


# To remove a key value pair we can access the value through bracket notation, and use the del keyword
# del testable["September"]
# # print(testable["September"])
# print(testable.get("September"))

# If youd like to capture the removed element for some purpose such as storing it somewhere, or letting
# the user know which element was removed use pop() method. It removes the element and returns it.
popped_value = testable.pop("September")
print(popped_value)
print(testable)

# If the specified key does not exist in the object pop will return a keyerror exception, but to mitigate
# this we can pass a second argument that is returned in the case of a keyerror.
popped_value = testable.pop("September", "No temp")
print(popped_value)
print(testable)

#If you just want to pop the last inserted item from the dict use popitem() method. It doesnt take arguments
testable.update({"September": "16C"})
testable.update({"October": "12C"})
print(testable)
popped_value = testable.popitem()
print(popped_value)


# Remove all items in an object using the clear() method
testable.update({"December": "6C"})
testable.update({"March": "16C"})
testable.update({"June": "12C"})
print(testable)
print(testable.clear())
print(testable)