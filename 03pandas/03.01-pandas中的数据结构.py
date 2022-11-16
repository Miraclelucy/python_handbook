import numpy as np
import pandas as pd

# 用numpy数组创建Series
data = pd.Series([0.25, 0.5, 0.75, 1.0])
n1 = data.values  # values是一个numpy数组
sub1data = data[1]
sub2data = data[1:3]

data2 = pd.Series([0.25, 0.5, 0.75, 1.0],
                  index=['a', 'b', 'c', 'd'])  # 类似一个广义的numpy数组，可以显式地指定index
sub1data2 = data2['b']
data3 = pd.Series([0.25, 0.5, 0.75, 1.0],
                  index=[2, 5, 3, 7])  # 索引可以不必是连续的

# 用字典创建Series
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
population1 = population['California']
population2 = population['California':'Illinois']

# 直接创建Series
pd.Series([2, 4, 6])
pd.Series(5, index=[100, 200, 300])
pd.Series({2: 'a', 1: 'b', 3: 'c'})
pd.Series({2: 'a', 1: 'b', 3: 'c'}, index=[3, 2])  # 只返回指定索引的部分数据

# 用多个Series创建DataFrame
area_dict = {'California': 423967,
             'Texas': 695662,
             'New York': 141297,
             'Florida': 170312,
             'Illinois': 149995}
area = pd.Series(area_dict)
states = pd.DataFrame({'population': population,
                       'area': area})
print(states.index)  # 索引名
print(states.columns)  # 列名
print(states['area']) # 访问某一列


# 用单个Series创建DataFrame
# DataFrame是Series的一个集合，也可以由一个Series构成
states1 = pd.DataFrame(population, columns=['population'])


# 用字典创建DataFrame
data = [{'a': i, 'b': 2 * i} for i in range(3)]
dataset0 = pd.DataFrame(data)

# 创建含有NaN的DataFrame
dataset1 = pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])

# 用二维numpy数组创建DataFrame
dataset2 = pd.DataFrame(np.random.rand(3, 2),columns=['foo', 'bar'],
             index=['a', 'b', 'c'])

# 用结构化的numpy数组创建DataFrame
A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
dataset3 = pd.DataFrame(A)


# 在pandas种索引本身是一种结构，用整数构造索引
ind = pd.Index([2, 3, 5, 7, 11])
print(ind[1])
print('---------------------------------')
print(ind[::2]) # 隔2个序号取一个值
print(ind[::-1]) # 把列倒着排一遍
print(ind.size, ind.shape, ind.ndim, ind.dtype)

# 索引是一种有序的集合，可以求交集、并集、差集
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
print(indA & indB)  # intersection
print(indA | indB)  # union
print(indA ^ indB)  # symmetric difference



