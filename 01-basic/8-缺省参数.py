# 延时函数
import time
print("a")
time.sleep(1)  # 暂1秒后执行下一步
print("b")


# 局部变量
# 在函数内定义的变量，称为局部变量，该变量只在定义中的函数内有效
# 形参也是局部变量

# 全局变量
# 在函数外面定义的变量即为全局变量，全局变量所有函数都能调用
# 然而全局变量并不能在函数中直接修改
# 如果一定要在函数中修改全局变量，则需要在该函数中声明
# 即 global “变量”
# 使用全局变量有可能会取到意想不到的值，尽量少用global


# 在函数中可以通过列表或者元组或字典的方式返回多个值
def test():
    a = 1
    b = 2
    c = 3
    return [a,b,c]  # 不加方括号则默认返回元组

list = test()   # 一定要先建一个变量存储函数的值
aa = list[0]
bb = list[1]
cc = list[2]
print(aa,bb,cc)
print("="*50)


# 缺省参数,指调用函数时可以有参数不传
def test(a,b,c = 3.5):  # 缺省参数一定要放在最后
    print(a,end=" ")
    print(b,end=" ")
    print(c)

test(11,22)  # 参数c不传，则取默认值3.5

def test2(a,b,c=12,d=23):
    print(a,end=" ")
    print(b,end=" ")
    print(c,end=" ")
    print(d)

test2(5,11,d=47)  # 多个缺省参数时，可以指定给其中一个参数传数据

# 不定长参数
def test3(a,b,*args,**kwargs):  # *args元组  **kwargs字典
    print(a,end=" ")
    print(b,end=" ")
    print(args,end=" ")
    print(kwargs)

test3(11,22,33,44,55,66,aa="asd",bb=234)
# 所传数值超过函数所需，多余数值会被存储到最后一位元组中
# 类似于aa="asd"这样的赋值则会被存到字典中
A = [55,77,99]
B = {"aa":400,"bb":600}
C = (90,80,70)
test3(["asd","asdffaf"],c = 11,d = 23,*C,*A,**B)
# 当元组/列表/字典在当作实参传递的时候，如果前面有一个*/**，表示对其进行解包
# 如果有缺少参数没传，会自动取被解包的元组/列表中第一个元素补上，字典不行
