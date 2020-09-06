import numpy as np
import pandas as pd
from pandas import Series,DataFrame

url = "https://en.wikipedia.org/wiki/Pivot_table"
df_list = pd.io.html.read_html(url)
df = df_list[0]

#print(df)

print('--------------------------------------')
#new_header = df.iloc[0] #grabs the first row of the header
df = df[0:] #take the data less the header row
#df.columns = new_header #assigning a new header

print(df)


print(df.pivot('Date of sale', 'Sales person', 'Total price'))
