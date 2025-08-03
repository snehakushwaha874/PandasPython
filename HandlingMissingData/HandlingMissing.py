import pandas as pd
data={
    "Name":['Ram',None,'Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,None,78,92,88,95,80,89]
}
df=pd.DataFrame(data)

#remove the missing values of a row/column,syntax: dropna(axis = 0(0->row, 1->column), inplace= True)
df.dropna(inplace=True)
print(df)

# #replaces the None value with the given value, syntax: fillna(value, inplace=True)
df.fillna(0, inplace=True)
print(df)

#replaces the None value with the calculated value, syntax: df['ColumnName'].fillna(df['ColumnName'].statistical_method(), inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)