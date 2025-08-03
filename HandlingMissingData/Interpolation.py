#Interpolations - refers to filling of missing value with estimated value (works only with numerical columns)
#Used for - preserving data integrity, smooth trends, avoid data loss
import pandas as pd
data={
    "Time" : [1,2,3,4,5],
    "Value" : [10,None,30,None,50]
}
df=pd.DataFrame(data)
print("Before Interpolation")
print(df)

#types : linear, polynomial, time, cubic etc.
#linear interpolation
df['Value']=df['Value'].interpolate(method="linear")
print("After Interpolation")
print(df)