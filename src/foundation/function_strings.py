# To execute the code of this file
# in project direvctory, on CMD:  uv run python -m foundation.function_string

import string

# Define the generate_email function
def generate_email(full_name):
    name_parts = []
    name_parts = full_name.split()
    print(name_parts)
    email = name_parts[0].lower() + '.' + name_parts[1].lower() + '@techcompany.com'

    # Return the email address
    return email


def validate_password(password):
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        # Check if password contains a special character
        for char in password:
            if char in string.punctuation:
                return True
    return False


# Define clean_text function with default values
# None - No value / empty

def clean_text(text, lower=True):
    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        # Apply lowercase transformation
        return clean_text.lower()

# Runs only when this file is executed directly, not when it is imported
if __name__ == "__main__":
    # Generate Email
    #full_name = "Alan Turing"

    # Call the function on the full_name string
    #print(generate_email(full_name))

    # Call the function and store the result
    #is_valid = validate_password("hgtr@8uyt")
    #print("Is the password valid? ", is_valid)
    
    product = 'Wireless Mouse'
    # Test with default behavior
    print(clean_text(text=product, lower=False))

