import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../resources/iris.csv', index_col=0)
print(df.columns)
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
    print(df)
for column in df:
    print(column)
    print(column, " mode ", df[column].mode())
    sns.distplot(df[column], kde_kws={"label": column})
    plt.show()
# df.hist()
# plt.show()
quit(0)
