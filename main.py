# A script is a file containing operations, that can be read and executed by an interpretor later on

# A module is a file that contains python statments and functions and ends with .py that can be
# imported into other files/modules

# Import a module using the import keyword. In order for a module to be importable, it needs to exist in
# the same directory as the file importing it.
# First, import looks for a module in the directory of this file, then in the builtins, then it raises an
# error
import super_module

# You can then utilize a modules methods and properties
super_module.super_function()
print(super_module.super_variable)

# You can also choose to load modules resources directly, instead of the whole module itself
from super_module import super_function
super_function()

# You can also use the wildcard, to import all names in a module. This should generally be avoided though
# because you wont know whats being imported and whether names are conflicting with what you already have
# Its better to be explicit about what youre importing
from super_module import *
print(super_variable)


# Guidelines for how you should order your imports:
# 1. standard library imports first
# 2. then third party imports
# 3. imports from other files in your project

# You should also separate the 3 groups by a line, and order them alphabetically.