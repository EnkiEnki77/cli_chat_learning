# pip list allows you to see all your packages installed
# pip show some_package allows you to see info about a package
# pip list -o shows outdated packages along with your current and their latest versions
# pip uninstall some_package to to remove a package from your computer

# When developing your program its advantageous to keep required packages for the project (dependencies)
# in a requirements file. pip install -r requirements.txt allows you to install all the dependies of the
# project that are listed in requirement.txt
# To add all the packages you have installed to requirements.txt run pip freeze > requirements.txt

import scipy

print(scipy.sparse.csgraph.csgraph_from_dense(6))