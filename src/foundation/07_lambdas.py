# approach that offers flexibility without the need to build a complete function from scratch.

# lambda keyword - represents an anonymous function

# lambda arguments: expression

"""
Conventions:
  1.   Convention is to use x for a single arguments
  2.   The expression is the equivalent to the function body
  3.   No return statement is required
"""

# lambda average function

print (lambda x: sum(x)/ len(x))


# captialize names in the list
names = ["john", "jill", "jack"]
def capitalize_name(name):
    return name.capitalize()
capitalized = map(capitalize_name, names)
print(list(capitalized))

# lambda function with iterable
# mapmap(function, iterable) applies the function to every item in the iterable.

names = ["john", "jill", "jack"]
captialize = map(lambda x: x.capitalize(), names)


# Do Youself
# Adding extra space to file size
file_size = 2500
extra_space = 0.15
# Define a lambda function
# calculate_total = ___ x: x * (1 + ___)
# Call the lambda function
# print(___(___))



"""
colleagues = ["Sarah Martinez", "Michael Chen", "Emily Brown"]

# Apply the lambda function to each colleague's name
cleaned = ___(lambda x: x.replace(" ", "_").lower(), ____)

# Convert map object to list
cleaned_list = ____(cleaned)
print(cleaned_list)
"""






# example of Dataframes
import pandas as pd

df = pd.DataFrame({
    "salary": [10000, 20000, 30000]
})




df["salary_increase"] = df["salary"].apply(lambda x: x * 1.1)

print(df)

# create new column
df["grade"] = df["salary"].apply(
    lambda x: "High" if x > 20000 else "Low"
)

"""
# Try yourself
employees = [
    {"name": "John", "salary": 50000},
    {"name": "Alice", "salary": 70000}
]

def get_salary(emp):
    return emp["salary"]

    
sorted_employees = sorted(employees, key=get_salary)

print(sorted_employees)

# rewrite the same using lambdas

"""


















"""
employees = [
    {"name": "John", "salary": 50000},
    {"name": "Alice", "salary": 70000}
]

sorted_employees = sorted(
    employees,
    key=lambda emp: emp["salary"]
)
"""