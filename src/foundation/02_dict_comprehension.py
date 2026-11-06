customers_raw_data = """customer_id,customer_fname,customer_lname,address,city,state,zip
11599,Mary,Malone,8708 Indian Horse Highway,Hickory,NC,28601
256,David,Rodriguez,7605 Tawny Horse Falls,Chicago,IL,60625
12111,Amber,Franco,8766 Clear Prairie Line,Santa Cruz,CA,95060
8827,Brian,Wilson,8396 High Corners,San Antonio,TX,78240
11318,Mary,Henry,3047 Silent Embers Maze,Caguas,PR,00725"""


customer_header = customers_raw_data.split("\n")[0]

# print (customer_header)

# separate the customer data
customer_data = customers_raw_data.split("\n")[1:]

# print (customer_data)

customer_dict = {}
for x in customer_data :
    customer_dict[x.split(",")[0]] = tuple(x.split(",")[1:])
    

# print (customer_dict)

# Dictionary Comprehension =  {key: value for item in iterable}

customer_dict1 = { y.split(",")[0] : tuple(y.split(",")[1:]) for y in customer_data }
# print (customer_dict1)

nested_dict = {}

# Nested  Dictionary
for key, value in customer_dict.items():
    nested_dict[key] = {
        "customer_fname" : value[0],
        "customer_lname" : value[1],
        "address" : value[2],
        "city" : value[3],
        "state": value[4],
        "pincode": value[5]
    }
    
print (nested_dict)

# to get pincode
print (nested_dict.get("11599").get("pincode"))