import pandas as pd
import numpy as np

my_stat = pd.read_csv('../resources/my_stat.csv')
my_stat['V5'] = my_stat.V1 + my_stat.V4
my_stat['V6'] = np.log(my_stat.V2)
print(my_stat)

quit(0)
