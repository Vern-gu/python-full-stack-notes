# 可变数据类型：列表、字典  改变其数据后id不变
# 不可变数据类型： 数字、字符串、元组  改变其数据后id改变
# 字典的key值是不可变类型
a = [11,22]
print(id(a))
a = a + a  # 把原来的列表拿来重新生成一个新列表在新列表里改 id改变
print(id(a))
b = [44,33,22]
print(id(b))
b += b  # 在原来列表的基础上直接改 id不变
print(id(b))

# 阶乘
'''
result = 1
i = 1
while i<=100:  # 法一：使用while 循环
    result *= i
    i += 1
print(result)
'''
# 一个函数调用了它自己本身，则这个函数称为递归函数
def test(num):  # 法二：使用递归函数
    if num > 1:
        return num * test(num - 1)  # return是将结果返回到调用的地方
    else:
        return 1

a = test(10)
print(a)

def asd(num):
    if num>=1:
        r = num*asd(num-1)
    else:
        r = 1
    return r  #

b = asd(10)
print(b)