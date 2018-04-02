# 从datatime模块中导入datatime类
from datetime import datetime,timedelta


now=datetime.now()
print(now)
print(type(now))

# 这里不能用04,前面不能带0..
# 默认构造顺序是年月日时分秒
dt=datetime(2018,4,1,16,13,55)
print(dt)
# 转换为timestamp,timestamp是现在的时间减去1970-01-01的秒数
dttt=dt.timestamp()
print(dttt)
# 转换为日期
print(datetime.fromtimestamp(dttt))
# 转换为格林威治标准时区时间,与北京的东八区小了八个小时
print(datetime.utcfromtimestamp(dttt))
# str转换为日期
cday=datetime.strptime('2018-4-1 16:23:55','%Y-%m-%d %H:%M:%S')
print(cday)
# a表示星期,b是月份,d是几号,H/M是时/分
print(now.strftime('%a,%b %d %H:%M'))


print(now+timedelta(hours=10))
print(now-timedelta(days=1))
print(now+timedelta(days=2,hours=12))

# 太多了,没啥乱用,再见!
