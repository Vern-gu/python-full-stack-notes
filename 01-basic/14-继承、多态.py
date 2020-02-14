# 保护对象的属性
# 有两种方法可以改变对象的属性：
# 对象名.属性名 = 数据   （直接修改） 不安全
# 对象名.方法名()         (间接修改)
class Protect:
    def __init__(self,num):
        self.__num = num  # 只要属性名前有两个下划线，即表示为私有属性
        # 私有属性不能在外部被调用  对象名.属性名
    def setNum(self,num):
        self.__num = num
    def test(self):
        print(self.__num)

a = Protect(11)
a.__num = 10  # 此时修改的属性为假象，实际类中的属性没有修改
print(a.__num)  # 无法直接获取，程序会报错
a.test()
a.setNum(20)  # 只能通过调用方法来修改和获取数据
a.test()
# 在方法名前加两个下换线同理，该方法无法被外部调用
# python使用的方法是将这个私有的属性或方法的名字改了，所以无法被调
print(a._Protect__num)  # 这是__num的真属性名
print(dir(Protect))  # 查看Protect类中所有的方法


# __del__ 方法：当删除一个对象后，python解释器就会默认调用这个方法
# 要养成好清内存的习惯

# 类 单继承
class Animal(object):  # 定义了一个父类
    def run(self):
        print("----跑----")
    def __num(self):
        print(123)

class Cat(Animal):  # 定义了一个子类
    pass
    # def test(self):
        # self.__num()  # 调用父类的私有方法是不可行的

class Dog(Animal):  # 要写父类的类名
    def run(self,speed):  # 当子类的要求的方法不满足时可以重写
        if speed == 1:
            super().run()  # 重写时可以使用super()来调用父类功能
        else:
            print("----奔----")

xiaomao = Cat()
xiaogou = Dog()
xiaomao.run()  # 继承就可以调用父类里的方法
xiaogou.run(0)
# xiaomao.test()  # 注意：在父类中的私有属性和方法，在子类中是无法调用的


# 类 多继承：一个子类继承了复数个父类
class Bird:
    def fly(self):
        print("----飞----")
    def animal(self):
        print("鸟")

class Fish:
    def swim(self):
        print("----游----")
    def animal(self):
        print("鱼")

class Feiyu(Bird,Fish):  # 同时继承了两个类
    pass

xiaofeiyu = Feiyu()
xiaofeiyu.fly()
xiaofeiyu.swim()
xiaofeiyu.animal()  # 当子类调用的方法，两个父类都有时，会优先调用第一个父类

print(Feiyu.__mro__)  # 使用__mro__可以查看类的调用先后顺序


# 多态：定义时的类型和运行时的类型不一样
# 面向对象的三个要素：封装、继承、多态


# 在__init__方法中定义的属性为实例属性，实例属性是跟着对象走的
# 在方法外部定义的属性称为 类属性，类属性跟着类走
class Cat:
    num = 0  # 类属性
    def __init__(self):
        self.name = "mew"  # 实例属性

mao = Cat()
print(Cat.num)  # 可以通过对象访问类属性，但一般都用类来访问类属性
# 如果类属性的名字和实例属性的相同，那么通过对象去取的时候往往会取到实例属性的值
Cat.num = 10  # 修改类属性一定要通过类来访问

# 类方法和静态方法
class Test:
    num = 0
    def __init__(self):
        self.a = 1
    @classmethod  # 修饰器
    def setNum(cls,newNum):  # 类方法
        cls.num = newNum
    @staticmethod
    def printTest():  # 静态方法
        print("---------")


a = Test()
print(Test.num)
Test.setNum(20)  # 也可以用对象名来调用
print(Test.num)
Test.printTest()  # 也可以用对象来调
# 使用类名是无法访问实例属性或方法的
