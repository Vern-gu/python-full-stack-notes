# 列表的常见操作为增加元素、删除元素、更改元素、查看元素
# 1.1 通过append向列表添加元素,append添加的元素都在最后
fruits = ["apple","banana","peach"]
fruits.append("orange")
print(fruits)
# 1.2 通过insert添加元素，insert(index,object)在指定位置index前插入object
fruits.insert(2,"pear")  # 在peach前插入pear
print(fruits)
# 1.3通过extend添加元素，可以将两个列表融合，append与insert都不行
vegetables = ["tomato","potato"]
fruits.extend(vegetables)
print(fruits)
fruits.insert(0,vegetables)
print(fruits)
print(fruits[0][1][3])  # 列表中包含列表时要取小列表中的数据可以用多个方括号
'''# 小练习：添加名字
nameList = ["Tom","Tony","Vern"]
name = input("enter your name please")
password = 0
code = "999"
code = "999"
flag = 0
for temp in nameList:
    if temp == name:
        flag = 1
        break
if flag == 1:
    print("your name in list")
else:
    print("inexistence")
    password = input("enter password:")
    if password == code:
        nameList.append(name)
        print("added")
    else:
        print("error")
print(nameList)
'''
# 2 更改元素 列表、字典、集合中的元素是可以更改的；而字符串和元组中的数据不可更改
fruits[0][1],fruits[0][0] = "Mary","Kimi"
print(fruits)
# 3.1 查看元素存在与否：in & not in
print("strawberry" in fruits)
print("strawberry" not in fruits)
# 3.2 用index，count查找，和字符串中的操作一样
print(fruits.index("apple",0,2))  # 左闭右开区间[0,2）中查找，index没找到会报错,列表中的列表元素无法找到
print(fruits.count("apple"))
# 4 用del，pop，remove删除列表中的元素
# del 根据下标进行删除
del fruits[-1]
print(fruits)
# pop 只删除最后一个元素
fruits.pop()
print(fruits)
# remove 根据元素的值进行删除
fruits.remove(["Kimi","Mary"])  # 通过remove删除了列表中的一个列表
print(fruits)

# 小练习：花名册管理系统
nameList = ["Vern"]
while True:
    usage = input("\t请输入数字：\n（1.添加名字 2.删除一个名字 3.修改一个名字 4.查询一个名字 按其他任意数字退出）")
    if usage == "1":
        name = input("请输入要添加的名字：")
        nameList.append(name)
        print(nameList)
    elif usage == "2":
        name = input("请输入要删除的名字：")
        nameList.remove(name)
        print(nameList)
    elif usage =="4":
        name = input("请输入查询的名字：")
        if name in nameList:
            print("该名字在名册中")
        else:
            print("不在名册中")
    elif usage == "3":
        print(nameList)
        i = int(input("要修改第几个名字？"))
        name = input("请输入修改的名字：")
        nameList[i-1] = name
        print(nameList)
    else:
        break