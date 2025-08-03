import pandas as pd
data={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)

#Adding column via assignment - using square brackets, syntax : df["Column_name"] = some data
df["Bonus"] = df['Salary'] * 0.1 #calculating bonus as 10% increment of salary
print(df)

#Using insert() method - can be added at any index position, syntax : df.insert(location,"column_name", some_data)
df.insert(0,"Employee_Id",[1,2,3,4,5,6,7,8])
print(df)

