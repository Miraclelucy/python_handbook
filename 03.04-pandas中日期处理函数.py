import pandas as pd
from datetime import timedelta,datetime
from pandas.tseries.offsets import DateOffset
from dateutil.relativedelta import relativedelta

# 1. date_range 获取2个日期之间的所有日期
sdate = '20221110'
edate = '20221115'
datelist = pd.date_range(datetime.strptime(str(sdate), "%Y%m%d").date(),datetime.strptime(str(edate), "%Y%m%d").date()-timedelta(days=1),freq='d').strftime("%Y%m%d")
datedf = datelist.to_frame(index=False,name='TIME')
print(datedf)

# 2. date_range 获取2个日期之间的所有月份
monthdf = pd.date_range('20211101', periods=14, freq=DateOffset(months=1)).map(lambda x: str(x).replace('-', '')[0:6]).to_frame()
monthdf.columns = ['monthlist']
print(monthdf)

# 3. 给定日期获取相隔2年的年份
end_month = (datetime.strptime('20220501', "%Y%m%d") + relativedelta(years=2)).strftime("%Y0101")
print(end_month)
