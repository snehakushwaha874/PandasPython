import pandas as pd
data={
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[10,20,30],
    "City":['Nagpur','Mumbai','Delhi']
}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False)
df.to_excel("output1.xlsx", index=False)
df.to_json("output2.json",index=False)