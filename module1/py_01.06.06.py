import pandas as pd

accountancy = pd.read_csv('../resources/accountancy.csv')

print(accountancy.groupby(['Type', 'Executor']).aggregate({'Salary': 'mean'}))
#print(accountancy.sort_values(['Executor', 'Type']))

quit(0)
