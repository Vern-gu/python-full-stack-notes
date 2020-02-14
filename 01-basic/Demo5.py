list = ["Jack", "John", "Tom", 3.14, 54]  # 列表中可以存储不同类型的字符串，列表中的内容称为元素
for temp in list:  # 将列表中全部内容都打印一遍称为遍历
    print(temp)
# 花名册练习
nameList = ["Jack", "John", "Tony", "Lisa", "Vern"]
# i = 0
# while i < len(nameList):
#     if myName == nameList[i]:
#         print("your name in list")
#     i += 1
findFlag = 0  # 定义一个变量，当被改变时说明目标被找到
while True:
    myName = input("input your name please(exit with 0):")
    for name in nameList:
        if myName == name:
            findFlag = 1  # 变量被改变
            break  # 只要找到了就结束循环，可以提升效率
    if findFlag == 1:
        print("your name in list")
        findFlag = 0  # 使变量复原以进行下一次循环
    elif myName == str(0):
        break  # 退出程序
    else:
        print("inexistence")

