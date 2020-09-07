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

# Группировка по нескольким аттрибутам
print(students_performance
      .groupby(['gender', 'race/ethnicity'], as_index=False)
      .aggregate({'math_score': 'mean'})
      .rename(columns={'math_score': 'math_score_mean'})
      )

# Если убрать 'as_index', то получится сложный составной индекс
mean_scores = students_performance \
      .groupby(['gender', 'race/ethnicity']) \
      .aggregate({'math_score': 'mean'}) \
      .rename(columns={'math_score': 'math_score_mean'})
print(mean_scores.index)
print(mean_scores)
print(mean_scores.loc[('female', 'group A')])
print(mean_scores.loc[[('female', 'group A'), ('female', 'group B')]])
print(mean_scores.loc[[('female', 'group A'), ('male', 'group A')]])
print(mean_scores.loc[[('female', 'group A'), ('female', 'group A')]])

# Количество уникальных оценок по математике по группам
print(students_performance.groupby(['gender', 'race/ethnicity']).math_score.nunique())

# 5 лучших мужчин и 5 лучших женщин математиков
print("5 лучших мужчин и 5 лучших женщин математиков")
print(students_performance.sort_values(['gender', 'math_score'], ascending=False))
print("============================================")
print(students_performance.sort_values(['gender', 'math_score'], ascending=False).groupby('gender'))
print(students_performance.sort_values(['gender', 'math_score'], ascending=False).groupby('gender').head(5))

quit(0)
