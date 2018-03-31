# -*- coding: utf-8 -*-

# 那个星号是干吗用的..

# arg表示的是什么,我不懂的原来那么多吗
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

f=lazy_sum(1,3,5,7,9)
f1=lazy_sum(1,3,5,7,9)

print((f()==f1()))
#这里会输出f,返回的是一个函数
print("输出函数:\n")
print(f)
print("调用函数:\n")
print(f())
