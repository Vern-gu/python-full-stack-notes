# 列表嵌套
a = [11, 22]
b = [22, 33]
a.append(b)
print(a)
# 小练习：八个老师随机分配进3间办公室
import random

office = [[], [], []]  # 定义三间办公室
teacher = ["a", "b", "c", "d", "e", "f", "g", "h"]  # 定义八名老师
for name in teacher:
    i = random.randint(0, 2)
    office[i].append(name)  # 引入随机数，老师按顺序被添加进随机的教室
# print(office)  # 其实到这步已经完成了，下面的遍历可以让显示更清楚
j = 1  # 为教室编号
for room in office:  # 遍历再遍历
    # print(room)
    print("办公室%d里的老师为：" % j, end="")
    for name in room:
        print(name, end=" ")
    print("")
    j += 1

# 元组和列表几乎一样，但是元组的元素无法被改变，元组使用小括号，列表使用方括号
# 不允许修改的数据可以存储在元组中
code = ("aa", "cbs", 12, 3.14, "好好")
code2 = ("aa",)  # 要建立一个只有一个元素的元组时要在其后加一个逗号，不然其类型将不会是元组
print(type(code2))

# 字典 {索引:值,索引2:值2, }  索引不允许相同，而值可以相同
info = {"name": "小明", "sex": "男"}
print(info.get("name"))  # 可以通过get（索引）来找字典中的值，如果索引不存在则会返回none
print(info.get("age", 14))  # 如果字典中没有age，就返回默认值14，如果有这个值就会返回字典中相应的值
# 1 修改字典中的元素
info["name"] = "小李"
print(info)
# 2 自字典中增加元素
info["money"] = 1000  # 直接给不存在的索引添加值即可
print(info)
# 3 删除字典中的元素 del  clear()
del info["money"]  # 这里如果直接del info 则会将整个字典删除
print(info)
info.clear()  # 清空字典中的内容，但不会将字典删除
print(info)
# 4 字典的其他操作
info = {"name": "小明", "sex": "男"}
print(len(info))  # 获取字典中键的个数
print(info.keys())  # 输出字典中全部的键
print(info.values())  # 输出字典中全部值
print(info.items())  # 输出键值对 （以上这些输出都是列表）
# print(info.has_key("sex")) # 判断字典中是否有这个索引（键值），有True，无False
# 字典的遍历：for循环
for temp in info.items():  # 如果这里只写info，最后只会有索引的遍历
    print(temp)

for key, value in info.items():
    print(key + " " + value)

# 小练习：实现带下标的索引的遍历
chars = ["a","b","c","d","e"]
i = 0
for char in chars:
    print(i,end =" ")
    print(char)
    i += 1
print("="*20)
for i,char in enumerate(chars):  # 方法二，使用enumerate枚举
    print(i,char)

chars.pop()   #  删除列表最后一个元素
print(chars)


# 将一个字典中中的元素，添加进另一个字典中
age = {"age":14}
info.update(age)
print(info)
