# 面向对象变成,所有的内容都可以看作是对象,可以往对象里存东西(属性),还可以读取
# object表示Student是继承它的
class Student(object):
    # __init__方法可能相当于java中的构造器
    def __init__(self,name,score):
#        self.name=name
        # 私有变量:
        self.__name=name
#        self.score=score
        # 私有变量:
        self.__score=score
    
    # 和java中一样,应该是因为面向对象吧,有getter和setter方法
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 设置set方法的时候可以对设置的属性值进行判断
    def set_name(self,name):
        self.__name=name

    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')

    # self相当于对象
    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))

# 类写好了之后,需要对象

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()
# 暂时不知道为什么没有效果
#bart.set_score=99
# 我真是个人才
bart.set_score(99)
bart.print_score()
