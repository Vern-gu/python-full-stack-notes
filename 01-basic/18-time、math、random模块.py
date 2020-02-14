import time
# 时间元组由9个整型元素组成，从左到右依次为;
#   年（如1970）
#   月（1-12）
#   日（1-31）
#   时（0-23）
#   分（0-59）
#   秒（0-59）
#   星期（0-6，周一是0）
#   元旦开始日（1-366）
#   夏令时修正时间（-1，0，1）

# time.time() 返回从计算机元年至当前时间的秒数的浮点数
# time.asctime([tuple]) 将时间元组转换为日期时间字符串
# time.localtime([secs]) 将UTC秒数时间转换为日期元组（本地时间为准）
# time.mktime(tuple) 将本地日期时间元组转换为新纪元秒数时间（UTC为准）


import math
# math.ceil(x)  对x向上取整
# math.floor(x)  对x向下取整
# math.sqrt(x)  返回x的平方根
# math.factorial(x)  返回x的阶乘
# math.log(3, 2)  即log2底3
# math.pow(x, y)  即x的y次方（x**y）
# math.fabs(x)  浮点数x的绝对值
# math.degrees(x)  将弧度x转换为角度
# math.radians(x)  将角度x转换为弧度
# math.sin(x)  返回x的正弦（x为弧度）
# math.cos(x)  返回x的余弦（x为弧度）
# math.tan(x)  返回x的正切（x为弧度）


import random
# random.random()  返回一个[0,1)之间的随机实数
# random.uniform(a,b)  返回一个[a,b)之间的随机实数
# random.randrange([start,] stop [,step])  返回一个[start,stop)之间的随机整数（跳过step），若没有start则从0开始
# random.randint(a,b)  返回[a,b]之间的随机整数
# random.choice(sequence)  从序列中返回随机元素
# random.shuffle(sequence[,random])  随机打乱序列
# random.seed(a=1)  用给定的数a设置随机种子，不给参数a则用当前时间设置随机种子
