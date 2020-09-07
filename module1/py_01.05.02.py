import pandas as pd

students_performance = pd.read_csv('../resources/StudentsPerformance.csv')

# gender column - panda Series
print(students_performance.gender)

# сравнение пандовской серии с некоторым результатом даст
# новую пандовскую серию со значениями true и false
print(students_performance.gender == 'female')

# отбор строк female
print(students_performance.loc[students_performance.gender == 'female'])

# отбор не полных строк, а только нужных колонок
print(students_performance.loc[students_performance.gender == 'female', ['gender', 'writing score']])

exit(0)
