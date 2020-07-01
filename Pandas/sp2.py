#creating df
# creating seriescreating from dic and list
# data types
# conversions
# comparisions

import pandas as pd
import numpy as np




empoyees = [('jack', 34, 'Sydney', 155),
             ('Riti', 31, 'Delhi', 177.5),
             ('Aadi', 16, 'Mumbai', 81),
             ('Mohit', 31, 'Delhi', 167),
             ('Veena', 12, 'Delhi', 144),
             ('Shaunak', 35, 'Mumbai', 135),
             ('Shaun', 35, 'Colombo', 111)
            ]




print(empoyees)
#dataframe

df=pd.DataFrame(empoyees,columns=["Name","Age","City","Marks"])
print(df)

series=df.dtypes
print(series)


idt=df["Age"].dtypes
print(idt)


seriesdic=dict(df.dtypes)
print(seriesdic)

if idt==np.int64:
	print("yes")


filteredcol=df.dtypes[df.dtypes==np.object]
print(list(filteredcol.index))


