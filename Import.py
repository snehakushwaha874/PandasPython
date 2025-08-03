import pandas as pd

#reading data from csv file into dataframe
# df=pd.read_csv("sales_data_sample.csv", encoding="latin1")

#reading data from excel file into dataframe
#df = pd.read_excel("SampleSuperstore.xlsx")

#reading data from json file into dataframe
df = pd.read_json("sample_Data.json")
print(df)