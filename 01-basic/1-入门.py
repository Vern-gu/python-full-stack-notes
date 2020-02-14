'''
多
行
注
释
'''
# coding=utf-8(python3已经支持中文)"#是单行注释"
print("hello world")
print('我的老婆是' + '新垣结衣')
# 定义变量
name = "Vern"
age = 23
print(name)
print(age)
# 使用这个变量
age = 22
print(age)
# 代码是从上往下执行的
# type可以知道其后面括号里变量的类型
print(type(age))
print(type(name))
# \n 换行；\t 制表符=tab键
print('\tname\n\tage')
# 只能相同类型的变量一起输出，不同类型的变量一起输出时要把类型统一
print(name + str(age))
print("我叫%s，我今年%d岁" % (name, age)) # 格式符号也有不同类型，常用的是%s和%d
print("my name is {},{} years old this year".format(name,age))
a = 0.35
print('中奖概率是：' + str(a))
# 将两个输出结果显示在一行,一般print之后都会默认带一个end='\n'即默认换行
print('aaaaa', end='')
print('bbbbb')
# 输入,input输入的内容都是字符串类型；python2中为raw_input()
userName = input('请输入用户名：')
print('用户名为%s，请确认'%userName)
# 分别赋值,以及变量的数据交换
a,b = 10,20 # 分别赋值
a,b = b,a # 数据交换，相较于其他语言不需要再定义第三个变量
print('='*(a+b))
num1 = input('请输入第一个数：')
num2 = input('请输入第二个数：')
result = int(num1)+int(num2)
print('%s + %s = %d'%(num1,num2,result))