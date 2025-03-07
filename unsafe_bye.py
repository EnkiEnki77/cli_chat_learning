# Executes module as a script even though we're just importing name. To fix this, we can use the __main__
# pattern
from unsafe_module import name

print("Bye", name)