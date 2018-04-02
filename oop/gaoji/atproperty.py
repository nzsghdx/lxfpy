# @property的使用

class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value <0 or value>100:
            raise ValueError('score must be between 0~100!')
        self._score=value

# 赋值和取值的时候分别调用两个方法

s=Student()
s.set_score(60)
print(s.get_score())
# s.set_score(9999)



class Student2(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value <0 or value>100:
            raise ValueError('score must be between 0~100!')
        self._score=value

    #这里只有一个@property,没有设置age.setter,age是只读属性
    @property
    def age(self):
        return 2018-self._birth

# 赋值和取值调用的是同一个方法


s2=Student()
# 这里括号变成了等于号,人家说变成了一个可控的属性操作
s2.score=80
print(s2.score)
