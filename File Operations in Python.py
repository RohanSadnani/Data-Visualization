import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#dframe = pd.read_csv('data2.csv')
#print(dframe)

dframe = pd.read_csv('data2.csv', header=None)
print(dframe)

print('-------------------')
#use readtable
dframe2 = pd.read_table('data2.csv', sep='!', header=None)
print(dframe2)

print('-------------------')
#partial rows importing

print(pd.read_csv('data2.csv',nrows=2, header=None))
print('-------------------')

#dump

dframe2.to_csv('outputCSV.csv', sep='!')

dframe.to_csv('dataoutput.csv', columns=[0,1])