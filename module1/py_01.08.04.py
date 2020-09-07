import pandas as pd

my_stat = pd.read_csv('../resources/my_stat.csv')
subset_1 = my_stat.query("V1 > 0 & V3 == 'A'")
subset_2 = my_stat.query("V2 != 10 | V4 >= 1")
print(subset_1)
print(subset_2)

quit(0)
