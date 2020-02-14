# 单例模式: 即一个类只有一个对象实例
class Test(object):
    def __init__(self):  # 创建完对象后默认调用，因此是在new方法后面
        self.num = 100
        print("---init---")
    def __str__(self):  # 相当于对这个类做注解
        return "---str---"
    def __new__(cls):  # new方法是用来完成创建一个对象的，首先调用
        print("---new---")
        return super().__new__(cls)  # 重写new方法
        # super().xxx 可以调用父类方法,这里的父类指的是object
        # 所以也可以用object.xxx
    def __call__(self):  # 该方法可以使类直接被调用，执行该方法
        print("---call---")
    def __del__(self):  # 最后被调用
        print("---del---")


a = Test()
a()  # 类中只要有call方法就可以直接调用对象名 来使用call方法
print(a.num)
print(a)



class Singleton(object):
    __instance = None
    __first_init = False
    def __new__(cls,i):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self,i):
        if not self.__first_init:
            print(i)
            self.__first_init = True


c = Singleton(10)
b = Singleton(20)  # 这个对象指向的仍是前一个对象c
print(c)
print(b)

# 通过new方法来决定对象的创建与否
