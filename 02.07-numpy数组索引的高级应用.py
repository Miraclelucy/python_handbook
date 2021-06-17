import numpy as np
rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
print("x:  ",x)
print("[x[3], x[7], x[2]]:  ",[x[3], x[7], x[2]])

# 一维数组索引
index = [3, 7, 4]
print("x[index]:  ",x[index])

# 二维数组索引
index2 = np.array([[3, 7],
                [4, 5]])
print("x[index2]:  ",x[index2])

X = np.arange(12).reshape((3, 4))
print("X:  ",X)
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
print("X[row, col]:  ",X[row, col])  # 第1个值是X[0, 2], 第2个值是X[1, 1],第3个值是X[2, 3]
print("X[row[:, np.newaxis], col]:  ",X[row[:, np.newaxis], col])
print("row[:, np.newaxis] * col:  ",row[:, np.newaxis] * col)

# np.newaxis的作用就是增加一个维度
x1 = np.array([1, 2, 3, 4, 5])
x1_new = x1[:, np.newaxis]
print("x1_new:  ",x1_new)
x1_new = x1[np.newaxis,:]
print("x1_new:  ",x1_new)

# 混合索引
print("X:  ",X)
print("X[2, [2, 0, 1]]:  ",X[2, [2, 0, 1]])
print("X[1:, [2, 0, 1]]:  ",X[1:, [2, 0, 1]])
mask = np.array([1, 0, 1, 0], dtype=bool)
print("XX[row[:, np.newaxis], mask]:  ",X[row[:, np.newaxis], mask])


