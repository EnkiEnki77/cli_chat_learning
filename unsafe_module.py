# Whenever a module is imported it is fully executed, and then added to your current namespace.
# Even when using from to import just specific functionality the whole module is still executed.
# This makes it difficult when youd like to both import your module and execute it as a script.

# This code will be executed wherever you import this file
name = "George"

# If we want to be able to both import our module, and execute it as a script put the script code behind
# a __main__ pattern conditional, so its only executed if the script is directly run
if __name__ == "__main__":
    print("Hello,", name)