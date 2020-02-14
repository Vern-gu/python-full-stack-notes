# 分组一个list里的元素使[1,2,3...,100]变成[[1,2,3],[4,5,6]...]
li = [li for li in range(1,101)]
l = []
i = 0
while i < len(li):
    l.append(li[i:i+3])
    i += 3
print(l)


b = [li[i:i+3] for i in range(0,len(li),3)] # 标准答案
print(b)

