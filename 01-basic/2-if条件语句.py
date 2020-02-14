"""
# if条件语句,if语句后别忘了加冒号,判断是==，赋值是=
age = int(input('请输入年龄：'))
if age >= 18:
    print("可以进入", end="")
    print('欢迎光临')
else:
    print("禁止")

# 交通违规扣分练习
score = int(input("请输入当前的分数"))
guize = int(input("闯红灯请输入1，违停请输入2"))
if guize == 1:
    score -= 6
if guize == 2:
    score -= 3
if score <= 0:
    print("你需要重新学习")
else:
    print("你现在的分数为：%d分" % score)
    # print("你当前的分数为："+str(score)+"分")

# 逻辑运算符and or not
user = input("请输入用户名：")
password = input("请输入密码：")
if user == "Vern" and password =="123456":
    print("登陆成功！")

num = input("请输入0-9：")
if not(num < '5' and num > '7'): #if "7" >= num >= "5":
    print("good")

# elif 判断语句
x = int(input("输入星期1.2.3..."))
if x == 1 :
    print("星期一")
elif x == 2:
    print("星期二")
elif x == 3 :
    print("星期三")
elif x == 4 :
    print("星期四")
elif x == 5 :
    print("星期五")
else :
    print("今天休息")
"""
# if嵌套语句练习：猜拳游戏。用到了random模块，模块一般放在代码最前面
import random
while True:
    player = int(input("请猜拳（石头1 剪刀2 布3）（按9退出）"))
    com = random.randint(1,3)
    if player == 9:
        break
    if player == com:
        if com == 1 :
            print("对方也出了石头，平局")
        elif com == 2:
            print("对方也出了剪刀，平局")
        elif com == 3:
            print("对方也出了布，平局")
    elif (player == 1 and com == 2) or (player == 2 and com == 3) or (player == 3 and com == 1):
        if com == 1 :
            print("对方出了石头，YOU WIN，你真强")
        elif com == 2:
            print("对方出了剪刀，YOU WIN，666啊")
        elif com == 3:
            print("对方出了布，YOU WIN，你是狗啊")
    else:
        if com == 1:
            print("对方出了石头，YOU LOSE，啧啧菜的抠脚")
        elif com == 2:
            print("对方出了剪刀，YOU LOSE，辣鸡")
        elif com == 3:
            print("对方出了布，YOU LOSE，彩笔")
