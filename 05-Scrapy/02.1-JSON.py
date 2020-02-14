# JSON：简单说就是js中的数组和对象，对象用{}，数组用[]
import json

# json模块有四个主要功能：dumps、dump、load、loads
# json.loads():把json格式字符串解码转换为python对象
strDict = '{"city":"北京","name":"大猫"}'
json.loads(strDict)
# json.dumps():实现python类型转换为json字符串，返回一个str对象
li = [1,2,3]
json.dumps(li)
# json.dump()  将python内置类型序列化为json对象后写入文件
# json.load()  读取文件中json形式的字符串元素转化为python类型
