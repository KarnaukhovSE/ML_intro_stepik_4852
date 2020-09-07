import pandas as pd

concentrations = pd.read_csv('../resources/algae.csv')
mean_concentrations = concentrations.groupby('genus').mean()

print(mean_concentrations)

quit(0)
