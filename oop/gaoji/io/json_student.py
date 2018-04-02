import json

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

s=Student("Bob",20,88)
# 以上是一个普通的python类

# 通过一个方法,把s对象转换为dict类型
def student2dict(s):
    return{
            'name':s.name,
            'age':s.age,
            'score':s.score
    }


# 两个语句是同样的功能,第二句是调用实例的__dict__属性转换为dict类型
#print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))


# 反序列化
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str='{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(json_str,object_hook=dict2student))
