# feature 特征变量 ->输入
# label 结果标签 ->输出

"""
分类(classification)：最终预测的结果可能是有限的，比如辨别男女，预测是否通过考试等（求topK中出现最多的类别）
回归(regression)：预测到的结果是一个连续变化的过程，比如预测房价，预测体重等（求topK的value的平均值）

机器学习的三个基本步骤
1.收集问题相关的数据（feature，label）
2.选择一种数学模型建立feature和label的关系
3.根据选择的模型进行预测

数据可以分为训练集和测试集，测试集用来验证机器学习的可靠和准确性
通常测试集占整个数据集的2/10，在拆分数据集时，需要先将数据集充分大乱

预测得到的数据不是特别准确时的解决方案：
1.预测模型参数不好（调参）
2.影响因子不够多（增加数据维度）
3.样本数据量不够（增加测试数据）
4.预测选取模型不够好（选择其他机器学习算法）
5.错误率评估：(label值-预测值)/label值 该值越小越好（一般15%以下就算较为准确），将所有错误率相加再除以条目数就是总错误率

在多个维度的数据中，不同的数据可能存在的差异特别大，这时就需要对数据进行预处理：
1.归一化(Normalization)：使集合中的数据保持在0-1之间，公式：Xnorm = (X-Xmin)/(Xmax-Xmin)
2.数据标准化(Standardization)：数据的最大最小没有明确的范围且数据的分布不均匀，差异很大时使用标准化 (value-平均值)/标准差

特征降维：降低特征的个数
1.特征选择：去除冗余特征或相关变量（非独立），旨在从原特征中找出主要特征
    过滤式：方差选择法（低方差特征过滤）
    嵌入式：决策树（信息熵、信息增益）、正则化（L1，L2）、深度学习（卷积等）
2.主成分分析


误差评估方法：损失函数(loss function)
  最小均方差(mse)/最小二乘法：((猜测值-真实值)^2+(猜测值-真实值)^2+ ...)/n  该值应当尽量接近0   （用于线性回归）
  最大似然估计/对数似然损失：∑-y·log(h(x)) - (1-y)·log(1-h(x))  （用于逻辑回归）
  交叉熵：-(1/n)∑ Actual·log(Guess) + (1-Actual)·log(1-Guess)    （ln(a*b)=lna + lnb）  （用于softmax回归）

优化方法：
  梯度下降（主要）：通过依次迭代计算，缓慢取得最优解
  正规方程（仅用于线性回归，且样本量较少时）：直接使用公式求出权重和偏置。w=（X^T·X）^-1·X^T·y

欠拟合与过拟合：
  模型欠拟合时：可以增加数据的特征数量
  模型过拟合时：需要正则化（L1、L2）
    L1正则：使某些特征的权重直接为0，删除这个特征的影响
    L2正则：尽量减小高次项特征的影响（使高次项特征的权重趋近于0） 损失函数+λ惩罚项

分类准确率的评估方法：
    精确率：预测结果为正例样本中真实结果为正例的比例
    召回率：真实为正例的样本中预测结果为正例的比例（查得全不全）
    F1-score：反映模型的稳健性 F1=(2·Precision·Recall)/(Precision+Recall)
        # 以上三个指标无法应对样本不均衡时的情况，无法正确反映模型的准确率

    ROC曲线与AUC指标（只能用于评价二分类，且当样本不均衡时更适合）：AUC越接近于1，模型越趋于完美；越接近0.5越糟糕

    轮廓系数（评估KMeans性能）：模型最优情况为：内部距离最小化，外部距离最大化
        SCi=(Bi-Ai)/MAX(Bi,Ai)  (Bi为外部最小距离，Ai为内部平均距离)
        取值范围（1，-1），越接近1聚类效果越好
"""
# 1 KNN(k-nearest neighbor)模型：
#   实际上是统计学的聚类算法，其特点是参数的变化一定会明显地导致结果变化
#   在预测点附近收集大量的数据，根据其规律可得预测点预测结果（通过预测点附近label来预测）
#   必须要有全套的数据集，每次预测都要重新计算整套数据集
#   适用于分类（偶尔回归）
#   k值一般取数据集数量的开平方

# 2 线性回归：
#   线性回归就是求线性函数的参数值的过程
#   与knn不同，线性回归是一种规律的总结，数据集训练完毕后可以丢弃
#   仅适用于回归问题，预测的数字是连续的

# 2.5 岭回归：
#   即带有L2正则化的线性回归
#   减少过拟合的情况

# 3 逻辑回归：
#   预测的是分类问题
#   多为二分类的问题
#   线性回归的输出就是逻辑回归的输入（线性模型）
#   线性模型输入到激活函数sigmoid中

# 4 朴素贝叶斯：
#   列出所有分类的概率，概率最大的分类即为预测目标（常用于文本分类）
#   朴素指的是：假设特征与特征之间是相互独立的
#   优点：对缺失数据不敏感，算法简单速度快
#   缺点：由于使用了样本属性独立性的假设，所以如果特征属性有关联时其效果不好

# 5 决策树：
#   进行最高效的决策顺序（特征排序），根据信息增益排序
#   优点：可视化，可解释能力强
#   缺点：无法推广过于复杂的树，过拟合

# 6 随机森林：
#   森林：包含多个决策树的分类器，其输出的类别是由个别树输出的类别的众数而决定的
#   随机：即随机特征（）、随机训练集（随机有放回抽样）

# 7 K-Means（K均值聚类）：
#   为无监督学习，即没有目标值的机器学习
#   该方法主要是将目标样本区分为若干个未知的类别
#   首先随机设置K个初始中心点，计算其余点到这些中心点的距离
#   根据距离将这些点划分为K个类别，然后根据新划分好的类别重新计算出新的中心点（平均值）
#   如果新中心点和原先的一致，计算就结束，否则再重新计算其余点到中心点的距离不断重复

#   神经网络
#   神经网络主要的工作就是分类和聚类
#   “画一条线将两种不同的点分割在两边不同的空间里”
#   将点代入线条方程，大于0的则表示点在线条上方
