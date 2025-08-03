import pandas as pd
data={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)

#sum() - calculates the sum of the given column
print(df["Age"].sum())

#mean() - calculates the average of the given column
print(df["Age"].mean())

#median() - calculates the median of the given column
print(df["Age"].median())

#count() - returnss the count of values of the given column
print(df["Age"].count())

#min() - returns the minimum element of the given column
print(df["Age"].min())

#max() - returns th maximum element sum of the given column
print(df["Age"].max())

#std() - calculates the standard deviation of the given column
print(df["Age"].std())
