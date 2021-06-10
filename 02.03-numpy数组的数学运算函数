import numpy as np
import time


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

x1 = np.arange(5)
x2 = np.arange(1, 6)

