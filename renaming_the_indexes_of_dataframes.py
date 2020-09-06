import numpy as np
import pandas as pd
from pandas import Series,DataFrame

df = DataFrame(np.arange(25).reshape(5,5,), index=['Uber','Ola','Grab','Gojek','lyft'], columns=['Re','Lo','Qu','Gr','Ag'])
print(df)

#use mapping
print('---------------------------------')

df.index = df.index.map(str.lower)
print(df)

print('---------------------------------')

#rename method
print(df.rename(index=str.title, columns=str.lower))
print('---------------------------------')

#using dictonary for changing indexes
print(df.rename(index={'uber': 'Most chutiya service in India'}, columns={'Re':'Revenue'}))

print('---------------------------------')

#how to save
df.rename(index={'uber': 'Most chutiya service in India'}, columns={'Re':'Revenue'}, inplace=True)
print(df)
