import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
### count()函数方法的使用
### 计算每列或每行的非NA单元格。

df = pd.DataFrame({"Person":
                    ["John", "Myla", "Lewis", "John", "Myla"],
                    "Age": [24., np.nan, 21., 33, 26],
                    "Single": [False, True, True, True, False]})

print(df.count()) # 对于每个列，non-NA/null条目的数量。
print(df.count(axis='columns')) # 对于每个行，non-NA/null条目的数量。

### value_counts()函数方法的使用
index = pd.DataFrame([3, 1, 2, 3, 4, np.nan], columns=['age'])
idx = index.value_counts() # 返回的是一个series
ax=plt.subplot(1,2,1)
idx.plot(kind='pie',autopct='%1.1f%%',shadow=True) # 画饼图
plt.show()
print(idx)
