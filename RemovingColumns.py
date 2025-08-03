import pandas as pd
data={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)

#used for removing unwanted columns from the data frame, syntax: df.drop(columns = ["ColumnName"], inplace=True)
#removing single column
df.drop(columns=['Performance Score'], inplace=True)
print(df)

#removing multiple columns
df.drop(columns=['Salary','Age'], inplace=True)
print(df)