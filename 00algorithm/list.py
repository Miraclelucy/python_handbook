import bisect

# 1.列表的二分查找插入算法
data = [1, 7, 3, 8, 5]
data2 = [2, 9, 10]
data.sort()
print(data)
i = bisect.bisect(data, 6) # 返回插入的索引，实际没有插入
print(i)
print(data[:3] +data2)
