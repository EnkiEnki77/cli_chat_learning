# A script is a module meant for direct execution. The difference between a module and script
# is how theyre used. Modules are loaded from other modules or scripts, scripts are executed directly.

# So if run this file directly here it's a script. But if import it to another file and run it there
# its a module.
print("Hello world!")

# Imported my local module
import module_to_import
module_to_import.greet(module_to_import.name, module_to_import.l_name)

# Be careful not to shadow the name of builtin modules with your local modules. Such as having a local
# module called math. This will cause errors if you try to utilize the builtin. Suffix _script to your
# modules to avoid this name shadowing problem.

