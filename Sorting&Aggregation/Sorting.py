#Sorting refers to arranging data according to some conditions
#Sorting data in one column, syntax: sort_values(by="Column_Name", ascending=True, inplace=True), ascending=True-> ascending, ascending=False-> descending
import pandas as pd
data={
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[28,34,22],
    "Salary":[50000,60000,45000],
    "Performance Score":[85,90,78]
}
df=pd.DataFrame(data)

df.sort_values(by="Age", ascending=False, inplace=True)
# print("Sorting age in descending order :-")
# print(df)

#Sorting data in multiple columns
df.sort_values(by=["Age","Salary"], ascending=[True, False], inplace=True)
print("Sorting age & salary in descending order :-")
print(df)