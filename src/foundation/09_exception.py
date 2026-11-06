import csv
from datetime import datetime


def read_date(text):
    """Try each known date format; give back None if none of them fit."""
    if not isinstance(text, str):
        return None
    text = text.strip()
    # print (f'stripped text {text}')
    for date_format in ("%Y-%m-%d", "%d/%m/%Y", "%b %d %Y"):
        try:
            return datetime.strptime(text, date_format)
        except ValueError:
            print(f'{text} does not match {date_format}')
    return None


def parse_order_dates(path):
    """Load the orders file and swap order_date text for real dates."""
    orders = []
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            if not row["order_id"]:
                continue
            row["order_date"] = read_date(row["order_date"])
            orders.append(row)
    return orders


if __name__ == "__main__":
    orders = parse_order_dates("src/data/incoming/orders.csv")
    # print (orders)
    bad = []
    for order in orders:
        print(order["order_id"], order["order_date"])
        if order["order_date"] is None:
            bad.append(order["order_id"])
    print(f"\n{len(bad)} row(s) with an unreadable date: {bad}")

