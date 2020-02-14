# 基于线性回归，得出线性公式（权重）后代入到激活函数sigmoid中
# 设置边界，得出结论

import numpy as np

data = np.array([
    [5, 0],
    [15, 0],
    [25, 1],
    [35, 1],
    [45, 1],
    [55, 1]
])
m, b = 1, 1
weight = np.array([
    [m],
    [b]
])

feature = data[:, 0:1]  # 等价于np.expand_dims(data[:,0], axis=1)
feature2 = np.append(feature, np.ones(shape=(len(feature), 1)), axis=1)
labels = data[:, -1:]
learningrate = 0.0001


def gradient_decent():
    """Features.T * (sigmoid(Feature * Weight) - Labels)"""
    z = np.dot(feature2, weight)
    d = 1/(1+np.exp(-z)) - labels  # 1/(1+e^-z)
    slop = np.dot(feature2.T, d)
    return slop


def train():
    """Weight = Weight - slop * learningrate"""
    global weight
    for i in range(3000000):
        slop = gradient_decent()
        weight = weight - slop*learningrate
        if abs(slop[0,0]) < 0.1 and abs(slop[1,0]) < 0.1:
            break
    print(slop)
    return weight


if __name__ == '__main__':
    print(train())
