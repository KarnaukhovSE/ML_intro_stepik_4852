import pandas as pd

titanic_passengers = pd.read_csv('../resources/titanic.csv')
#print(titanic_passangers)
print("columns:", titanic_passengers.columns.size)
print("rows:", titanic_passengers.index.size)
print("num types:")
print(titanic_passengers.dtypes.value_counts())
