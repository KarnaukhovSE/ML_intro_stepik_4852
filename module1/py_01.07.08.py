import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../resources/dota_hero_stats.csv')
print(df.columns)
df['roles_length'] = df.roles.str.split(',').str.len()
# with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
#     print(df)
print(df.groupby('roles_length').aggregate({'roles_length': 'count'}))
df.roles_length.hist()
plt.show()

quit(0)
