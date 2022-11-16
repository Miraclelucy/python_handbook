# 1. list列表的拼接
print([1] + [2])
print([1] + [2, 3])

# 2. pop()和pop(0)
list1 = ['Google', 'Runoob', 'Taobao']
list_pop = list1.pop()
print(list_pop)
list_pop = list1.pop(0)
print(list_pop)

# 3. path和path[:]
res = []
res1 = []
path = [1, 2]
res.append(path)
res1.append(path[:])
path.append(3)
print("path ", res)
print("path[:] ", res1)

# 4. join()函数
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b")  # 字符串序列
print(s1.join(seq))
print(s2.join(seq))


# 5. map()函数
def square(x):
    return x ** 2


res3 = list(map(square, [1, 2, 3, 4, 5]))
print("res3 ", res3)

# 6. 根据值找索引
inorder = [9, 3, 15, 20, 7]
p1 = inorder.index(9)
p2 = inorder.index(3)
print("p1 ", p1)
print("p2 ", p2)

# 7. 比如有一个变量a，那么if not a和if a is None两者有区别吗？
def fun():
    return None


a = fun()
if not a:
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')

a = []
if not a:   #逻辑运算
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')

# 8. 计算字符串长度
print(len("digits"))

# 9. enumerate() 函数
# 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序
candidates = [2,3,6,7]
enum = enumerate(candidates)
print(list(enum))

# 10. 初始化一个全0，长度为10的列表
res = [0] * 10
print(res)

# 基础运算符
# * 代表乘法 ** 代表乘方
# // 代表取整除 - 返回商的整数部分（向下取整）
# % 代表取模 - 返回除法的余数

a = 21
b = 10
c = a * b
print("a * b的值为：", c )


c = a % b
print("a % b的值为：", c )

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print("a**b的值为：", c )

a = 10
b = 5
c = a//b
print("a//b的值为：", c )
