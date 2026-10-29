# copy code from comments and run on Python shell

"""
Collections: data structures used in ETL, data processing, APIs, and analytics.
These data structures are everywhere:
API responses
Spark collections
Pandas conversions
Airflow ETL tasks
JSON files
Data validation rules

List and Dictionary
============================================================================
List:
function : append(), remove(), pop()

A list stores an ordered collection of items.
cities = ["Mumbai", "London", "New York"]
print(cities[0])  # returns ?

Often work with Dynamic columns
columns = ["id", "name", "salary"]
for col in columns:
    print(col)

Running aggregations like sum, average, min, max
sales = [100, 200, 300, 400]
total_sales = sum(sales)
print(total_sales)


Collecting Invalid Records: common in ETL pipelines.
invalid_records = []

records = [
    {"id": 1, "email": "abc@gmail.com"},
    {"id": 2, "email": ""}
]

for x in records:
    if not x["email"]:
        invalid_records.append(record)

print(invalid_records)

"""
# ============================================================
"""
Dictionaries: A dictionary stores data as key-value pairs.
employee = {
    "id": 101,
    "name": "John",
    "salary": 50000
}

print(employee["name"])

JSON/API Response
response = {
    "status": "success",
    "rows_processed": 1000
}

print(response["rows_processed"])


Counting Records: 
languages = ["en", "fr", "en", "es", "en"]
counts = {}

for lang in languages:

    if lang in counts:
        counts[lang] += 1
    else:
        counts[lang] = 1

print(counts)

List of Dictionaries
Think of it as records from a database table.
employees = [
    {"id": 1, "name": "John", "salary": 50000},
    {"id": 2, "name": "Alice", "salary": 70000},
    {"id": 3, "name": "Bob", "salary": 60000}
]

for emp in employees:
    print(emp["name"])

Creating DataFrame from List of Dictionaries
import pandas as pd

employees = [
    {"id": 1, "name": "John", "salary": 50000},
    {"id": 2, "name": "Alice", "salary": 70000}
]

df = pd.DataFrame(employees)

print(df)

Dictionary of Lists
data = {
    "id": [1, 2, 3],
    "name": ["John", "Alice", "Bob"],
    "salary": [50000, 70000, 60000]
}

df = pd.DataFrame(data)

print(df)

Raw CSV
id,name,salary
1,John,50000
2,Alice,70000
3,Bob,60000

import pandas as pd
df = pd.read_csv("employees.csv")
records = df.to_dict(orient="records")
print(records)

On Run you will notice:
Entire dataset → List
Each row → Dictionary

"""