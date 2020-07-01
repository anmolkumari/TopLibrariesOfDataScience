
# adding, manpulating and removing inside df in pandas
import pandas as pd

ufo=pd.read_table('http://bit.ly/uforeports',sep=',')

#printing top 5
print(ufo.head(25))
print(ufo.info())
print(ufo.describe())
print(ufo.shape)

#moduifyng

ufo['Address']=ufo['City']+","+ufo['State']
print(ufo.head(3))
print(ufo.dtypes)



#removing the columns
ufo.drop('Colors Reported',axis=1,inplace=True)
print(ufo.head(3))
print(ufo['State'].sort_values(ascending=False))

