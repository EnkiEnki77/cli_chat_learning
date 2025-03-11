planets = {"Venus", "Uranus", "Jupiter", "Saturn", "Pluto", "Neptune", "Earth"}

# Allows you to create a dictionary with a list as its set of keys, you can also pass a list of its values
# otherwise they default to None.
# Keep in mind that fromKeys points to the same object in memory for every value. So if you try to mutate the
# value of one key, youre mutating it for all keys.
planets_dict = dict.fromkeys(planets, [])
satellites = ['Moon', 'Io', 'Europa']
planets_dict['Earth'].append(satellites[0])
planets_dict['Jupiter'].append(satellites[1])
planets_dict['Jupiter'].append(satellites[2])
print(planets_dict)

# To get around the memory pointer issues of fromkeys when assigning an object as value to the keys,
# use a dictionary comprehension instead. Each value will be it's own object in memory.
planets_dict_2 = {key: [] for key in planets}
planets_dict_2['Earth'].append(satellites[0])
planets_dict_2['Jupiter'].append(satellites[1])
planets_dict_2['Jupiter'].append(satellites[2])
print(planets_dict_2)


testable = {'September': '16°C', 'December': '-10°C'}
another_dictionary = {'June': '21°C'}
# The update method allows you to update a dictionaries existing keys or add new ones. You can do this
# by passing in different dictionary:
testable.update(another_dictionary)
print(testable)

# Or passing in a key value pair:
testable.update(October="32C")
print(testable)

# If a key you pass in already exists, the value will simply be updated, if it doesnt the new key/value will
# appended.
testable.update(October="42C")
print(testable)



# You can use the union operator | to merge two dictionaries. If a key exists in both the key in the right
# hand operand prevails.
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "c": 5, "d": 6}
dict_merge = dict_1 | dict_2
print(dict_merge)