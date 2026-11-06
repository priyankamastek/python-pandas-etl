import string


original_price = 899.99
# Define the function with default arguments
def calculate_discount(price, discount_percent=15, round_result=True):
    discounted_price = price - (price * (discount_percent / 100))
    
    if round_result == True:
        # Round the result to two decimal places
        return round(discounted_price, 2)
    else:
        return discounted_price

# Call the function with keyword arguments
final_price = calculate_discount(price=original_price, discount_percent=25, round_result=False)
print(final_price)

# Arbitrary arguments allow functions to accept any number of argumamts
# Allow any number of positional arguments, non-keyword arguments
def average(*args):
   return sum(args) / len(args)

# * converts arguments to a single iterable tuple
# print (average (*[15, 19], *[4, 13], *[11, 8]))

# Arbitrary keyword arguments - **kwargs | kw = keyword = value
# command seperated values - print (average(a=10, b=29, c=4, e=11))
# other way - print (average(**{"a":10, "b":29, "c":4, "e":11}))
def average1(**kwargs):
    average_value = sum(kwargs.values())/ len(kwargs.values())
    rounded_average = round(average_value, 2)
    return rounded_average

# Try this
# Define a function called concat
"""
def concat(*args):
  #Concatenates multiple string arguments with spaces between them.

  result = ""

  # Iterate over the Python args tuple
  for ___ in ____:
    result += " " + arg
  return result

# Call the function
print(____("Python", "is", "great!"))
"""
"""
# Define a function called concat
def ____(____):
  # Concatenates keyword arguments into a single string with spaces.
  
  result = ""
  
  # Iterate over the Python kwargs
  for ____ in kwargs.____():
    result += " " + kwarg
  return result

# Call the function
print(____(____="Python", ____="is", ____="great!"))
"""
# Runs only when this file is executed directly, not when it is imported
if __name__ == "__main__":
    # Calling function with positional arguments
    print (average(10, 34, 67.89, 11, 8))

