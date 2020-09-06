import numpy as np
import pandas as pd
from pandas import Series
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

ds = randn(100)
#fig = sns.distplot(ds, bins=15).get_figure()
#fig.savefig('kde_plot_as_well_as_histogram.png')

#implementing the rugplot

#fig2 = sns.distplot(ds, hist=False, bins=10, rug=True).get_figure()
#fig2.savefig('technani.png')

#change parameters of each graph

#fig3 = sns.distplot(ds, bins=15, kde_kws={'color':'red', 'label':'KDE graph'},
 #                   hist_kws={'label':'Histogram label', 'color':'green', 'alpha':0.5}).get_figure()

#fig3.savefig('Rohan.png')

s1 = Series(ds,name='s1')
fig4 = sns.distplot(s1, bins=15).get_figure()
fig4.savefig('RohanBhai.png' )


