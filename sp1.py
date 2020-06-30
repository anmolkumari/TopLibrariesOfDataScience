# learnt tabulate
# learnt string replace
# learnt groupby
# learnt mean
# using a function and accessing pandas df


import pandas as pd
from tabulate import tabulate

# #initialising 
# val=[['Alice',23],['Bubble',22],['Joy',24]]


# #printing in table format
# print(tabulate(val,headers=['Name','Age']))

df=pd.read_csv('original.csv')

print(df.info())
def cleanup_salary(row):
	salary=row['Salary'].replace('$','')
	salary=float(salary)
	return salary

df['clean']=df.apply(cleanup_salary,axis=1)
print(df.groupby('gender')['clean'].mean())

print(df['clean'].mean())
print(df)
print(df.dtypes)

#  print(df['Salary'].dtypes)
#  print(df)

 



