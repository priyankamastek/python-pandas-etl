# Error - code when violates a rule, error is raised by python
# Error - also called as exception

# TypeError: Incompatible data type
# "Hello" + 5

# ValueError: Value is not within an acceptable range
# float("Hello")
# float("2")

# Error -  code in package
# package contain other people code e.g. custom functions
# pip install <package>
# the pandas 'pd.read_csv()' function executes the code written for that custom function behind the scene

"""
import pandas as pd
products = pd.DataFrame({"ID":"ABC1", "price": 29.99})
products["tag"]
"""

"""
def clean_text(text):
  # Attempt to clean the text
  try:
    return text.replace(" ", "_").lower()
  # Run this code if an error occurs
  expect:
    print("The clean_text() function expects a string as an argument, please check the data type provided!")
    
clean_text(187)
"""
"""
def clean_text(text):
  # Check the data type
  if ___(text) == ___:
    return text.replace(" ", "_").lower()
  else:
    # Return a TypeError error if the wrong data type was used
     ____("The clean_text() function expects a string as an argument, please check the data type provided!")
    
clean_text("User Name 187")
"""