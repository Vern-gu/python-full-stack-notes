import numpy as np
import collections as c

"""
data = np.array([  # 数组
    [154,1],
    [126,2],
    [70,2],
    [196,2],
    [161,2],
    [371,4]
])

feature = data[:, 0]  # 特征变量
label = data[:, -1]  # 结果标签。 -1表示取最后一列，方便以后数据拓展
predictPoint = 200  # 预测点
distance = list(map(lambda x:abs(x-predictPoint),feature))  # 计算每个点与预测点的距离
sortIndex = np.argsort(distance)  # 对distance集合从小到大排序元素，返回的是排序后下标的位置
sortedLabel = label[sortIndex]  # 用排序后的sortindex来操作label集合，根据distance来排序获得label
k = 3  # knn算法中的k，表示取最近的3个邻居
value = c.Counter(sortedLabel[:k]).most_common(1)[0][0]  # Counter计数器方法接收一个序列；mostcommon计算出现次数最多的前n个元素
print(value)
"""


def knn(feature, label, k, predict_point):  # 提取knn函数预测小球落点
    """feature = [123,120,231,97,112 ...]"""
    distance = list(map(lambda x: abs(x - predict_point), feature))
    sort_index = np.argsort(distance)
    sort_label = label[sort_index]
    value = c.Counter(sort_label[:k]).most_common(1)[0][0]
    return value


def knn2(k,predict_point,predict_color,label,feature):  # 数据集增加一个维度
    """
        feature = [[123,0.50],[230,0.52],[157,0.53]....]
        输入的 feature = traindata[:,0:2]
    """
    distance = list(map(lambda x: (((x[0]-predict_point)**2)+(x[1]-predict_color)**2)**0.5, feature))  # 计算欧式距离
    sort_index = np.argsort(distance)
    sort_label = label[sort_index]
    value = c.Counter(sort_label[:k]).most_common(1)[0][0]
    return value


def knn3(k, label, feature, predict):  # 使用矩阵和向量来实现knn回归算法预测房价
    """
    data = [
        [经度,纬度,房价],
        [经度,纬度,房价],
        ...
    ]
    """
    # 矩阵运算：先特征减去预测点后平方和，再开根号
    sort_index = np.argsort(np.sqrt(np.sum(np.square(feature-predict), axis=1)))
    sort_label = label[sort_index]
    predict_price = np.sum(sort_label[:k])/3
    return predict_price


if __name__ == '__main__':
    data = np.array([
        [154,1],
        [126,2],
        [70,2],
        [196,2],
        [161,2],
        [371,4]
    ])
    feature = data[:,0]
    label = data[:,1]
    predict_point = 200
    k = 3
    print(knn(feature, label, k, predict_point))