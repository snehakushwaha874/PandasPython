#Provides a summary of descriptive statistics for numerical columns in your data frame
import pandas as pd

#creating sample dataframe
data={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

print("Sample Dataframe")
df = pd.DataFrame(data)
print(df)

print("Descriptive Statistics")
print(df.describe())


#count - gives the count of rows with non null values in each column
#mean - gives average of each column
#std - standard deviation - how much values are spread from average value - if std > mean then the values are have big differences and vice versa
#min - smallest data in the column
#25% - first quarter of your data
#50% - median value
#75% - third quarter of your data
#max - largest data in the column