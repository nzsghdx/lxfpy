# 匹配邮箱

import re

# 三个条件,必须要有@和.,@前面必须有至少一个字符,@和.之间至少有一个字符

# 三个条件可以把邮箱地址分为五部分

# 还可以改进,但是我不想写了

print(re.match(r'^(\w+)\@(\w+)\.(\w+)$','someone@gmail.com').groups())
print(re.match(r'^(\w+\.\w+)\@(\w+)\.(\w+)$','bill.gates@microsoft.com').groups())
