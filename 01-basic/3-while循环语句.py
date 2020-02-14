"""
# while循环语句，只要条件满足会一直执行下去
a = 1
while a <= 8:
    print('+', end='')
    a += 1

# 小练习，输出1~100中的偶数
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

# 1~100的偶数累计和
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print("和为：%d" % sum)

# while嵌套九九乘法表，外圈控制行数，内圈控制列数
i = 1
while i <= 9:
    j = 1
    while j <= i:
        k = 0
        k = i * j
        print("%d * %d = %d\t"%(j,i,k),end = '')
        j += 1
    print("")
    i += 1
"""
# for in 循环语句。格式： for 临时变量 in 字符串:
name = "Vern"
for temp in name:
    print(temp)
# 用下标索引的方式(下标从0开始)可以使while实现for的功能
i = 0
while i < 4:
    print(name[i])
    i += 1
print("=" * 10) # 分隔符
# 切片：变量名[起始:长度]或者[起始:结束:步长]
name = "abcd1234"
print(len(name))  # 获取变量的长度
print(name[0:5])  # 获取从零开始到第五位的字符串
print(name[::2])  # 隔一位取一个字符
print(name[::-1])  # 反取
print(name[-2])  # 直接取倒数第二位
print(name[0:-1])  # 只能取到第一位到倒数第二位同[-2]
