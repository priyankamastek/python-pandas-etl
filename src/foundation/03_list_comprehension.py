#list of tuples - (100, 300, 400) - are immutable
order_amount = [(100, 5), (200, 18), (50, 12), (500, 18), (400, 20)]
order_including_gst = [x[0] + x[0]*x[1]/100 for x in order_amount]
print (order_including_gst)

"""order_including_gst = []

for x in order_amount:
    order_including_gst.append(x[0] + x[0]*x[1]/100)

print(order_including_gst)
"""

# comprehension : List, Dictionary, set
# [expression iterable  condition]


# list comprehension - [expression for item in iterable]

order_including_gst1 = [x[0] + x[0]*x[1]/100 for x in order_amount]
print (order_including_gst1)


# Need to get only tuple
# [(100, 5, 105), (200, 18, 236), ...]
# use list comprehension

# create a nested list
# [[1,1,1], [2,4,8], [3, 9, 27]]
nested_list = []
for i in range (1, 4):
    nested_list.append([i, i**2, i**3])
    

print (nested_list)   

# do it same with list comprehension


# [1,1,1,2,4,8,3,9.27]
flattend_list = []

for sublist in nested_list:
    for item in sublist:
        flattend_list.append(item)


#print (flattend_list)


orders_list = [
    [101, '2023-07-25 00:00:00.0', 11599, 'CLOSED'],
    [102, '2023-07-25 00:00:00.0', 256, 'PENDING_PAYMENT'],
    [103, '2023-07-25 00:00:00.0', 12111, 'COMPLETE']
]

closed_orders = [ order for order in orders_list if order[3] == 'CLOSED' ]

orders = [1, "2013-07-25 00:00:00.0", 11599, "CLOSED"]
# without unpacking
order_id = orders[0]
order_date = orders[1]
customer_id = orders[2]
order_status = orders[3]

# unpacking
order_id, order_date,customer_id,order_status = orders

# enumerate
for index, element in enumerate(orders):
    print(f'Index : {index} , Element : {element}')


# count occurence of each word
input_list = ["hello", "HELLO", "I AM", "i am", "sumit"]

result_list = []

for word in input_list:
    result_list.append((word, input_list.count(word)))

print (result_list)


input_list_lower = [word.lower() for word in input_list]
print (input_list_lower)











flattend_list1 = [item  for sublist in nested_list for item in sublist]
print (flattend_list)

