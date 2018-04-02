import re

# 这里能在b和c之间取出来一个空格:无法识别连续的空格,两个空格会打印出来一个
print('a b  c'.split(' '))

# 这里正常,re大法好,正则表示至少一个空格
print(re.split(r'\s+','a b  c'))

# 是根据空格/逗号分隔
print(re.split(r'[\s\,]+','a, b, c  d'))

# 正则表达式表示空格/逗号/分号分隔
print(re.split(r'[\s\,\;]+','a,b;; c  d'))
