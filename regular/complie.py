# python中使用re模块的时候,python会先编译正则表达式,然后才会拿它去匹配字符串,所以可以手动预编译,提高效率

import re

re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())
