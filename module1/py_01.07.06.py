import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../resources/dataset_209770_6.txt', delimiter=' ')
print(df)
df.plot.scatter(x=df.columns[0], y=df.columns[1])
plt.show()

quit(0)
