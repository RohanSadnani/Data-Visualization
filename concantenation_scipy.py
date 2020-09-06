import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from numpy import random

B1 = np.arange(25).reshape(5,5)

A1 = random.randn(25).reshape(5,5)

print(B1)
print('-------------------')
print(A1)

print('-------------------')

print(np.concatenate([A1,B1], axis=1))

print('-------------------')
print(np.concatenate([A1,B1], axis=0))

#Series concat- series mei isko concat bolte hai and numpy mei concatenate bolte hai
print('-----------------------')
s1 = Series([100,200,300], index=['A','B','C'])

s2 = Series([400,500], index=['D','E'])

print(pd.concat([s1,s2]))

print(pd.concat([s1,s2], axis=1))

#DataFrames

df1 = DataFrame(random.rand(4,3), columns=['A','B','C'])

df2 = DataFrame(random.rand(3,3), columns=['B','D','A'])

print('pd.concat dataframes')
print(pd.concat([df1,df2])) #we passing 2 dataframes as a list, toh abhi sochega yeh list kaise difference
# yeh hai ki apan ne square brackets use kiye ha

print(pd.concat([df1,df2], ignore_index=True))