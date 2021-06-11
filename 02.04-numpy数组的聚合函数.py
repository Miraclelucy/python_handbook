import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # set plot style

L = np.random.random(100)
print("L ", L)
print("sum(L) ", sum(L))  # 自带的求和函数和np求和的效果一样，但是因为动态编译的原因，更加耗时
print("np.sum(L) ", np.sum(L))

# 最大最小函数
big_array = np.random.rand(1000000)
print("max(big_array) ", max(big_array))
print("min(big_array) ", min(big_array))
print("np.max(big_array) ", np.max(big_array))
print("np.min(big_array) ", np.min(big_array))

# 多维聚合
M = np.random.random((3, 4))
print("M ", M)
print("M.min(axis=0) ", M.min(axis=0))
print("M.max(axis=1) ", M.max(axis=1))

# 其他聚合函数
'''
np.sum np.nansum 计算元素的总和
np.prod np.nanprod 计算元素的乘积
np.mean np.nanmean 计算元素的平均值
np.std np.nanstd 计算标准偏差
np.var np.nanvar 计算方差
np.min np.nanmin 求最小值
np.max np.nanmax 求最大值
np.argmin np.nanargmin 查找最小值的索引
np.argmax np.nanargmax 查找最大值的索引
np.median np.nanmedian 计算元素的中位数
np.percentile np.nanpercentile 计算元素的基于等级的统计数据
np.any N/A 评估是否有任何元素为真
np.all N/A 评估是否所有元素都为真
'''
data = pd.read_csv('data/president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)
print("Mean height:       ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())
print("25th percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th percentile:   ", np.percentile(heights, 75))

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
plt.show()

