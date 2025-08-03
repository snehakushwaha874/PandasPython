#info() - number of rows & columns, column name, data type, non null columns, memory usage of dataframe
import pandas as pd
df = pd.read_json("sample_Data.json")

print("Print displaying the info of the Dataset")
print(df.info())