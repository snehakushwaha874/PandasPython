#head(n) - by default 5 rows, tail(n)- by default 5 rows
#does not work with float values.
import pandas as pd
df = pd.read_json("sample_Data.json")

print("Displaying first 10 rows")
print(df.head(10))

print("Displaying last 10 rows")
print(df.tail(10))

