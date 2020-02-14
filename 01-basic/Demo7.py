# 在一个函数中调用另一个函数，即函数的嵌套 调用
# 函数的定义 要放在调用的代码前
# 两个函数的名字相同时，只有最后一个函数会生效（会覆盖第一个函数）

# 小练习： 写一个函数打印一条横线  打印自定义行数的横线
'''
def striping(i):  # 法一
    a = 0
    while a < i:
        print("-" * 60)
        a += 1


striping(1)


def line():  # 法二：如果一开始需求没有明确，而是后期增加的，则不建议修改原函数
    print("-" * 60)


def printLine():  # 而应该在不改变原函数的基础上新增函数来满足新的需求
    n = int(input("打印几条线？"))
    a = 0
    while a < n:
        line()  # 直接调用原函数
        a += 1


printLine()
'''


# 小练习2：写一个函数求三个数的和   写一个函数求三个数的平均值
def sum():
    a, b, c = input("请输入三个数(用逗号隔开)：").split(",")  # 这样输入得到的是一个列表
    d = int(a) + int(b) + int(c)  # 由于类型是str，所以要转成int才能计算
    return d


def average():
    d = sum()  # 返回的值一定要用到这个函数并把值存起来
    e = d / 3
    return e


e = average()
print(e)
