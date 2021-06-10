import numpy as np

# np数组的属性
# numpy.random.randint(low, high=None, size=None, dtype='l')
# 函数的作用是，返回一个随机整型数，范围从低（包括）到高（不包括），即[low, high)。high: int (可选)
x1 = np.random.randint(10, size=6)  # 一维数组
x2 = np.random.randint(10, size=(3, 4))  # 二维数组
x3 = np.random.randint(10, size=(3, 4, 5))  # 三维数组

print("x3 ndim: ", x3.ndim)  # 秩，即轴的数量或维度的数量
print("x3 shape:", x3.shape)  # 数组的维度，对于矩阵，n 行 m 列
print("x3 size: ", x3.size)  # 数组元素的总个数，相当于 .shape 中 n*m 的值
print("dtype:", x3.dtype)  # ndarray对象的元素类型
print("itemsize:", x3.itemsize, "bytes")  # ndarray对象中每个元素的大小，以字节为单位
print("nbytes:", x3.nbytes, "bytes")  # 所有元素的总字节数

# 访问一维np数组
print(x1)
print(x1[0]) # 从数组的正向索引开始访问，返回倒数第1个元素
print(x1[4]) # 从数组的正向索引开始访问，返回倒数第5个元素
print(x1[-1]) # 从数组的反向索引开始访问，返回倒数第1个元素
print(x1[-2]) # 从数组的反向索引开始访问，返回倒数第2个元素

# 访问二维np数组
print(x2)
print(x2[0,0])
print(x2[2,0])
print(x2[2,-1])

# 指定索引，给数组赋值
x1[0] = 3.14159 #如果插入一个浮点数到整形数组，浮点数会被截断为整形
print(x1)

x2[0, 0] = 12
print(x2)

# 访问一维np数组的一个片


