import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

url='https://github.com/mwaskom/seaborn-data/blob/master/flights.csv'
df = sns.load_dataset('flights')

df2 = df.pivot('year','month','passengers')
print(df2)

#sns.heatmap(df2).get_figure().savefig('heatmap1.png')

#sns.heatmap(df2, annot=True, fmt='d').get_figure().savefig('heatmap2.png')

sns.heatmap(df2, center=df2.loc[1955,'January']).get_figure().savefig('heatmap3.png')