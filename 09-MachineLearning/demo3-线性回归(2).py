import numpy as np


data = np.array([
    [80, 200],
    [95, 230],
    [104, 245],
    [112, 274],
    [125, 259],
    [135, 262],
])
xarray = np.expand_dims(data[:, 0], axis=1)  # 等价于data[:, 0:1]
feature = np.append(xarray, np.ones(shape=(len(data), 1)), axis=1)  # 数据集矩阵增加一列1
label = data[:, -1:]  # 等价于np.expand_dims(data[:, -1], axis=1)
m = 1
b = 1
weight = np.array([
    [m],
    [b]
])
# print(feature,"\n",label)
learningrate = 0.00001


def gradient_decent():
    """
    slop = (Feature-T * (Feature * Weight - Label))/n
    """
    d = np.dot(feature, weight)-label  # 差值
    slop = np.dot(feature.T, d)*2/len(feature)
    print(slop)
    return slop  # 结果矩阵，第0行0个位置是mslop，第1行第0个位置是bslop


def train():
    """
    weight = weight - slop * learningrate
    通过梯度下降，不断获取更优秀的权重
    """
    global weight
    for i in range(2):
        slop = gradient_decent()
        weight = weight - slop * learningrate
        if abs(slop[0, 0]) < 0.1 and abs(slop[1, 0]) < 0.1:  # mslop=slop[0][0]  bslop=slop[1][0]
            break
    print("weight={}".format(weight))  # 第一个元素就是m，第二个元素就是b


if __name__ == '__main__':
    train()
