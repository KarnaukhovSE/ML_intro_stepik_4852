import pandas as pd

students_performance = pd.read_csv('../resources/StudentsPerformance.csv')

# объединение условий
writing_score_mean_value = students_performance['writing score'].mean()
print(students_performance.loc[(students_performance['writing score'] > writing_score_mean_value) & (students_performance['gender'] == 'female')])

# можно вынести условие в переменную
condition = (students_performance['writing score'] > writing_score_mean_value) & (students_performance['gender'] == 'female')
print(students_performance.loc[condition])

# можно последовательно применить условие (если И)
writing_score_condition = students_performance['writing score'] > writing_score_mean_value
gender_condition = students_performance['gender'] == 'female'
print(students_performance.loc[writing_score_condition].loc[gender_condition])

print("gender condition type:", type(gender_condition))

quit(0)
