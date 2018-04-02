# 两种导入方式都行
# import duotai
from duotai import Animal
from duotai import Dog

# 依然不明白为什么把duotai文件中的方法都输出了

a=list()
# 同样两种调用方式都可以
#b=duotai.Animal()
#c=duotai.Dog()
b=Animal()
c=Dog()

print(isinstance(a,list))
# 不知道为什么输出中把dog和cat中的方法打印了一遍
print(isinstance(b,Animal))
#print(isinstance(b,duotai.Animal))
#print(isinstance(c,duotai.Dog))
print(isinstance(c,Dog))
# 因为dog继承了animal类,所以dog也属于animal类型
print(isinstance(c,Animal))
