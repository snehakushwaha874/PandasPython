#for AND condition use -> &
#for OR condition use -> |

import pandas as pd
data={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)

#display dataframe
print("Sample Dataframe")
print(df)

#single condition
high_salary = df[df['Salary']>50000]
print("Employees with salary greater than 50000")
print(high_salary)

#multiple conditions
salary_age = df[(df['Salary']>50000) & (df['Age']>80)]
print("Employees with Salary greater than 50000 and Age greater than 80")
print(salary_age)