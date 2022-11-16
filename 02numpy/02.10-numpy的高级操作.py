import numpy as np

#一维数据
x =  np.array(['晴', '晴', '阴', '雨', '雨', '雨', '阴', '晴', '晴', '雨', '晴', '阴', '阴', '雨'])
#x =  np.array([1,2,3])
print(x)
print(x.shape)

y = np.expand_dims(x,axis=1)
print("y: ",y)
print("y.shape: ", y.shape)

# 二维数据
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)
print(x.shape)

y = np.expand_dims(x, axis=0)
print("y: ",y)
print("y.shape: ", y.shape) # 怎么数维度？看每层括号有几个元素，那一层就是几维的

y = np.expand_dims(x, axis=1)
print("y: ",y)
print("y.shape: ", y.shape)

y = np.expand_dims(x, axis=2)
print("y: ",y)
print("y.shape: ", y.shape)
