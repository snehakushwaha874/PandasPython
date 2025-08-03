import pandas as pd
data={
    "Name":['Ram','Shyam','Ghanshyam','Karan','Varun'],
    "Age":[28,34,22,34,28],
    "Salary":[50000,60000,45000,52000,48000]
}
df=pd.DataFrame(data)

#grouping age column and calculating salary of each age group
group = df.groupby("Age")["Salary"].sum()
print(group)