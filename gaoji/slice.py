#!/usr/bin/env python3

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print('stupid :',[L[0],L[1],L[2]])

# 取出特定个数的元素:利用循环读取并且存入到一个临时的list中

r=[]

n=3

for i in range(n):
    r.append(L[i])
    
print(r)


# 切片实现读取

print("切片表示不包括最后一个")

print('Slice L :',L[0:3])

print('从第一个开始读取可以省略0:',L[:3])

print('Use -1 read the end number:',L[-1])

print('从倒数第二个到倒数第一个-2:-1 :',L[-2:-1])

print('从倒数第二个到最后一个-2: :',L[-2:],'\n')

print('从倒数第四个到最后一个:',L[-4:],'\n')
