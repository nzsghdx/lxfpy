#!/usr/bin/env python3

L=[]
n=1
while n<=99:
    L.append(n)
#    print(L)
    n=n+2
#    print(n)

# print(L)

# 取出L中前一半的元素

print(len(L))

m=1
i=0

# m从1开始,到半数25正好25个数
while m<=(len(L)/2):
    print(L[i])
    i=i+1
    m=m+1
#    print('m:',m)

# print('fm:',m)

