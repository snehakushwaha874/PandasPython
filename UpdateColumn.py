import pandas as pd
data={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)

#.loc[] - used for accessing any cell, row, column, syntax: df.loc[row_index, "Column_name" = new_value]
#updating the salary of ram (single cell)
print("updating the salary of ram")
df.loc[0, 'Salary'] = 55000
print(df)

#increasing all salaries by 5% (whole column)
print("increasing all salaries by 5%")
df['Salary'] = df['Salary'] * 1.05
print(df)