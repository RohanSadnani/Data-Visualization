import pandas as pd
import numpy as np

from pandas import Series,DataFrame

cars= Series (['Alpheon','Hyundai','Kia','SsangYong'],index=['a','b','c','d'])
print(cars)

cars= cars.drop('a')
print(cars)

#dataframes

cars_df = DataFrame(np.arange(12).reshape(4,3), index=['Alpheon','Hyundai','Kia','SsangYong'], columns=['revenue','profit','expenses'])
print(cars_df)

cars_df = cars_df.drop('Kia',axis=0)
print(cars_df)

cars_df = cars_df.drop('revenue', axis=1)
print(cars_df)