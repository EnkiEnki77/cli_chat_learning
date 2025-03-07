# Whenever a module is imported it is fully executed, and then added to your current namespace.
# Even when using from to import just specific functionality the whole module is still executed.
# This makes it difficult when youd like to both import your module and execute it as a script.

# This code will be executed wherever you import this file


# The convention is if youre using the __main__ pattern and your script has more than one line, put it
# all in a main function, and execute that. naming it main is just a convention to indicate its code
# only run when the file is executed as a script.
def main():
    name = "George"
    print("Hello,", name)
    x = input("What's your lucky number? ")

# If we want to be able to both import our module, and execute it as a script put the script code behind
# a __main__ pattern conditional, so its only executed if the script is directly run
# This is called the safe import option, blocking script coding from executing when imported as a module.
if __name__ == "__main__":
    main()