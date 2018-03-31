# 使用filter过滤器求素数

#素数就是...算了

# 想了一下,这应该是传说中的算法,怕了怕了


# 从3开始的一个无限序列生成器,因为用到了yield
# 执行到yield部分的时候,中止一下,输出一下,下次调用继续从3开始计算
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

# 筛选函数
# 恩,不怎么懂lambda,以前了解过现在全忘了

def _not_divisible(n):
    return lambda x:x%n>0

# 一步看不懂,步步看不懂?
def primes():
    yield 2 #首先输出一下2
    it=_odd_iter()
    while True:
        n=next(it) #然后不断的生成3及更多的素数
        yield n #然后输出一下?
        #然后使用函数过滤结果
        it=filter(_not_divisible(n),it)

# 遍历无限数列primes,给定参数100,100应该被带入到了_not_divisible(n)函数的n参数
for n in primes():
    if n<100:
        print(n)
    else:
        break


# 很迷
