import pandas as pd
import numpy as np

students_performance = pd.read_csv('../resources/StudentsPerformance.csv')
print(students_performance)
print(students_performance.head())
print(students_performance.head(1))
print(students_performance.tail(2))
print(students_performance.describe())
print(students_performance.dtypes)
print(students_performance.shape)
print(students_performance.groupby('gender').aggregate({'writing score': 'mean'}))
print(type(students_performance))

print("===========================================")
print("iloc")
print(students_performance.iloc[0:5, 0:3])
