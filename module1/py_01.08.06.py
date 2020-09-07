import pandas as pd

my_stat = pd.read_csv("../resources/my_stat.csv")
my_stat = my_stat.rename(columns={"V1": "session_value", "V2": "group", "V3": "time", "V4": "n_users"})
print(my_stat)

quit(0)
