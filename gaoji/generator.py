# 首先定义一个普通的generator

s=(x*x for x in range(5))
print('打印generantory:\n')
print(s)
print('遍历generator:\n')
for x in s:
    print(x)

print('\n')

print('函数中定义generator:\n')

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

f=fib(10)

print('fib(10)',f)

print('')

for x in f:
    print(x)

print('上方是打印x:\n')
g=fib(5)
while 1:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
