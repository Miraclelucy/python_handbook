import pandas as pd

# 指定索引访问Series对象
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
print(data['b'])  # 指定索引访问数据
print('a' in data)  # 判断索引是否在Series中
print(data.keys())  # 访问keys值
print(list(data.items()))  #
data['e'] = 1.25  # 修改指定索引的值

# 访问Series对象的片
slice1 = data['a':'c']  # 用显式索引访问，返回了3个元素，这个注意一下
slice2 = data[0:2]  # 用隐式索引访问，返回了2个元素
slice3 = data[(data > 0.3) & (data < 0.8)]
slice4 = data[['a', 'e']]  # 花式索引

# 由于整数索引存在潜在的混乱，pandas一般这几个函数来访问数据loc, iloc
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
slice5 = data.loc[1]  # 用显式索引访问
slice6 = data.loc[1:3]  # 用显式索引访问
slice7 = data.iloc[1]  # 用隐式索引访问
slice8 = data.iloc[1:3]  # 用隐式索引访问

area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area': area, 'pop': pop})
subdata1 = data['area']
subdata2 = data.area
data['density'] = data['pop'] / data['area']
data.values
data.values[0]
data.T

data['area']
data.iloc[:3, :2]  # 隐式索引是不包含边界的
data.loc[:'Illinois', :'pop']  # 显式索引是包含边界的
data.loc[data.density > 100, ['pop', 'density']]
data.iloc[0, 2] = 90  # 赋值

data['Florida':'Illinois']
data[1:3]
data[data.density > 100]
