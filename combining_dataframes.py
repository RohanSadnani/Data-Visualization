import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from numpy import random

s1 = Series([5,np.nan,6,np.nan], index=['A','B','C','D'])
print(s1)

s2 =Series(np.arange(4), dtype=np.float64, index=s1.index)
print(s2)

s3 = Series(np.where(pd.isnull(s1),s2,s1),index=s1.index)
print(s3)

s4 = Series(s1.combine_first(s2))
print(s4)

#DataFrames

df_5m = DataFrame({'col1': [5, np.nan,15],'col2':[20,25,np.nan],'col3':[np.nan,np.nan,35]})

df_10m =DataFrame({'col1': [0,10,20],'col2':[20,25,30]})

print(df_5m)
print('----------------')
print(df_10m)

print(df_5m.combine_first(df_10m))