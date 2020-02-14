# 装饰器：其本质是在调用方法时，在此方法前增加其他需求
def w1(func):
    print("装饰中")

    def inner(*args,**kwargs):
        print("---验证---")
        a = input("enter a num")
        if a == "00":
            print(type(func))
            re = func(*args,**kwargs)  # 调用原函数，用(*args,*kwargs)可以随便传递多个参数而不需要更改
            return re  # 若原函数有返回值，则装饰器内也需要返回参数
        else:
            print("验证失败")
    return inner

@w1  # 等价于 f1 = w1(f1)
def f1(a):
    print("----%d----"%a)
@w1  # 只要python解释器执行到了这个代码，就会立刻执行装饰，而不是等到调用时才装饰
def f2(b,c,d,f):
    print("----%d,%d,%d,%d----"%(b,c,d,f))
@w1
def f3():
    print("----f3----")
    return "return of f3 "

f1(1)  # 在调用前，已经进行装饰了
f2(2,3,4,5)
f = f3()
print(f)
# 当有多个装饰器装饰同一个函数时，最后的一个装饰器先装饰，但调用顺序还是从上到下调用
# 通用装饰器，可以接受或不接受参数，可以返回或不返回函数值，以上装饰器就是一个通用装饰器
def func_arg(arg):  # 设置带参数的装饰器时，需要在装饰器外再套一层函数以接收参数
    def func(fun):
        def func_in():
            print(arg)
            fun()
        return func_in
    return func

@func_arg("sad")  # 为装饰器传递参数，可以在运行时设置不同的功能
def fun():
    print("-=-=-=-=-=-=-")

fun()

print("===================作用域、动态==================")

# 作用域
locals()  # 查看所有局部变量，返回一个字典
# python使用LEGB的顺序来查找一个符号对应的对象
# locals -> enclosing function(闭包) -> globals -> builtins(内嵌函数)
import types
class Person(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("%s正在吃"%self.name)

def run(self):
    print("%s正在跑"%self.name)

p1 = Person("小红")
p1.eat()
p1.age = 13  # 动态添加属性
p1.run = types.MethodType(run,p1)  # 动态添加方法
p1.run()  # 这时，Person类就添加了一个实例方法
# 由于python是动态语言，因此可以随时添加属性
# 这时我们可以使用__slots__变量，来限制class实例能添加的属性
class Animal(object):
    __slots__ = ("name","age")  # 限制Animal类能添加的实例属性仅为name和age

cat = Animal()
cat.name = "猫"
cat.age = "2 months"
# cat.sex = "female"  # 该属性无法添加

print("===============生成器=============")
b = (x*x for x in range(100))  # 普通的生成器

def fib():  # 斐波那契数列的生成器
    a,b = 0,1
    for i in range(10):
        temp = yield a  # 只要在函数内部添加了yield，这个函数就不会被执行，而变成了一个生成器
        print(temp)
        a,b = b,a + b

a = fib()  # 生成器对象

next(a)
a.__next__()  # 可以用这两种方法取到生成器中的值，这两种方式是等价的
a.send("value")  # send与next都可以使yield继续执行下去，但是send会给予yield一个值，而next不会

# 多任务，分为协程，进程，线程，其中协程运行速度最快
def test1():   # yield的应用，多任务——协程
    while True:
        print("---1---")
        yield None
def test2():
    while True:
        print("---2---")
        yield None

t1 = test1()
t2 = test2()
'''
while True:
    t1.__next__()
    t2.__next__()
# 先调用test1，打印1，到yield停止，开始调用test2，打印2，再到yield停止，再调用test1循环。。。
'''