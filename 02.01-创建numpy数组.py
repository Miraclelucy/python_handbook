import numpy as np

# 简单的Python列表
L = list(range(10))
L2 = [str(c) for c in L]
L3 = [True, 1, '2']

# Python列表转np数组
n1 = np.array([1, 2, 3, 4])
n2 = np.array([3, 4, 5, 6], dtype='float32')
n3 = np.array([range(i, i + 3) for i in range(4)])

# 利用函数创建np数组
n4 = np.zeros(10, dtype=int)  # 全0的一维数组
n5 = np.ones((3, 5), dtype=float)  # 全1的形状为3*5的二维数组
n6 = np.full((3, 5), 3.14)  # 全部元素为3.14的形状为3*5的二维数组
n7 = np.arange(0, 20, 2)  # 0-20取值且步幅为2的一维数组
n8 = np.linspace(0, 1, 5)  # 0-1之间的5个呈线性分布的数
n9 = np.random.random((3, 3))  # 0-1之间随机取值，返回形状为3*3的二维数组
n10 = np.random.normal(0, 1, (3, 3))  # 均值为0方差为1的正态分布中取值，返回形状为3*3二维数组
n11 = np.random.randint(0, 10, (3, 3))  # 0-10之间随机取值，返回形状为3*3二维数组
n12 = np.eye(3) # 形状为3*3对角二维数组
n13 = np.empty((3,2), dtype = int) # 创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
