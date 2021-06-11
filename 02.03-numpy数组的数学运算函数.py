import numpy as np
import time
from scipy import special


# 尽量减少使用loop循环
# loop循环与矢量计算
def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output


values = np.random.randint(1, 100, size=100)
start_time = time.process_time()
print(compute_reciprocals(values))  # 可以看到数据量很大时，loop循环耗时约1.4s
# print(1.0 / values) # 直接矢量计算几乎耗时很小
end_time = time.process_time()
print('cost time : {} s'.format(end_time - start_time))

# 两个数组之间的矢量操作
x1 = np.arange(5)
x2 = np.arange(1, 6)
y = np.arange(5) / np.arange(1, 6)

# 基础运算函数
x = np.arange(2, 6)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)  # 整除(e.g., 3 // 2 = 1)
print("-x     = ", -x)
print("x ** 2 = ", x ** 2)  # 求幂
print("x % 2  = ", x % 2)  # 取余
print("np.add(x, 2) = ", np.add(x, 2))

y = np.array([-2, -1, 0, 1, 2])
print("abs(y) = ", abs(y))
print("np.absolute(y) = ", np.absolute(y))
print("np.abs(y) = ", np.abs(y))

z = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
print("np.abs(z) = ", np.abs(z))

# 三角函数
theta = np.linspace(0, np.pi, 3)
print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

x = [-1, 0, 1]
print("x         = ", x)
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))

# 指数和对数函数
x = [1, 2, 3]
print("x     =", x)
print("e^x   =", np.exp(x))
print("2^x   =", np.exp2(x))
print("3^x   =", np.power(3, x))

x = [1, 2, 4, 10]
print("x        =", x)
print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))

x = [0, 0.001, 0.01, 0.1]
print("exp(x) - 1 =", np.expm1(x))
print("log(1 + x) =", np.log1p(x))

# 特殊的函数
# Gamma 函数（广义阶乘）和相关函数
x = [1, 5, 10]
print("gamma(x)     =", special.gamma(x))
print("ln|gamma(x)| =", special.gammaln(x))
print("beta(x, 2)   =", special.beta(x, 2))

# 误差函数（高斯积分）
# its complement, and its inverse
x = np.array([0, 0.3, 0.7, 1.0])
print("erf(x)  =", special.erf(x))
print("erfc(x) =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))

# 更多函数- 特殊化输出
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print("np.multiply(x, 10, out=y) ", y)

y = np.zeros(10)
np.power(2, x, out=y[::2])
print("np.power(2, x, out=y[::2]) ", y)

# 聚合
x = np.arange(1, 6)
print("x ", x)
print("np.add.reduce(x) ", np.add.reduce(x))
print("np.multiply.reduce(x) ", np.multiply.reduce(x))
print("np.add.accumulate(x) ", np.add.accumulate(x)) # 存储累加的中间计算结果
print("np.multiply.accumulate(x) ", np.multiply.accumulate(x)) # 存储累乘的中间计算结果

# 创建乘法表
print("np.multiply.outer(x, x) ", np.multiply.outer(x, x))
