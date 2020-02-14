# 类装饰器
class Test(object):
    def __init__(self,func):
        print("初始化")
        print("func name is %s"%func.__name__)
        self.__func = func
    def __call__(self):
        print("---装饰其中的功能---")
        self.__func()

@Test  # 解释器运行到这里就会自动调用Test类的init方法
def test():
    print("test")

test()
# 如果类中有call方法，就可以直接调用类，否则只能 类丶方法
# 目前为止学到过的默认方法;init,new,del,str,call
# __mro__类的调用先后顺序
# __slots__限制类中可以创建的属性
# __getattribute__当要访问类中的属性或方法时，会调用此功能，看作是属性或方法的拦截器


# 元类：就是用来创建类的“东西”，元类就是类（对象）的类
# python中万物皆对象，即使是一个类也是对象，一个数字也是对象
def run(self):
    print("%s跑得贼快"%self.name)
Person = type("Person",(),{"age":23,"name":"Tom","run":run})  # 创建一个元类（类名，（继承），{属性，方法...}）
ming = Person()
print("%s的年龄是%d"%(ming.name,ming.age))
ming.run()


def upper_attr(class_name,class_parents,class_attrs):
    newAttr = {}  # 这个方法是将所有属性名改写为大写
    for name,value in class_attrs.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value
    return type(class_name,class_parents,newAttr)

class Foo(object,metaclass=upper_attr):  # 使用metaclass可以让类创建成自己想要的东西
    # __metaclass__ = upper_attr  (python2 中用法)
    home = "rip"

print(hasattr(Foo,"home"))
print(hasattr(Foo,"HOME"))
f = Foo()
print(f.HOME)
# 元类运作原理：1.拦截类的创建 2.修改类 3.返回修改后的类


print("===================垃圾回收==================")
# 垃圾回收机制：Garbage Collection（GC机制），当一个对象的引用计数为0时，它就会被删除
# 小整数对象池：[-5,257)之间的整数对象是python提前建立好的，不会被垃圾回收，单个字符也同理
# 大整数对象池：每一个大整数均创建一个新的对象，引用为0则删除
# intern机制：不含空格等特殊字符的字符串，只要值相等，他们的地址也相等，当该字符串的引用为0是就会被删除
# 零（隔）代收集机制（次要）：每过一段时间会将零代上互相引用的对象的计数减一，如有互相引用 内存就会被释放

import gc
import sys
gc.get_count()  # 获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表，即查看0-2代分别清理了多少次
gc.get_threshold()  # 也可在其中设置值，自定义其清理频率
# 新创建的对象数减去已经清理的对象数大于700就会零代清理；每清理10次零代就会清理一次一代
a = "asdasd"
sys.getrefcount(a)  # 查看一个对象被引用的次数


print("===================内建属性==================")
# __getattribute__(self,obj) 属性访问拦截器，当要访问属性时，此功能率先被调用
class Test(object):
    def __init__(self,subject):
        self.subject1 = subject
        self.subject2 = "sbjct"
    def __getattribute__(self,subject):  # 这里输入的变量是属性名或方法
        if subject == "subject1":
            print("access forbidden")
            return "redirect %s"%subject
        else:  # 如果这两行被注释，则无法访问其他属性或方法
            return object.__getattribute__(self,subject)  # 拦截完以后重新定向应有的属性或方法
    def show(self):
        print("---Test over---")

t = Test("python")
print(t.subject1)
print(t.subject2)
t.subject3 = "rwby"
print(t.subject3)
t.show()

# map(function,sequence[,sequence,...])函数，输入要使用的函数，再输入函数的参数，返回对应的值
map(lambda x: x+x,[1,2,3])  # 其结果为[2,4,6]
map(lambda x,y: x*y,[1,2,3],[2,3,4])  # 结果为[2,6,12]
def function(x,y,z):
    a = x**2+y*x-z
    return a
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
ret = map(function,l1,l2,l3)
print(list(ret))

# filter()筛选函数，用法与map类似，只是返回的结果为调用为True的元素（不是函数值）
filter(lambda x: x%2,[1,2,3,4])  # 返回结果为[1,3]

# reduce()函数，reduce依次从sequence中取一个元素，和上一次调用function的结果做参数再次调用function
from functools import reduce
reduce(lambda x,y: x+y,["a","b","c","d"])  # 结果为abcd
reduce(lambda x,y: x+y,["a","b","c","d"],"e")  # 此时先取e给x，a给y，结果为eabcd

# sorted函数，列表排序
sorted([1,23,4,32,4,2,5,12])  # 从小到大排序
sorted([1,23,4,32,4,2,5,12],reverse=1)  # 从大到小排序，字母也可以按照ASCII码大小排序

# set()集合
a = set("abc")
b = set("bcd")
c = a&b  # 求交集 bc
d = a|b  # 求并集 abcd
e = a-b  # 差集 a ，是将a集合中的元素减去b中也有的元素，取a中剩余的元素
f = a^b  # 对称差集 ad  ，将两集合中共有的元素去除后，取两集合中剩下的元素
print(f)

print("================python常用标准库===============")
# builtins内建函数默认加载、os操作系统接口、sys Python自身的运行环境、
# json 编码和解码（多用于爬虫）、hashlib加密算法

import hashlib  # 哈希算法，多用于加密
m = hashlib.md5()
print(m)
m.update(b"fantastic")
print(m.hexdigest())


print("================python常用扩展库===============")
# requests使用了urllib3、urllib基于http的高层库、scrapy爬虫、beautifulsoup4 HTML/XML的解析器。这些库都用于爬虫
