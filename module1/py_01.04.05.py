import pandas as pd
import numpy as np

students_performance = pd.read_csv('../resources/StudentsPerformance.csv')
#select first 5 rows and first 3 columns
print(students_performance.iloc[0:5, 0:3])

#select 0, 3 and 10 rows
print(students_performance.iloc[[0,3,10],[-1, -2, -3]])
