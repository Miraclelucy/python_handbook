import numpy as np
import pandas as pd

# 用numpy数组创建Series
data = pd.Series([0.25, 0.5, 0.75, 1.0])
n1 = data.values  #values是一个numpy数组
subdata1 = data[1]
subdata2 = data[1:3]

data2 = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])# 类似一个广义的numpy数组，可以显式地指定index
subdata3 = data2['b']
data3 = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=[2, 5, 3, 7]) # 索引可以不必是连续的

# 用字典创建Series
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
subdict1 = population['California']
subdict2 = population['California':'Illinois']

# 直接创建Series
pd.Series([2, 4, 6])
pd.Series(5, index=[100, 200, 300])
pd.Series({2:'a', 1:'b', 3:'c'})
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2]) # 只返回指定索引的部分数据


