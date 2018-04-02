class Student(object):
    # 限制可以绑定的属性,但是只对当前类的实例起作用,不限制子类
    __slots__=("name","age")

s=Student()
s.name="Dalao"

s.age=21
# 报错 'Student' object has no attribute 'score'
# s.score=100
print(s.name)

class GStudent(Student):
    pass

g=GStudent()
# 不限制子类是否存在没有声明的属性
g.score=100
print(g.score)
