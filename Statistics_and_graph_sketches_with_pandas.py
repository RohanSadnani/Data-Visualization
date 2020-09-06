import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn
import matplotlib.pyplot as plt

array1 = np.array([[10,np.nan,20],[30,40,np.nan]])
print(array1)

df1 = DataFrame(array1, index=[1,2], columns=list('ABC'))
print(df1)

#sum operations

print(df1.sum())

#sum along the rows
print(df1.sum(axis=1))

print(df1.min())
print(df1.max())

print('----------')

print(df1.idxmax())
print(df1.idxmin())
print('----------')

print(df1.cumsum())
print('----------')

print(df1.describe())
print('----------')

df2 = DataFrame(randn(9).reshape(3,3),index=[1,2,3], columns=list('ABC'))
print(df2)
print('----------')

plt.plot(df2)
plt.legend(df2.columns, loc="lower right")
plt.savefig("first graph in python")
plt.show()

ser1 = Series(list('abcccaabd'))
print(ser1.unique())

print(ser1.value_counts())
