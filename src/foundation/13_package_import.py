# Syntax: import <package.module_name>
# Syntax: from <package.module_name> import function, class, variable

#from src.foundation.function_strings import generate_email

# from <package.module_name> import function, class
# Refer __init__.py file to use the below style of importing packages
from foundation import generate_email

if __name__ == "__main__":
    # Generate Email
    full_name = "Alan Turing"

    # Call the function on the full_name string
    print(generate_email(full_name))