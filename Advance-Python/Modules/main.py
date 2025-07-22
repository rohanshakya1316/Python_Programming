# ‘__name__’ evaluates to the name of the module in python from where the program is ran.

# If the module is being run directly from the command line, the ‘ __name__’ is set to string “__main__”. Thus, this behaviour is used to check whether the module is run directly or imported to another file.

# main.py

# Import from our own module
import math_utils

# Import specific function and variable
from math_utils import subtract, PI

# Import from a subpackage
from greetings.hello import say_hello

print("Addition:", math_utils.add(5, 3))
print("Subtraction:", subtract(10, 4))
print("PI value:", PI)
print(say_hello("Rohan"))

print(__name__)