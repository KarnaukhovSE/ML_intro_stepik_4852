import pandas as pd

dota_hero_stats = pd.read_csv('../resources/dota_hero_stats.csv')
print(dota_hero_stats.groupby('legs').size())

quit(0)
