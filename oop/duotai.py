class Animal(object):
    def run(self):
        print('Animal is running...')

    def eat(self):
        print("Eating meat...")

class Dog(Animal):
#    print("Dog is running...")
    def run(self):
        print("Dog is running...")

    def eat(self):
        print("Dog Eating meat...")

class Cat(Animal):
#    print("Cat is running...")
    def run(self):
        print("Cat is running...")

dog=Dog()
# 重写之前,调用的是父类的方法,重写之后,调用自己的方法
dog.run()
dog.eat()

cat=Cat()
cat.run()
cat.eat()
