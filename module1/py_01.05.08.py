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
print(students_performance.columns)

# запросы

print(students_performance.query("writing_score > 74"))

print(students_performance.query("gender == 'female'"))

print(students_performance.query("gender == 'female' & writing_score > 78"))

writing_score_query = 78
print(students_performance.query("writing_score > @writing_score_query"))

quit(0)
