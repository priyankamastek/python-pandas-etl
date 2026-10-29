"""
Data Quality Validation:
You receive customer data from multiple sources and need to identify invalid records.

customers = [
    {"id": 101, "name": "John", "email": "john@gmail.com"},
    {"id": 102, "name": "", "email": "alice@gmail.com"},
    {"id": 103, "name": "Bob", "email": ""}
]


"""

"""
API Processing:
extracting orders from an e-commerce API
orders = [
    {
        "order_id": 1001,
        "customer": "John",
        "items": [
            {"product": "Laptop", "qty": 1},
            {"product": "Mouse", "qty": 2}
        ]
    },
    {
        "order_id": 1002,
        "customer": "Alice",
        "items": [
            {"product": "Keyboard", "qty": 1}
        ]
    }
]

Count total items sold
"""

"""
Raw transactions
transactions = [
    {"region": "India", "amount": 500},
    {"region": "UK", "amount": 700},
    {"region": "India", "amount": 300},
    {"region": "US", "amount": 800},
    {"region": "UK", "amount": 200}
]
Aggregate revenue
"""