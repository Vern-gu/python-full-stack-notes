# 模块的存储路径被保存在一个列表中
import sys
sys.path
print(sys.path)
# sys.path.append("./")  # 也可以通过appand在其中添加路径

# 以下方法，手动重新导入模块（模块有修改，一般都要重开才能生效）
from imp import *
# reload(模块名)


# is 、 == 的区别
a = [11,22]
b = [11,22]
a == b  # 返回True
a is b  # 返回False
#  ==用于判断两者的内容是否相等，is由于判断两者是否指向同一个内存地址


# 浅拷贝：对于一个对象的顶层拷贝，即拷贝了引用而没有拷贝内容
a = [1,2,3]
b = a  # 这就是浅拷贝，没有开辟一个新的内存将值放入内存中，而只是引用
# 深拷贝
import copy
c = copy.deepcopy(a)  # 此时c的内存地址与a不相同，即c = [1,2,3]
d = copy.copy(a)  # cpoy的复制会根据原来变量的变化而变化，如果复制的是不可变类型，则不会开辟新的内存地址
a.append(4)
print(a,b,c,d)  # a,b都指向a，因此a变化时，b也会跟着改变

print("==========================property=========================")
# 私有化
# xx：共有变量
# _x：单前置下划线，私有化属性或方法，无法通过from xx import * 导入，但可以通过import xx导入
# __x：双前置下划线，无法在外部直接访问该属性
class Test(object):        # 使用以下方法来访问或修改私有属性
    def __init__(self):
        self.__num = 100
    @property  # property 的第一种使用方法
    def num(self):
        return self.__num
    @num.setter
    def num(self,value):
        self.__num = value


t = Test()
print(t.num)
t.num = 12  # 相当于调用了t.setter()
print(t.num)  # 相当于调用了t.getter()


class Test2(object):
    def __init__(self):
        self.__xx = 10
    def getter(self):
        return self.__xx
    def setter(self,value):
        self.__xx = value
    value = property(getter,setter)  # property属性,相当于将两个方法封装成了一个属性（第二种使用方法）

t2 = Test2()
print(t2.value)  # 等价于print(t2.getter())
t2.value = 15  # 等价于t2.setter(15)
print(t2.value)  # 等价于print(t2.setter())