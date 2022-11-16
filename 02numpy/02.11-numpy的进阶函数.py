import numpy as np

# np.triu(arr, k=0),返回矩阵的上三角,最后返回的是矩阵
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('---a---')
print(a)
b = np.triu(a, 0)
print('---np.triu(a, k=0)---')
print(b)

# np.triu_indices_from(arr, k),返回方阵的上三角矩阵的索引
index_arr = np.triu_indices_from(a, k=0)
print('---np.triu_indices_from(a, k=0)---')
print(index_arr)
print('---a[index_arr]---')
print(a[index_arr])

index_arr = np.triu_indices_from(a, k=1)
print('---np.triu_indices_from(a, k=1)---')
print(index_arr)
print('---a[index_arr]---')
print(a[index_arr])

# np.triu_indices(n, k),返回方阵的上三角矩阵的索引
index_arr = np.triu_indices(3, k=0)
print('---np.triu_indices(3, k=0)---')
print(index_arr)
print('---a[index_arr]---')
print(a[index_arr])

index_arr = np.triu_indices(3, k=1)
print('---np.triu_indices(3, k=1)---')
print(index_arr)
print('---a[index_arr]---')
print(a[index_arr])

index_arr = np.triu_indices(2, k=0)
print('---np.triu_indices(2, k=0)---')
print(index_arr)
print('---a[index_arr]---')
print(a[index_arr])

index_arr = np.triu_indices(2, k=1)
print('---np.triu_indices(2, k=1)---')
print(index_arr)
print('---a[index_arr]---')
print(a[index_arr])
