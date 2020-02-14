# 异常处理：try...except...捕获异常
try:
    # print(a)  # 有问题的代码在try中不会报错
    open("aaa.txt")  # try中只能测试一条有问题的代码，当检测到时，程序就结束
except FileNotFoundError as result:  # 同时将原来的报错信息保存在result变量中
    print("没有找到该文件%s" % result)
    print(type(result))
except(NameError, FileNotFoundError):  # 一个except捕获多种异常
    print("asdasd")
except Exception as error:  # 可以捕获所有异常
    print("该变量没有定义%s" % error)  # 当try中代码出错时，执行这条代码
except:  # 默认的except必须放在最后
    print("hahahah")
else:
    print("没有异常")  # 当try中没有异常代码，才会执行
finally:
    print("最后执行")  # 不管try中有没有异常，异常有没有被捕获，最后一定会执行，常用于清除内存


# 异常的传递
def test1():
    print(1)
    print(a)  # 异常的根源
def test2():
    print(2)
    test1()
def test3():
    try:  # 会一直被传递到最后，其实是会一直追溯异常直到根源
        print(3)
        test2()
    except Exception as error:
        print(error)

test3()


# 抛出自定义异常
class ShortInputException(Exception):  # 定义一个继承于Exception的子类，这个类就是自定义的异常类
    def __init__(self,length,atleast):
        self.length = length
        self.atleast = atleast


try:
    s = input("请输入->")
    if len(s) < 5:
        raise ShortInputException(len(s),5)  # raise用来引发刚才定义的异常
except ShortInputException as result:  # 这里的result相当于一个对象，它指向刚才定义的异常类
    print("你输入的字符长度为%d，至少需要输入%d个字符"%(result.length,result.atleast))
else:
    print("没有错误")


try:
    a = int(input("请输入1或0"))
    b = 0
    print(a/b)
except:
    if a == 1:
        print("error")
    else:
        raise  # 将捕获到的异常抛出
