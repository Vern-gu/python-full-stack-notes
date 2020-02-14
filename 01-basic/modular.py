def test():
    print("test函数内程序")



variable = "全局变量"

class Test:
    pass


if __name__ == "__main__":  # 使别人调用此模块时不自动执行，用于测试
    print(__name__)
    test()

# __name__ 自身调用此变量时其结果为__main__;
print(__name__)  # 而当别人调用时其结果为调用的模块名