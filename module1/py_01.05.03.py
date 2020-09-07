import pandas as pd

students_performance = pd.read_csv('../resources/StudentsPerformance.csv')

# отбор строк со значением writing score выше среднего
# students_performance.writing score - так нельзя, пробел мешает :(
writing_score_mean_value = students_performance['writing score'].mean()
print(students_performance.loc[students_performance['writing score'] > writing_score_mean_value, ['gender', 'writing score']])
print(type(students_performance['writing score'] > writing_score_mean_value))

exit(0)
