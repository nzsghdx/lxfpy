# python允许多重继承,java可以使用接口的方式来实现类似于多继承的功能

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 狗
class Dog(Mammal,Runnable):
    pass
# 蝙蝠
class Bat(Mammal,Flyable):
    pass
# 鹦鹉
class Parrot(Bird,Flyable):
    pass
# 鸵鸟
class Ostrich(Bird,Flyable):
    pass


