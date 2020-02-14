# 面向过程：根据业务逻辑 从上到下写代码，即要考虑到方方面面的事
# 面向对象： 将数据与函数绑定在一起，进行封装，即只考虑要达成的目的
# 面向对象可以更快速的开发程序，减少了重复代码的重写过程
# 类 和 对象
# 打个比方 类就是图纸模型  对象就是通过图纸模型而得到的实体实物
# 类由名称/属性/方法构成
# 名称：类名（建议首字母大写）  属性：数据  方法：操作的方法，行为（函数）

# 定义一个类： class 类名：   注意定义类不要加括号
class Cat:  # 定义了一个猫 类
    def eat(self):  # 定义了类的方法  注意方法一定要加(self)
        print("---吃---")

    def mew(self):  # 定义了第二个方法
        print("---喵---")

    def w(self):  # 这里方法名和属性名不能相同
        print(self.weight)

    def __init__(self,newSex,newAge):  # 当创建完一个对象后，会立刻自动调用这个方法
        self.sex = newSex
        self.age = newAge  # 可以在这个方法中添加属性
        print("这是一只猫")


xiaomao = Cat("female","3 month")  # 创建了“小猫”这个对象,同时定义了部分属性
xiaomao.eat()  # 调用方法
xiaomao.mew()

print(xiaomao.sex)
print(xiaomao.age)
xiaomao.color = "黑色"  # 给小猫这个对象添加color属性
xiaomao.weight = "3 kg"  # 添加weight属性

a = xiaomao.color  # 获取小猫对象的属性
print(a)
xiaomao.w()  # 先定义一个方法，再调用这个方法以获取属性
# 调用方法要加() ，调用属性不用加

