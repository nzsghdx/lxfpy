import functools 

# int是偏函数中的函数参数,base=2是关键字参数(**kwargs),还可以有个无名参数*args,但是无名参数必须要在关键字参数前面,这里没有设置无名参数,所以没有报错,否则报错
int2=functools.partial(int,base=2)

# 这里的10是无名参数(*args)
max2=functools.partial(max,10)

print(max2(2,3,5))
print(max2(2,3,50))

print(int2('1000000'))

print(int2('1000000',base=10))
