import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../resources/income.csv')
print(df.index)
print(df.income)
print(df.columns)
print(df.columns[0])
print(sns.__version__)
#income.hist()
#plt.show()

#income.plot.scatter(x='date', y='income')
#plt.show()

sns.lineplot(x=df.index, y=df.income)
plt.show()

plt.plot(df.index, df.income)
plt.show()

df.plot(kind='line')
plt.show()

sns.lineplot(data=df)
plt.show()

df['income'].plot()
plt.show()

df.plot()
plt.show()

df.income.plot()
plt.show()

quit(0)
