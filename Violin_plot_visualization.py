import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

ds = randn(80)
#sns.violinplot(ds).get_figure().savefig('violin1.png')
#sns.violinplot(ds,bw=0.2).get_figure().savefig('violin2.png')

sns.violinplot(ds, inner='stick').get_figure().savefig('violin3.png')