#  三元表达式：
# [on true] if [expression]else [on false]
# 如果 [expression] 为真, 则 [on true] 部分被执行。如果表示为假则 [on false] 部分被执行

b = 1
a = 0
a = b-a if b > a else b+a
print(a)

# ===========================================================================================================
# 将一个序列中的元素随机排列
import random

l = [1,2,3,4,5,6,7]
random.shuffle(l)
print(l)

# eval()函数：把一个字符串当表达式来执行，返回表达式执行后的结果
# exec()函数：把一个字符串当程序来执行
