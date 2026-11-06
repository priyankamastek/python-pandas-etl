import csv

with open("src\\data\\incoming\\orders.csv") as f:
    for row in csv.DictReader(f):
        qty = int(row["quantity"])
        price = float(row["unit_price"])
        print(row["order_id"], qty * price)