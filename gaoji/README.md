# 恩,高阶函数挺不容易的.

- 小意思,想想你不会的时候别人是怎么嘲讽你的.

记录Map/Reduce部分的学习过程,暂时觉得还挺难的.

### Reduce示例:

````

from functools import reduce
def add(x,y):
	return x+y
reduce(add,[1,2,3,4,5])
15

```

>reduce接收两个参数,一个是函数,一个是序列,把第一个函数作用在序列上.

reduce小例子:
把队列`[1,2,3,4,5]`转换为整数:

```

form functools import reduce
#第一个参数是函数
def add(x,y):
	return x*10+y
#第二个参数是整数
reduce(add,[1,2,3,4,5])

```


### Map学习示例:

```

#定义函数
def f(x):
	return x*x
#使用map
r=map(f,[1,2,3,4,5])
#得出一个iterable惰性序列,列出,返回一个list
list(r)

```

>Map同样是两个参数,第二个参数队列作为第一个函数的参数传入第一个参数.

Map另一个小示例:

```

#使用内置函数,把list中所有的int类型的数字转换为字符串
list(map(str,[1,2,3,4,5]))

```


### Map/Reduce的异同

- 相同点呢
 - 两个参数
 - 第一个参数是函数
- 不同点
 - 不同点就是计算方式不同了,上方已简单总结
  >太嫩,暂时不知道怎么总结


### 复杂玩法

map和reduce同时使用: 

1.把str转化为int

```

#导入reduce
from functools import reduce
#reduce所调用方法,把队列中的数字组合成整数
def fn(x,y)
	return x*10+y
#map所调用方法,奴知道什么意思,我想玩一会了,暂时不想深究
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
reduce(fn,map(char2num,'13579'))

```
2.str2int

3.lambda简化





