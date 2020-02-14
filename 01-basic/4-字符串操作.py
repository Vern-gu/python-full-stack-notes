name = "A B C D E F G"
print(name[2:6:1])  # 前两位之差即字符长度，第一位为起始，第二位终点，第三位步长
for temp in name:
    print(temp)
# i = 0
# while i < 6:
#     print(name[i])
#     i += 1
print(len(name))
print("=" * 8)

# 字符串操作 find & index
str = "hello world and Python and me 哈哈"
print(str.find("and"))  # 此时会返回12，index用法和find一样，index找不到时会报错，
# find找不到时会返回-1
print(str.rfind("and"))  # 从右边开始找，返回23，rindex同理
# 取文件后缀
fileName = "popkart.kartrider.exe.zip"
print(fileName.rfind("."))  # 返回21
print(fileName[21:])

# 字符串操作 count
print(str.count("and"))  # count主要作用为计数，找到该字符在变量中出现的次数
print(len(str))  # 获取字符串长度
print(str.count("and", 23, 29))  # 从第23开始到第29，找and
# 字符串操作 replace
print(str.replace("me", "YOU"))  # 可已将原字符串中的me替换为YOU（只要有me，就都替换）
print(str)  # 但这不是赋值，str中的字符串是不会改变的
print(str.replace("and", "YOU", 1))  # 只替换一次
# 字符串操作 split
print(str.split("and"))  # 将里面特定的字符作为逗号分隔
# capitalize 把字符串的第一个字符大写
# title 把字符串的每一个单词首字母大写
# startswith & endswith
print(str.startswith("hello"))  # 检查该字符串是否以“hello”开头，返回结果true或者false
print(str.endswith("hello"))  # 检查该字符串是否以“hello”结尾，
# lower 把字符串中的所有大写字符转换为小写
# upper 把字符串中的所有小写字符转换为大写
# ljust居左 & rjust居右 & center
str.center(50)  # 对于一行50个字符长度的屏幕进行居中
print(str.rjust(50))  # 右对齐，使用空格填充至长度50的新字符串
# strip & lstrip & rstrip 删除字符串两端/左边/右边的空白字符
a = "\n\tjust we   \t\n"
print(a.strip())  # 返回“just we”
# partition  以关键字分割成三部分，rpartiton是从右边开始
print(str.partition("and"))  # and前，and，and后，split会将关键字删去，而partition不会
# splitlines 按字符串中的换行符来提取分割
# isalpha 判断字符串中字符是否都为字母，返回true或者false
print(str.isalpha())  # 返回False
# isdigit 判断字符串是否为纯数字
# isalnum 判断是否都为字母或数字
print(name.isalnum())  # 返回True
# isspace 判断字符串中是否只有空格
# join 在每个字符串后都插入一个关键字变成一个新的字符，注意要加入的字符写在join前面
print("name")
name = name.split(" ")
char = "_"
print(char.join(name))
# 帮助 help(a.join) 可查看join的功能

# 小练习 给定一个字符串aStr，返回使用空格或者“\t”分割后的倒数第二个字串
aStr = "my name is Vern Gu"
temp = aStr.split()
print(temp[-2])

pstr = "Hello World!!"
def myReplace(str, oldStr, newStr):
    return str.replace(oldStr, newStr)

print(myReplace(pstr,"Hello", "Bye"))


