import pandas as pd
from pandas.tseries.offsets import DateOffset
import numpy as np

import datetime
from dateutil.relativedelta import relativedelta

# 1. isin函数的应用
# 告诉你没有isnotin，它的反函数就是在前面加上~
df = pd.DataFrame(np.random.randn(4, 4), columns=['A', 'B', 'C', 'D'])
df['E'] = ['a', 'a', 'c', 'b']
df.D = [0, 1, 0, 2]
df[df.E.isin(['a', 'd']) & df.D.isin([0, ])]

print(df)
print(df[df.E.isin(['a', 'd']) & df.D.isin([0, ])])

# 2. drop函数 使用drop，它不改变原有的df中的数据，而是返回另一个dataframe来存放删除后的数据
df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
df.drop(['B', 'C'], axis=1)  # 删除列
df.drop(columns=['B', 'C'])  # 删除列
df.drop([0, 1])  # 按索引删除

df.dropna()  # 将所有含有nan项的row删除

# 3. stack函数 堆叠
# 构造数据
data = pd.DataFrame(np.arange(12).reshape((3, 4)) + 100,
                    index=pd.Index(['date1', 'date2', 'date3']),
                    columns=pd.Index(['store1', 'store2', 'store3', 'store4'])
                    )
data2 = data.stack().reset_index()
print(data2)
print(data2.index)

# 4. 截取函数
string="Hello world!"
string1=string[:-1]    #去掉尾部一个字符
string2=string[1:-1]   #去掉头尾各一个字符
string3=string[1:]    #去掉头部一个字符

print("23060401^欧菲".find("23060401") > 0)
print('23060401^欧菲' in '23060401^欧菲' )
