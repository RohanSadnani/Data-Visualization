#oulou ka chutiyapa hai na wo ola uber lyft ka abbreviation hai

import pandas as pd
import numpy as np
from pandas import DataFrame,Series

df1 = DataFrame({'reference':['O','U','L','O','U'], 'data':range(5)})
print(df1)
print('------------------------------')

df2 = DataFrame({'profit':[10,20,30]}, index=['O','U','L'])
print(df2)
print('------------------------------')

print(pd.merge(df1,df2, left_on='reference', right_index=True))
print('------------------------------')

df3 = DataFrame({'ref1':['A','A','O','O','O'],'ref2':[5,10,15,20,25],'ref3': np.arange(5.)})

df4 = DataFrame({'ref1':['A','A','O','O','O'],'ref2':[5,10,15,20,25],'ref3':[2,3,4,5,6]})

#print(pd.merge(df3,df4, left_on=['ref1','ref2'],right_index=True))

#join functions in pandas

print(df3.join(df4, lsuffix='x', rsuffix='y'))