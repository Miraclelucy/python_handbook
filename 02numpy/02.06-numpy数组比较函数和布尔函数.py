import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn;

seaborn.set()  # set plot styles

# 加载西雅图市 2014 年的每日降雨量
rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0  # 1/10mm -> inches
print(inches.shape)  # (365,)

plt.hist(inches, 40);
plt.show()

# 比较函数
x = np.array([1, 2, 3, 4, 5])
print("x < 3  ", x < 3)
print("x > 3  ", x > 3)
print("x <= 3  ", x <= 3)
print("x >= 3  ", x >= 3)
print("x != 3  ", x != 3)
print("x == 3  ", x == 3)

'''
比较运算符执行时，实际上Numpy在内部执行的函数ufunc
==	np.equal		!=	np.not_equal
<	np.less		    <=	np.less_equal
>	np.greater		>=	np.greater_equal
'''

# 比较函数
rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
print("x   ", x)
print("np.count_nonzero(x < 6)  ", np.count_nonzero(x < 6))  # 小于6的元素总数
print("np.sum(x < 6)  ", np.sum(x < 6))  # 小于6的元素总数
print("np.sum(x < 6, axis=1)  ", np.sum(x < 6, axis=1))  # 每一行小于6的元素总数
print("np.any(x > 8)  ", np.any(x > 8))  # 是否存在元素大于8
print("np.any(x < 0)  ", np.any(x < 0))  # 是否存在元素小于0
print("np.all(x < 10)  ", np.all(x < 10))  # 是否所有的元素都小于10
print("np.all(x == 6)  ", np.all(x == 6))  # 是否所有的元素都等于6
print("np.all(x < 8, axis=1)  ", np.all(x < 8, axis=1))  # 是否每行中所有的元素都小于8

# 布尔函数
print(inches.shape)  # (365,)
print("np.sum((inches > 0.5) & (inches < 1)) ", np.sum((inches > 0.5) & (inches < 1)))  # 降雨量大于0.5英寸小于1英寸的天数
np.sum(~((inches <= 0.5) | (inches >= 1)))  # 与上条等价
print("Number days without rain:      ", np.sum(inches == 0))
print("Number days with rain:         ", np.sum(inches != 0))
print("Days with more than 0.5 inches:", np.sum(inches > 0.5))
print("Rainy days with < 0.2 inches  :", np.sum((inches > 0) & (inches < 0.2)))

# 布尔数组
print("x   ", x)
print("x < 5 ", x < 5)
print("x[x < 5] ", x[x < 5])

# 将比较函数运用在西雅图市2014年的每日降雨量的分布中
rainy = (inches > 0)
# construct a mask of all summer days (June 21st is the 172nd day)
days = np.arange(365)
summer = (days > 172) & (days < 262)

print("2014年雨天平均降水量 (inches):   ", np.median(inches[rainy]))  # 计算元素的中位数
print("2014年夏季平均降水量 (inches):  ", np.median(inches[summer]))  # 计算元素的中位数
print("2014年夏季最大降水量 (inches): ", np.max(inches[summer]))
print("2014年非夏季雨天平均降水量 (inches):", np.median(inches[rainy & ~summer]))

# 操作符& 和 |
print("bool(42)   ", bool(42))
print("bool(0)   ", bool(0))
print("bool(42 and 0)   ", bool(42 and 0))
print("bool(42 or 0)   ", bool(42 or 0))
print("bool(42 &  0)   ", bool(42 & 0))
print("bool(42 |  0)   ", bool(42 | 0))
print("bin(42)   ", bin(42))  # 访问数字对应的二进制
print("bin(59)   ", bin(59))
print("bin(42 & 59)   ", bin(42 & 59))
print("bin(42 | 59)   ", bin(42 | 59))

A = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
B = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
print("A | B   ", A | B)
# print("A or B  ", A or B) #会报错

x = np.arange(10)
print("(x > 4) & (x < 8)  ",(x > 4) & (x < 8))
# print("(x > 4) and  (x < 8)  ",(x > 4) and  (x < 8)) #会报错

'''
and 和 or 对整个对象执行单个布尔计算，而 & 和 |是对对象的内容（单个位或字节）执行多个布尔评估
'''
