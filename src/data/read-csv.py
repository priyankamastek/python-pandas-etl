# to run : uv run -m src.data.read-csv
import pandas as pd
df = pd.read_csv('src\\data\\incoming\\orders.csv')
# print (df)
print (type(df))
print (type(df["order_date"]).__name__)
print (print(df.dtypes))