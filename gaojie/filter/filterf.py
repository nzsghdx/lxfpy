# First filter file

def is_odd(n):
    return n%2==1

L=list(filter(is_odd,[1,2,4,5,6,9,10,15]))
#以前还不知道可以这么玩,把list赋值给一个变量,然后使用print函数输出
#我还考虑的很久,后来抱着试试看的态度...
print(L)
