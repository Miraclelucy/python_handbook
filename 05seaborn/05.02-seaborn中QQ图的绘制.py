import warnings
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

df = pd.read_csv('./data/StudentsPerformance.csv', engine='python')
df = df[['math score', 'reading score', 'writing score']]
df['score_tol'] = df['math score']+df['reading score']+df['writing score']

# 直接调包画QQ图 验证学生总分数是否符合正态分布
df = df.sort_values('score_tol', ascending='false').reset_index(drop=True)
res = stats.probplot(df['score_tol'], dist='norm', plot=plt)
plt.show()

# 手动画Q-Q图 来实现检验1列数据是否符合正态分布
# 1.当2列行数相同时，直接用排序后的两列数据花散点图
data = np.random.randn(1000)
df_n = pd.DataFrame(data, columns=['vals']).sort_values('vals', ascending='false').reset_index(drop=True)

sns.regplot(x = df_n['vals'], y= df['score_tol'],ci=None, color='b', line_kws={'color':'r'})
plt.show()

# 2.当2列行数不同时，直接用排序后的两列数据花散点图 我们接下来取0到100的500个分位数
ls1 = sorted([np.percentile(df_n['vals'], i) for i in np.linspace(1,100,500)],reverse=True)
ls2 = sorted([np.percentile(df['score_tol'], i) for i in np.linspace(1,100,500)],reverse=True)

sns.regplot(x = pd.Series(ls1), y= pd.Series(ls2), ci=None, color='b', line_kws={'color':'r'})
plt.show()

# 手动画Q-Q图 来实现检验2列数据是否符合同一分布
# 1.当2列行数相同时，直接用排序后的两列数据花散点图
ls3 = sorted(df['math score'])
ls4 = sorted(df['reading score'])
sns.regplot(x = pd.Series(ls3), y= pd.Series(ls4), ci=None, color='b', line_kws={'color':'r'})
plt.show()

# 2.当2列行数不同时，直接用排序后的两列数据画散点图
df1 = df.sample(n=800)
ls1 = sorted([np.percentile(df1['math score'], i) for i in np.linspace(1,100,500)],reverse=True)
ls2 = sorted([np.percentile(df['reading score'], i) for i in np.linspace(1,100,500)],reverse=True)
sns.regplot(x = pd.Series(ls1), y= pd.Series(ls2), ci=None, color='b', line_kws={'color':'r'})
plt.show()

