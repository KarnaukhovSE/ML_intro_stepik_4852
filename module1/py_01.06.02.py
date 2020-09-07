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

# Группировка по полю 'gender' и вычисление среднго для каждого числового столбца по группам
print(type(students_performance.groupby('gender')))
print(type(students_performance.groupby('gender').mean()))
print(students_performance.groupby('gender').mean())

# в aggregate передаём маппинг, какие переменные используются для агрегации
# и что нужно узнать про эти переменные
# Например среднее для скора по математике
print(students_performance.groupby('gender').aggregate({'math_score': 'mean'}))
print(students_performance.groupby('gender').aggregate({'math_score': 'mean', 'reading_score': 'mean'}))

# В качестве индекса результирующего датафрейма выступают значения атрибута,
# по которому проводилась агрегация. Можно изменить это поведение
print(students_performance.groupby('gender', as_index=False).aggregate({'math_score': 'mean'}))

# Жаль что в названии колонки не заложено, что там находится среднее значение. Не беда...
print(students_performance
      .groupby('gender', as_index=False)
      .aggregate({'math_score': 'mean'})
      .rename(columns={'math_score': 'math_score_mean'})
      )

print(students_performance.groupby('gender').aggregate({'gender': 'count'}))

quit(0)
