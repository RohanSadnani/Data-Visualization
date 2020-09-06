import numpy as np
import pandas as pd
from pandas import DataFrame,Series

df1 = DataFrame(np.arange(8).reshape(2,4), index=pd.Index(['Uber','Grab'], name="Cabs"), columns=pd.Index(['c1','c2','c3','c4'], name="attributes"))
print(df1)

print('-------------------------')

stackdf1 = df1.stack()
print(stackdf1)

unstackdf1 = stackdf1.unstack()
print(unstackdf1)

print('-------------------------')

df3 = stackdf1.unstack('Cabs')
print(df3)

df4 = stackdf1.unstack('attributes')
print(df4)

#Series (using stack and unstack funstions in series)

s1 = Series([5,10,15], index=['A','B','C'])

s2 = Series([15,20,25], index=['B','C','D'])

s3 = pd.concat([s1,s2], keys=['k1','k2'])
print(s3)

df = s3.unstack()
print(df)

print('----------------------------')

print(df.stack())

print('----------------------------')

print(df.stack(dropna=False))

