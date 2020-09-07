import pandas as pd

students_performance = pd.read_csv('../resources/StudentsPerformance.csv')
# неудобно работать с именами колонок с пробелами - нельзя обратиться через точку.
# переименуем
students_performance = students_performance.rename(columns={
    'gender': 'gender',
    'race/ethnicity': 'race/ethnicity',
    'parental level of education': 'parental_level_of_education',
    'lunch': 'lunch',
    'test preparation course': 'test_preparation_course',
    'math score': 'math_score',
    'reading score': 'reading_score',
    'writing score': 'writing_score'
})

# нужно показать не все колонки, а только те, в названии которых есть "score"

# Вариант 1. Не pandas-way
print("Вариант 1. Не pandas-way")
print(list(students_performance))
score_columns = [i for i in list(students_performance) if 'score' in i]
print(score_columns)
print(students_performance[score_columns])
print("====================")
print()

# Вариант 2. Pandas-way
print("Вариант 2. Pandas-way")
print("====================")
print(students_performance.filter(like='score'))
print()

# датасет с именованными индексами
students_performance_with_names = students_performance.iloc[[0, 3, 4, 7, 8]]
print(students_performance_with_names)

# Назначение имён индексам
students_performance_with_names.index = ['bebebe', 'bababa', 'dedede', 'dadada', 'fefefe']
print(students_performance_with_names)

# Отбор колонок, в именах которых есть латинская буква 'e'
print(students_performance_with_names.filter(like='e', axis=1))
# Отбор строк, в именах индексов которых есть латинская буква 'e'
print(students_performance_with_names.filter(like='e', axis=0))

quit(0)
