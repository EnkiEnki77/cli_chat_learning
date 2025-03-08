# OOP is a programming paradigm, that revolves around objects and how the interact with each other to create
# the functionality of the program

# Objects have states and behaviors (properties and methods). Some objects may have similar characteristics,
# you can create a class which acts as a constructor for the creation of these objects with similar
# characteristics. This makes your code more DRY, because you dont have to redefine the state and behavior
# for each of the objects. Its instantiated through the class.

# Classes represent the common structure of similar objects, their data and their behavior

class MyClass:
    # class attributes defined in the class, but outside any methods. available for all instances fo the
    # class. Accessible through dot notation. class attribute values are the same for all instances.
    num = 0

    # Where you accept the arguments passed to an instantiation of the class, and define the main instance
    # attributes of the class.
    def __init__(self, num1, num2):
        # The instance attributes store data unique to each instance of a class. You can pass in arguments
        # when the class instantiated, this is where they are passed, and those arguments can be assigned
        # to instance attributes. Instance attributes are stored on the self object. Which makes them accessible
        # to the methods of the class.
        self.x = num1
        self.y = num2

    # The objects behavior, known as a method
    def add(self, a, b):
        return a + b

# Each instance of the class returns an object with the defined data and behavior's built in.
my_obj = MyClass()
my_obj.add(1, 2)
print(my_obj.num)
my_obj_2 = MyClass()
my_obj_2.add(1, 2)

