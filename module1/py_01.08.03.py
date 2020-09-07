import pandas as pd

my_stat = pd.read_csv('../resources/my_stat.csv')
subset_1 = my_stat[['V1', 'V3']].head(10)
subset_2 = my_stat.drop([0, 4])[['V2', 'V4']]
print(subset_2)

quit(0)
