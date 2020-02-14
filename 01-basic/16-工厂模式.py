class Car:
    def move(self):
        print("车在移动")
    def stop(self):
        print("停车")

class Store:
    def order(self):
        self.car = Car()  # 在一个类的方法中可以直接调用另一个类的方法
        self.car.move()  # 当Car类的对象给定后，可以直接调用对象.方法
        self.car.stop()

fourS = Store()
# dazhong = Car()
fourS.order()

print("=========================")

class Cake(object):
    def __init__(self,taste = "还行"):
        self.taste = taste

class AppleCake(object):
    def __init__(self,taste = "很甜有浓浓的苹果味"):
        self.taste = taste

class OrangeCake(object):
    def __init__(self,taste = "有点酸，橙子味"):
        self.taste = taste

class ChooseCake(object):
    def __init__(self,category):
        self.category = category
    def cakeChoice(self):
        if self.category == "蛋糕":
            cake = Cake()
        elif self.category == "苹果派":
            cake = AppleCake()
        elif self.category == "橙子派":
            cake = OrangeCake()
        return cake.taste

class CakeStore(object):
    def taste(self,category):
        self.cake = ChooseCake(category)
        cake = self.cake.cakeChoice()
        print("---味道:%s---"%cake)

dangaodian = CakeStore()
category = input("想要尝什么派？")
dangaodian.taste(category)

# cake = Cake()
# print(cake.taste)

# 工厂方法：在父类中定义了一个方法，但下面是pass
# 这时需要使用者定义一个子类，重写这个方法
