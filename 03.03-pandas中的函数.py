import pandas as pd
import numpy as np
### count函数方法的使用
### 计算每列或每行的非NA单元格。

df = pd.DataFrame({"Person":
                    ["John", "Myla", "Lewis", "John", "Myla"],
                    "Age": [24., np.nan, 21., 33, 26],
                    "Single": [False, True, True, True, False]})

print(df.count()) # 对于每个列，non-NA/null条目的数量。
print(df.count(axis='columns')) # 对于每个行，non-NA/null条目的数量。
