'''
# 排序（sort，reverse）
# 用sort排序
nums = [1, 4, 2, 3]
print(nums)
nums.sort()  # sort默认为由小到大排序,如果是单词则会按照首字母的asc码大小排序
print(nums)
nums.sort(reverse=True)  # 使用参数reverse=True则为由大到小排序
print(nums)
nums = [1, 4, 2, 3]
nums.reverse()  # reverse可以直接将原列表中的元素反向排序
print(nums)


# 所谓函数就是将具有独立的功能的代码块封装成一个整体重复使用（def前不能加tab）
# 1 定义函数: def 函数名（函数要执行的代码）,定义的函数不会被执行
def printCode():
    """第一段
    python
    函数"""
    "换行用三引号，不换行用双引号"  # 函数的文档说明
    print("-" * 30)
    print("=" * 30)
    print("+" * 30)
    print("~" * 30)


# 2 调用函数：函数名（）
printCode()
help(printCode)  # 使用help就可以看到该函数的文档说明


# 3 函数参数
def sumOf3Num(num1, num2, num3):  # 形式参数
    print(num1 + num2 + num3)


sumOf3Num(12, 69, 56)  # 实际参数


# 4 返回值：程序中函数完成一件事后，最后给调用者的结果（return）
def add(a, b):
    return a + b  # 没有return的话，最后调用时，将无法得出结果。遇到return函数就结束


result = add(22, 33)  # "add(22,33)"就可以看作是函数中return后面的"a+b"结果
print(result)


# 5 函数可分为四种：1.无参数 无返回 2.无参数 又返回 3.有参数 无返回 4.有参数 有返回
'''
# 小练习：学生管理系统
def printMenu():  # 打印菜单
    print("\t\t学生管理系统 V4.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4 保存学生信息")
    print("5 显示所有学生信息")
    print("0.退出系统")
    print("=" * 30)


def inputInfo():  # 获取学生信息
    # global newName  # 使该变量变为全局变量而非局部变量，这样就可以被主函数调用
    # global newPhone  # 全局变量所有函数都能调用改变不够安全
    newName = input("请输入姓名：")
    newPhone = input("请输入手机号：")
    return {"name":newName,"phone":newPhone}


def modifyInfo():  # 修改学生信息
    j = int(input("请输入要修改的序号："))
    newInfo = inputInfo()
    stuInfo[j - 1]["name"] = newInfo["name"]
    stuInfo[j - 1]["phone"] = newInfo["phone"]


def save():  # 保存数据
    file = open("temp.txt", "w")
    file.write(str(stuInfo))
    file.close()


def recover():  # 恢复数据
    file = open("temp.txt","r")
    temp = file.read()
    global stuInfo
    if temp != "":
        stuInfo = eval(temp)  # 当temp为空时，eval函数会出错
    file.close()


stuInfo = []
def main():
    recover()  # 再次打开程序时，可以不丢失数据
    while True:
        printMenu()
        key = int(input("请输入序号："))
        if key == 1:  # 添加学生信息
            newInfo = inputInfo()
            stuInfo.append(newInfo)
            save()
        elif key ==2:  # 删除学生信息
            j = int(input("请输入要删除的学生序号："))
            del stuInfo[j-1]
            save()
        elif key == 3:  # 修改学生信息
            modifyInfo()
            save()
        elif key == 5:  # 显示当前名单
            print("序号\t姓名\t电话")
            i = 1
            for temp in stuInfo:
                print("%d\t\t%s\t\t%s" % (i, temp["name"], temp["phone"]))
                i += 1
        elif key == 4:  # 保存数据
            save()
            print("保存完毕")
        elif key == 0:  # 退出
            break


main()
# 对以上实例第89行global的说明：
# 在全局中定义了一个全局变量后如：a = [11,22]
# 尽管a是一个列表是可变类型
# 但是在一个函数中，如：
# def test()
    # a = [33,44]
# 在其他函数调用test()后a的值还是[11,22]
# 这时的a其实是一个函数中的局部变量（虽然和全局变量同名）
# 需要在函数中用global声明，a的值才可以改变
# 只有用诸如a.append()的函数时，才不需要用global


