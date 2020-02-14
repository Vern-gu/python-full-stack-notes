import numpy as np


#   对最小均方差进行求导后 乘以 一个学习速率 就是所谓的梯度下降

data = np.array([
    [80, 200],
    [95, 230],
    [104, 245],
    [112, 274],
    [125, 259],
    [135, 262],
])
m = 1
b = 1
xarray = data[:, 0]  # 数据集中的房屋面积
yreal = data[:, -1]  # 实际房价
learningrate = 0.00001


def gradient_decent():  # 定义梯度下降方法：
    bslop = 0  # b求导后的斜率
    mslop = 0  # m求导后的斜率
    for index, x in enumerate(xarray):
        bslop += (m * x + b - yreal[index])  # 根据mse对b求偏导得出b的斜率
    bslop = bslop * 2 / len(xarray)
    print("mse对b求导={}".format(bslop))

    for index, x in enumerate(xarray):
        mslop += ((m * x + b - yreal[index]) * x)  # 根据mse对m求偏导得出m的斜率
    mslop = mslop * 2 / len(xarray)
    print("mse对m求导={}".format(mslop))
    return bslop, mslop


def train():  # 定义训练数据的方法，将循环梯度下降方法直至找出合适的m与b
    for i in range(1000000):
        bslop, mslop = gradient_decent()
        global b
        global m
        b = b - bslop * learningrate  # 根据学习速率和所得的斜率，不断梯度下降地代入新的参数b和m
        m = m - mslop * learningrate
        if abs(bslop) < 0.1 and abs(mslop) < 0.1:  # 直到得到满意的参数值（当斜率为0时，则是mse最接近0的时候）
            break
    print("m={},b={}".format(m, b))
    return b, m


if __name__ == '__main__':
    train()
