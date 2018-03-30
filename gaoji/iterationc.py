# 判断时候是可迭代的对象

from collections import Iterable

print("'abc':",isinstance('abc',Iterable))

print("[1,2,3]:",isinstance([1,2,3],Iterable))

print("123:",isinstance(123,Iterable))
