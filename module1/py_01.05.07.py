import pandas as pd

students_performance = pd.read_csv('../resources/StudentsPerformance.csv')

free_reduced_lunch_condition = students_performance["lunch"] == "free/reduced"
standard_lunch_condition = students_performance["lunch"] == "standard"

print("Standard mean:")
print(students_performance.loc[standard_lunch_condition].mean(numeric_only=True))
print("Standard variance:")
print(students_performance.loc[standard_lunch_condition].var(numeric_only=True))
print("Standard describe:")
print(students_performance.loc[standard_lunch_condition].describe())

print("Free mean:")
print(students_performance.loc[free_reduced_lunch_condition].mean(numeric_only=True))
print("Free variance:")
print(students_performance.loc[free_reduced_lunch_condition].var(numeric_only=True))
print("Free describe:")
print(students_performance.loc[free_reduced_lunch_condition].describe())


quit(0)
