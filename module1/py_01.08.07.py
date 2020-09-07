import pandas as pd

my_stat = pd.read_csv("../resources/my_stat_1.csv")
my_stat = my_stat.fillna(0)
median_positiv = my_stat.loc[my_stat.n_users >= 0].n_users.median()
my_stat.n_users = my_stat.n_users.where(my_stat.n_users >=0, median_positiv)
print(my_stat)

quit(0)
