import modular

# modular.test()
# 当要使用导入的模块的函数时，要使用模块名.方法()，而这样太麻烦了
# 因此可以使用 from 模块名 import * 导入该模块所有方法
from modular import *  # 导入多个方法用逗号隔开即可
test()

# 可以用__all__来定义“*”中的方法范围
# __all__ = ["方法1","方法2","方法3","方法4"]
# 这时再用from 模块名 import *时，就会导入以上列表中的方法


# 包：在文件夹中创建一个名为“__init__.py”的文件，
# 这时python解释器会把这个文件夹认为python的一个包
print(variable)


# 列表推导式
a = range(1,10)  # 左开右闭区间[1,10)
print(type(a))
for i in a:
    print(i,end = ' ')
print("")

b = [x for x in range(1,20,2)]  # [1.20)，从1开始每次+2取值，取到19
print(b)

for i in range(5):  # 从0到4循环5次，以后可以用这种方式快速进行多次循环
    print(i)

c = [x for x in range(11) if x%2 == 0]  # 遍历range中的数，只有满足if条件，才会取值
print(c)

d = [x for x in range(4) for y in range(3)]  # 嵌套循环，外循环为range(3) 重复range(4)三遍
print(d)

# 集合中的数据不能重复
e = set(d)  # 集合可用来去重
print(e)


# 如果缺省参数是一个可变类型那么这个参数只能被初始化一次
def practice(a,b = []):
    b.append(a)
    return b
list1 = practice(10)
list2 = practice(123,["a","b","c"])
list3 = practice("a")  # list1与list3所指向的都是局部变量b，因此当list3改变时list1也同时改变
print(list1)
print(list2)
print(list3)


# 一个函数，给定参数n，生成含有n个元素值为1~n的列表，元素顺序随机，但不重复
from random import randint
def newList(n):
    li = []
    while True:
        a = randint(1,n)
        if a not in li:
            li.append(a)
        if len(li) == n:
            return li

li = newList(10)
print(li)

