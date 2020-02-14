# 迭代器：可以被next()函数调用并不断返回下一个值的对象称为迭代器
# 可以直接作用于for循环的对象统称为可迭代对象，如生成器等
num = (a for a in range(10))  # 这就是一个生成器，生成器一定是迭代器
print(num)
print(type(num))
for temp in num:
    print(temp)

# 判断一个对象是否可迭代
from collections import Iterable
print(isinstance(num,Iterable))  # iterable即可迭代，用isinstance来判断是否可迭代
from collections import Iterator
li = [1,2,4,6]
print(isinstance(li,Iterator))  # 列表可迭代但不是可迭代对象，判断是否为可迭代对象
print(isinstance(num,Iterator))  # 生成器是可迭代对象
a = iter(li)  # iter 函数使其转化为可迭代对象
print(type(a))
print(isinstance(a,Iterator))
# 总结：可迭代未必是可迭代对象，生成器一定是可迭代对象，可迭代对象=迭代器

print("="*50)





# 闭包：在一个函数内再定义一个函数，并且这个函数用到了外边函数的变量
# 那么这个函数以及用到的一些变量称之为闭包
def test(num):
    print(num)
    def test_in(num_in):
        print(num_in + num)
        return num+num_in+num
    return test_in  # 调用外函数时，使其指向内函数

test(1)  # 不会调用函数内部的函数，等价于test_in
bibao = test(1)
bibao(2)  # 调用内部函数，不会执行外部函数
print(bibao(3))  # print中的"bibao(3)"会先执行调用一下，再打印返回值
print("============================闭包应用↓============================")
def line(a,b):  # 闭包的应用
    def line_x(x):
        return a * x**2 + b  # 设置了一个二次函数，即y=ax2+b
    return line_x

line1 = line(1,2)  # 设置了该函数为y=x2+2
print(line1(2))  # 当x=2时，可得y=6
