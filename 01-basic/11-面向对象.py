class Dog:
    def bark(self):
        print("旺旺叫")

    def __init__(self, newColor):
        print("this is a dog")
        self.color = newColor

    def __str__(self):
        return "这是一只%s狗" % self.color  # 使用str后，直接打印对象会获得return定义的内容


def test(aaa):
    aaa.bark()


wangcai = Dog("黑")
print(wangcai.color)
# wangcai.bark()
test(wangcai)  # 可以用函数调用类里的方法或属性

print(wangcai)  # 直接打印对象会得到存储的内存地址，他和id函数类似
print(id(wangcai))
print("="*40)  # 分割线==========================================


# 面向对象编程小练习：烤地瓜
class Digua:
    def __init__(self):  # 初始化工作
        self.cookedlevel = 0
        self.cookedstring = "生的"
        self.spicies = []
    def __str__(self):  # 返回终值
        if len(self.spicies) == 0:
            return "这个地瓜%s，生熟等级为%d"\
                   %(self.cookedstring,self.cookedlevel)
        else:
            return "这个地瓜%s，生熟等级为%d，添加了%s"\
               %(self.cookedstring,self.cookedlevel,str(self.spicies)[1:-1])
    def addSpicies(self,spicies):  # 定义添加佐料这个方法
        self.spicies.append(spicies)
    def cook(self,t):  # 定义烤地瓜这个方法
        self.cookedlevel += t
        if 3 < self.cookedlevel <= 5:
            self.cookedstring = "半生不熟"
        elif 5 < self.cookedlevel <= 8:
            self.cookedstring = "熟了"
        elif self.cookedlevel > 8:
            self.cookedstring = "焦了"
        elif self.cookedlevel <= 3:
            self.cookedstring = "是生的"


food = Digua()
print(food)
def cooking():  # 这个函数是用户烤地瓜的时间
    while True:
        time = int(input("你烤了几分钟？"))
        food.cook(time)
        spicies = input("你要加什么料？")
        food.addSpicies(spicies)
        print(food)
        if food.cookedstring == "焦了":
            break
cooking()

