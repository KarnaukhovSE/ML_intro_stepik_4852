import pandas as pd

concentrations = pd.read_csv('../resources/algae.csv')
#print(concentrations.columns)

#print(concentrations.groupby('group').count())
#print(concentrations.groupby('group').std())
#print(concentrations.groupby('group').var())

print()
print('Сахароза: размах')
print((concentrations.groupby('group').aggregate({'sucrose': 'max'})['sucrose'] - concentrations.groupby('group').aggregate({'sucrose': 'min'})['sucrose']).round(2))

print()
print('Цитрат: дисперсия')
print(concentrations.groupby('group').aggregate({'citrate': 'var'}).round(2))

print()
print('Группы: количество')
print(concentrations.groupby('group').aggregate({'citrate': 'count'}).rename(columns={'citrate': 'num'}))

quit(0)
