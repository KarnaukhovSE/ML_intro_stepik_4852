import pandas as pd

students_performance = pd.read_csv('../resources/StudentsPerformance.csv')

free_reduced_lunch_condition = students_performance["lunch"] == "free/reduced"
free_reduced_lunch_students = students_performance.loc[free_reduced_lunch_condition]
free_reduced_lunch_students_ratio = free_reduced_lunch_students.index.size / students_performance.index.size
print(free_reduced_lunch_students_ratio)
