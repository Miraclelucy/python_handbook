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
print(x1[0])  # 从数组的正向索引开始访问，返回倒数第1个元素
print(x1[4])  # 从数组的正向索引开始访问，返回倒数第5个元素
print(x1[-1])  # 从数组的反向索引开始访问，返回倒数第1个元素
print(x1[-2])  # 从数组的反向索引开始访问，返回倒数第2个元素

# 访问二维np数组
print(x2)
print(x2[0, 0])
print(x2[2, 0])
print(x2[2, -1])

# 指定索引，给数组赋值
x1[0] = 3.14159  # 如果插入一个浮点数到整形数组，浮点数会被截断为整形
print(x1)

x2[0, 0] = 12
print(x2)

# 访问一维np数组的一个片
# numpy.arange(start, stop, step, dtype = None)
# start —— 开始位置，数字，可选项，默认起始值为0
# step —— 步长，数字，可选项， 默认步长为1
x = np.arange(10)
print("x : ", x)
print("x[:5] : ", x[:5])  # 前5个元素
print("x[5:] : ", x[5:])  # 索引5以及后面的元素
print("x[4:7] ", x[4:7])  # 包含开始索引4 不包含索引7
print("x[::2] ", x[::2])  # 索引从0开始 step=2
print("x[1::2] ", x[1::2])  # 索引从1开始 step=2
print("x[::-1] ", x[::-1])  # 所有元素反转
print("x[5::-2] ", x[5::-2])  # 倒着数的索引是5开始的数 step=2
print("x[4::-1] ", x[4::-1])  # 倒着数的索引是4开始的数 step=1

# 访问多维np数组
print("x2 : ", x2)
print("x2[:2, :3]  ", x2[:2, :3])  # 第0,1行和第0,1,2列
print("x2[:3, ::2]  ", x2[:3, ::2])  # 第0,1,2行和第0,2列
print("x2[::-1, ::-1]  ", x2[::-1, ::-1])  # 所有行反转，所有列反转

# 访问np数组的行和列
print("x2[:, 0]  ", x2[:, 0])  # 所有行，第0列
print("x2[0, :]  ", x2[0, :])  # 第0行，所有列
print("x2[0]  ", x2[0])  # 第0行

# np数组的复制 copy()
x2_sub_copy = x2[:2, :2].copy()  # 数组的复制
print("x2_sub_copy ", x2_sub_copy)
x2_sub_copy[0, 0] = 42
print("x2_sub_copy ", x2_sub_copy)
print("x2 : ", x2)  # 给copy的数组赋值，不改变原数组

# 改变np数组的形状
grid = np.arange(1, 10).reshape((3, 3))
print("grid : ", grid)
x4 = np.array([1, 2, 3])
print("x4.reshape((1, 3)): ", x4.reshape((1, 3)))
print("x4.reshape((3, 1)): ", x4.reshape((3, 1)))

# 数组连接和拆分
# 一维数组的连接
m = np.array([1, 2, 3])
n = np.array([3, 2, 1])
print("np.concatenate([m, n]): ", np.concatenate([m, n]))
z = [99, 99, 99]
print("np.concatenate([m, n, z]): ", np.concatenate([m, n, z]))

# 二维数组的连接
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("np.concatenate([grid, grid]): ", np.concatenate([grid, grid]))
print("np.concatenate([grid, grid], axis=1): ", np.concatenate([grid, grid], axis=1))

# 混合数组的连接 vstack()和hstack()
print("np.vstack([grid, m]): ", np.vstack([grid, m])) # 垂直方向上连接数组
p = np.array([[99],
              [99]])
print("np.hstack([grid, p]): ", np.hstack([grid, p])) # 水平方向上连接数组

# 分割数组
# split(ary, indices_or_sections, axis=0)
# indices_or_sections:如果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置
# axis：沿着哪个维度进行切向，默认为0，横向切分
s = [1, 2, 3, 99, 99, 3, 2, 1]
s1, s2, s3 = np.split(x, [3, 5])
print(s1, s2, s3)

# 水平分割和垂直分割
grid = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(grid, [2])
print("grid ",grid)
print("upper ",upper)
print("lower ",lower)
left, right = np.hsplit(grid, [2])
print("left ",left)
print("right ",right)
