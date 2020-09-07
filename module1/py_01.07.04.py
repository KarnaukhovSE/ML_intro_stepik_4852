import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# Matplotlib интегрирован с pandas
students_performance.plot.scatter(x='math_score', y='reading_score')
plt.show()

# В seaborn графики покрасивее и больше возможностей
sns.lmplot(x='math_score', y='reading_score', data=students_performance)
plt.show()

# Покрасим точки в зависимости от переменной gender
sns.lmplot(x='math_score', y='reading_score', hue='gender', data=students_performance)
plt.show()

# Если регрессионные прямые не нужны
sns.lmplot(x='math_score', y='reading_score', hue='gender', data=students_performance, fit_reg=False)
plt.show()

# У графика можно менять параметры, например установить подписи для осей
plot = sns.lmplot(x='math_score', y='reading_score', hue='gender', data=students_performance, fit_reg=False)
plot.set_xlabels('Math score')
plot.set_ylabels('Reading score')
plt.show()


quit(0)
