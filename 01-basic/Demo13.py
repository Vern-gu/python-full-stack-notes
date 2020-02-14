# 小练习：老王开枪
class Person:
    def __init__(self,name,blood):
        self.name = name
        self.blood = blood
        self.weapon = None
    def addBullet(self,zidan):
        danjia.addBullet(zidan)
    def addCharger(self,danjia):
        qiang.addCharger(danjia)
    def equipWeapon(self,qiang):
        self.weapon = qiang
    def shoot(self):
        qiang.shoot()   # 等于self.weapon.shoot()
    def __str__(self):
        msg = "%s当前的血量为%d"%(self.name,self.blood)
        return msg

class Gun:
    def __init__(self):
        self.charger = None
    def addCharger(self,danjia):
        if self.charger == None:
            self.charger = danjia
    def shoot(self):
        zidan = danjia.shoot()  # self.charger.shoot()
        if zidan:
            zidan.damage()
        else:
            print("没有子弹了...")
    def __str__(self):
        if self.charger:
            return "弹夹就位，目前子弹数%d/%d"\
                   %(len(danjia.chargerList),danjia.volume)
        else:
            return "弹夹未安装"

class Charger:
    def __init__(self,volume):
        self.volume = volume
        self.chargerList = []
    def addBullet(self,zidan):
        self.chargerList.append(zidan)
    def shoot(self):
        if len(self.chargerList) > 0:
            zidan = self.chargerList[-1]
            self.chargerList.pop()
            return zidan
        else:
            return None
    def __str__(self):
        msg = "装入弹夹%d发子弹"%(len(self.chargerList))
        return msg

class Bullet:
    def __init__(self,power):
        self.power = power
    def damage(self):
        boss.bleed(self.power)

class Enemy:
    def __init__(self,blood):
        self.blood = blood
    def bleed(self,damage):
        self.blood -= damage
    def __str__(self):
        return "敌人当前血量为：%d"%self.blood


boss = Enemy(50)
wang = Person("WANG",100)
print(wang)
danjia = Charger(20)
i = 0
while i < 5:
    zidan = Bullet(10)
    wang.addBullet(zidan)
    i += 1
print(danjia)
qiang = Gun()
wang.addCharger(danjia)
wang.equipWeapon(qiang)
print(wang.weapon)
print(boss)
wang.shoot()
print(boss)
print(wang.weapon)
