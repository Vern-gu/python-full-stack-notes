'''
# 匿名函数：没有名字的函数lambda, 适用于比较简单的函数
sum = lambda a, b: a + b      # a,b为传入的参数
print(sum(11, 22))  # 匿名函数不能直接调用print


def test(a, b, c):  # 作为内置函数的参数
    return c(a, b)


result = test(5, 9, lambda x, y: x - y)
print(result)


a = [{"num":23,"age":17},{"num":10,"age":16},{"num":15,"age":20}]
a.sort(key = lambda k:k['num'],reverse = True)  # sort函数还可以给列表中字典排顺序
print(a)

g_a = [15,16]
def A():
    g_a.append(17)  # 全局变量如果是可变类型则在函数中可以直接修改，不需加global
    print (g_a)
A()
'''

# 文件：用于记录数据，防止数据丢失
# f = open("test.txt","r")  # 以只读的方式打开一个文件，a追加，w写入
# b = f.read()  # 一次把文件读完（不会分行），之后无法再读取
# b = f.read(5)  # 表示一次读五个字节
# f.close()  # 关闭文件
# readlines 可以按照行的方式（分行）把整个文件中的内容进行一次性读取，返回迭代器
# readline 逐行读取数据

# 文件的复制操作
def copy():
    fileName = input("请输入要复制的文件名：")
    file = open(fileName,"r")
    temp = fileName.rfind(".")
    fileCopy = open(fileName[:temp]+"[副本]"+fileName[temp:],"w")  # 创建一个副本文件
    # for fileLine in file.readlines():  # 按行的方式读取文件内容
        # fileCopy.write(fileLine)  # 再用for循环写入副本文件

    while True:   # 第二种方法，逐行复制内容，程序不容易崩溃
        fileLine = file.readline()
        fileCopy.write(fileLine)
        if fileLine == "":
            break
    file.close()
    fileCopy.close()

copy()


# 补充：
with open("test.txt","r") as f:
    f.read()
# 用with as 方法可以省略一步文件的关闭操作
'''
f = open("test.txt")  # 不加r,w,a 则默认是r  ,open还可以打开一个带路径的文件
f.tell()  # 可以告诉用户现在文件读到了哪里，即定位的方式
f.seek(偏移量，方向)  # from方向只能取（0，1，2）
# seek即将光标移至相应的地方

# 重命名文件
import os
os.rename("test.txt","newFile.txt")  # (old,new)旧名字，新名字
# 删除文件
os.remove（）  # (文件名)
# 创建文件夹
os.mkdir("新文件夹")
# 获取当前目录
os.getcwd()
# 改变默认目录
os.chdir("./") 将自己所在位置转移至其他目录
# 获取目录列表
os.listdir("./")
# 删除文件夹
os.rmdir()

'''

'''
# 批量修改文件名
import os
fileName = os.listdir("./test")
print(fileName)
for name in fileName:
    os.rename("./test/"+name,"./test/"+ name[6:])
'''