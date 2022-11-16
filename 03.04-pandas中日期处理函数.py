import pandas as pd
from datetime import timedelta,datetime

# 1. date_range 获取2个日期之间的所有日期
sdate = '20221110'
edate = '20221115'
datelist = pd.date_range(datetime.strptime(str(sdate), "%Y%m%d").date(),datetime.strptime(str(edate), "%Y%m%d").date()-timedelta(days=1),freq='d').strftime("%Y%m%d")
datedf = datelist.to_frame(index=False,name='TIME')
print(datedf)
