import pandas as pd
import numpy as np

concentrations = pd.read_csv('../resources/algae.csv')
#min = concentrations.groupby('genus').min().filter(like='Fucus', axis=0).filter(like='alanin').iloc[0, 0]
#mean_concentrations = concentrations.groupby('genus').mean().filter(like='Fucus', axis=0).filter(like='alanin').iloc[0, 0]
#max = concentrations.groupby('genus').max().filter(like='Fucus', axis=0).filter(like='alanin').iloc[0, 0]

#print(np.round(min, 2), np.round(mean_concentrations, 2), np.round(max, 2))
# print(concentrations.describe())

print(concentrations.groupby('genus').aggregate({'alanin': ['min', 'mean', 'max']}).round(2).loc[['Fucus']])

quit(0)
