class MyObject(object):
    def __init__(self):
        self.x=9

    def power(self):
        return self.x*self.x

obj=MyObject()

print(hasattr(obj,'x'))
print(hasattr(obj,"y"))
print(getattr(obj,"x"))
setattr(obj,"y",19)
print(hasattr(obj,"y"))
print(getattr(obj,"y"))
# 获取的同时如果不存在,就取默认值
print(getattr(obj,"z",404))
print(hasattr(obj,'power'))
print(getattr(obj,'power'))
# 不加括号表示获取对象,加上括号表示方法
print(getattr(obj,'power')())
