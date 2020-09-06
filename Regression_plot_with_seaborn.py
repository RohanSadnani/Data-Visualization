import numpy as np
import pandas as pd
from pandas import Series
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv"
df = sns.load_dataset('diamonds').sample(frac=1).head(100)
print(df)

sns.lmplot('price','carat',df).savefig('drift.png')

#modify

sns.lmplot('price','carat',df, scatter_kws={'marker':'x','color':'green'},
           line_kws={'color':'red', 'linewidth':1}).savefig('tokyo.png')

#higher order trend line
sns.lmplot('price','carat',df, order=4,scatter_kws={'marker':'x','color':'green'},
           line_kws={'color':'red', 'linewidth':1}).savefig('denver.png')

#scatter plot without a trend line
sns.lmplot('price','carat',df, fit_reg=False).savefig('moscow.png')

#hue arguments
sns.lmplot('price','carat',df, hue='cut', markers=['^','v','*','.','s']).savefig('lisbon.png')

sns.lmplot('price','carat',df, hue='cut').savefig('Nairobi.png')

#local regression
sns.lmplot('price','carat',df,lowess=True).savefig('Rio.png')

#regplot
sns.regplot('price', 'carat',df).get_figure().savefig('Berlin.png')

#sub plot
# we are creating a subplot with 1 row and 2 columns, price and carat are x and y axis respectively ax= axis and they are plt1 and plt2
image, (plt1, plt2) = plt.subplots(1,2, sharey=True)
sns.regplot('price','carat',df, ax=plt1).get_figure().savefig('Helsinki.png')
sns.boxplot(df['carat'], df['depth'], color='green', ax=plt2).get_figure().savefig('Helsinki.png')