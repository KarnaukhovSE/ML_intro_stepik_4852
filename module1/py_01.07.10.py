import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../resources/iris.csv', index_col=0)
sns.violinplot(y=df['petal length'])
plt.show()

quit(0)
