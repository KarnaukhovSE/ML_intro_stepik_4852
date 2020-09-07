import pandas as pd
import numpy as np

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

# Добавление колонки (панда серии) в датафрейм
print(type(students_performance.math_score + students_performance.reading_score + students_performance.writing_score))
students_performance['total_score'] = \
    students_performance.math_score + \
    students_performance.reading_score + \
    students_performance.writing_score
print(students_performance)

# добавление метод assign
students_performance = students_performance.assign(total_score_log=np.log(students_performance.total_score))
print(students_performance)

# удаление колонок
print(students_performance.drop(['total_score'], axis=1))

quit(0)
