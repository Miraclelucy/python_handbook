# seaborn中的countplot函数的用法
import seaborn as sns
import matplotlib.pyplot as plt

# 从seaborn默认的库中读取一个数据集，即读取tips.csv文件
tips_df = sns.load_dataset('tips')
# 统计单个类别变量
sns.countplot(x='sex', data=tips_df)
# 画图
plt.show()
