#Merging refers to joining rows of two or more dataframes based on a common key column. They are like SQL Joins.
#Syntax : pd.merge(df1, df2, on="Common_Column_Name", how="type of join")
#types : cross, inner, outer, left, right
import pandas as pd
df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':["ramesh","suresh","kalpesh"]
})

df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'Order_Amount':[250,450,350]
})

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="cross")
print(df_merged)

#inner - return values with common cell value
#outer - return values with all common cell value and replaces the non-common value with Nan
#left - return values of left column those are common in right column also
#left - return values of right column those are common in left column also
#cross - returns cartesian product of both dataframes