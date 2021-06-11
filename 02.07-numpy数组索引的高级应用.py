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
print("X[row, col]:  ",X[row, col])
