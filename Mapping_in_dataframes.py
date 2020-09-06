import numpy as np
import pandas as pd
from pandas import DataFrame

df = DataFrame({'country':['India','South Korea','Thailand'],
                'code':['91','82','66']})

print(df)

print('--------------------------------')

GDP_map = {'India':'20', 'South Korea':'12.8', 'Thailand':'215'}
print(GDP_map)

print('--------------------------------')

df['GDP'] = df['country'].map(GDP_map)
print(df)