import time

def countdown(i):  # 倒计时
    print(i)
    time.sleep(1)
    if 0 >= i:  # 递归的基线条件，到达基线条件则停止递归
        return
    else:  # 递归条件
        countdown(i-1)

countdown(3)

# ===================================


def jiecheng(j):  # 栈递归，阶乘
    if 1 == j:
        return 1
    else:
        return j*jiecheng(j-1)


print(jiecheng(3))
