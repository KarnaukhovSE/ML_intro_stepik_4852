import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../resources/genome_matrix.csv', index_col=0)
print(df.shape)
g = sns.heatmap(df, center=0, cmap="viridis")
g.xaxis.set_ticks_position('top')
g.xaxis.set_tick_params(rotation=90)
plt.show()

quit(0)
