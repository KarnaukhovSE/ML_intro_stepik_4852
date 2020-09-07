import pandas as pd

my_stat = pd.read_csv('../resources/my_stat.csv')
my_stat = my_stat.rename(columns={"V1": "session_value", "V2": "group", "V3": "time", "V4": "n_users"})
mean_session_value_data = \
    my_stat.groupby('group', as_index=False) \
        .agg({'session_value': 'mean'}) \
        .rename(columns={'session_value': 'mean_session_value'})
print(mean_session_value_data)

quit(0)
