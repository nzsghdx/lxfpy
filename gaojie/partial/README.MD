# 偏函数(Partial)

>作用就是设置默认值,把一个函数的参数给固定住,并且返回一个新的函数,调用新函数会更简单更简洁.

使用的时候需要先导入:import functools
然后使用eg:int2=func.partial(int,base=2)
