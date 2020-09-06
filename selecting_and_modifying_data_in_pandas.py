import pandas as pd
import numpy as np

from pandas import Series,DataFrame

series1 = Series([100,200,300,400,500], index=['A','B','C','D','E'])
print(series1)

print(series1['A'])
print(series1['B'])

print(series1[['A','B']])

print(series1[0])
print(series1[1])

print(series1[0:3])
print('------------')

#conditional values
print(series1[series1>150])

print(series1[series1==300])
print('------------')

#using df and accessing in dataframes

df1=DataFrame(np.arange(9).reshape(3,3), index=['car','bike','cycle'], columns=['A','B','C'])
print(df1)
print('------------')
#accessing the members of the columns

print(df1['A'])

print(df1[['A','B','C']])
print('------------')

print(df1>=5)
print('------------')

print (df1.loc['bike'])
print('------------')

print(df1.iloc[1])

