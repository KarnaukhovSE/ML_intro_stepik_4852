import pandas as pd

students_performance = pd.read_csv('../resources/StudentsPerformance.csv')
students_performance_with_names = students_performance.iloc[[0, 3, 4, 7, 8]]
print(students_performance_with_names)

# Назначение имён индексам
students_performance_with_names.index = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print(students_performance_with_names)

# Получение строк по именам индексов
print(students_performance_with_names.loc[['aaa', 'ddd']])

# Получение строк по именам индексов и столбцов по именам столбцов из файла
print(students_performance_with_names.loc[['aaa', 'ddd'], ['race/ethnicity', 'reading score']])

# Получение первого столбца и определение его типа
print(students_performance_with_names.iloc[:, 0])
# Каждый столбец имеет тип panda Series, эти panda Series объединяются в panda Dataframe
print(type(students_performance_with_names.iloc[:, 0]))

# Pandas Series
pd_ser = pd.Series([1, 2, 3])
print(pd_ser)

# Pandas Series with named indexes
pd_ser_named_indexes = pd.Series([4, 5, 6], index=['zzz', 'yyy', 'xxx'])
print(pd_ser_named_indexes)

# Panda Dataframe - это словарь в котором ключами являются имена колонок,
# а значениями - panda Series, содержащие значения колонок
pd_ser_1 = pd.Series([2, 3, 5], index=['www', 'mmm', 'rrr'])
pd_ser_2 = pd.Series([9, 8, 7], index=['www', 'mmm', 'rrr'])
pd_dataframe = pd.DataFrame({'col_01': pd_ser_1, 'col_02': pd_ser_2})
print(pd_dataframe)

# получение колонки в виде поддатафрейма из датафрейма
sub_pd_dataframe = pd_dataframe[['col_01']]
print(sub_pd_dataframe)
print(type(sub_pd_dataframe))
print(sub_pd_dataframe.shape)

# получение колонки в виде серии из датафрейма
ser_from_dataframe = pd_dataframe['col_01']
print(ser_from_dataframe)
print(type(ser_from_dataframe))
print(ser_from_dataframe.shape)

exit(0)
