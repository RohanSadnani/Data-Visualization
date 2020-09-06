import pandas as pd
from pandas import DataFrame,Series

df = DataFrame({'col1':['Uber','Uber','Uber','Uber','Grab'], 'col2':[5,4,3,3,5]})
print(df)

print('------------------------')

print(df.duplicated())

print('------------------------')

print(df.drop_duplicates())

print('------------------------')

print(df.drop_duplicates(['col1']))

print('------------------------')

print(df.drop_duplicates(['col1'], keep='last'))