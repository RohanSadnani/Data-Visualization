import numpy as np
import pandas as pd
from pandas import Series

from numpy.random import randn

ser_1 = Series([500,1000,1500], index=['a','c','b'])
print(ser_1)

print('---------')

#sorting by index
print(ser_1.sort_index())

print('---------')

#sort by values
print(ser_1.sort_values())

print('---------')

#ranking of series
ser_2 = Series(randn(10))
print(ser_2)
print('---------')

print(ser_2.rank())

print('---------')
ser_2 = ser_2.sort_values()

print('---------')
print(ser_2.rank())


print('---------')
#print(ser_1.rank())