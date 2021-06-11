import numpy as np
import matplotlib.pyplot as plt

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print("a + b ", a + b)
print("a + 5 ", a + 5)

M = np.ones((3, 3))
print("M ", M)
print("M + a ", M + a)

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
print("a ", a)
print("b ", b)
print("a + b ", a + b)

M = np.ones((2, 3))
a = np.arange(3)
print("M ", M)
print("a ", a)
print("M + a ", M + a)

# 广播机制的应用
X = np.random.random((10, 3))
print("X ", X)
print("X.mean(0) ", X.mean(0))
print("X.mean(1) ", X.mean(1))

# 画二维函数
# x and y have 50 steps from 0 to 5
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
f = np.sin(x)
plt.plot(x, f)
plt.show()
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5],
           cmap='viridis')
plt.colorbar()
plt.show()
