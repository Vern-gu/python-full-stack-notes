# transformer（转换器）为sklearn中所有特征工程的父类
# fit_transform()可以拆分为fit()以及transform()，fit方法为计算当前特征的基本数据（如平均值、标准差等），transform方法为最终的转换

"""
import sklearn

sklearn.datasets.load_*  # 获取小规模数据集（*为具体数据集的名字
sklearn.datasets.fetch_*(datahome=None,subset='train')  # 获取大规模数据集,datahome为下载的路径（默认为家目录下）
    # subset为选择要加载的数据集，train训练集，test测试集，all所有

sklearn.model_selection.train_test_split(feature,label,test_size,random_state)  # 划分数据集

transform = sklearn.feature_extraction.DictVectorizer(sparse=True)  # 字典特征提取
transform.fit_transform(字典)
transform.get_feature_names()  # 获取特征名字

transform = sklearn.feature_extraction.text.CountVectorizer(stop_words=[])  # 文本特征抽取,stop_words表示不统计的单词列表（停用词）
transform.fit_transform(文本)

transform = sklearn.feature_extraction.text.TfidfVectorizer(stop_words=[])  # 词频-逆向文档频率 （衡量一个词的重要程度
transferm.fit_transform(文本)

sklearn.preprocessing.MinMaxScaler(feature_range=(0,1))  # 数据预处理，归一化（feature_range默认为0到1），缺点为易受到异常值的影响
sklearn.preprocessing.StandardScaler().fit_transform(x)  # 数据标准化，处理后所有数据都聚集在均值为0附近，标准差为1

transfer = sklearn.feature_selection.VarianceThreshold(threshold=0)  # 特征选择，删除所有低方差特征（默认删除方差小于等于0的特征）
transfer.fit_transform(x)

transfer = sklearn.decomposition.PCA(n_composition=None)  # 将数据分解为较低维数空间（但尽可能保留多的信息）
        n_composition 为小数时，表示保留百分之多少的信息；整数表示减少到多少特征
transfer.fit_transform(x)
"""

# load和fetch返回的数据类型为datasets.base.Bunch（字典格式）
#   data：特征数据数组（二维的ndarray数组）
#   target：标签数组（一维ndarray数组）
#   DESCR：数组描述
#   feature_name：特征名
#   target_name：标签名

# train_test_split将数据集划分
#   feature：数据集特征值
#   label：数据集标签值
#   test_size：测试集大小（一般为浮点数）
#   random_state：随机数种子（不同种子会导致不同采样结果）
#   返回训练特征，测试特征，训练目标，测试目标

# feature_extraction  特征值化
#   DictVectorizer.fit_transform(x) 将字典转换为一个特征矩阵 x：字典或包含字典的迭代器，默认返回sparse稀疏矩阵
#   CountVectorizer.fit_transform(x) 统计每个样本特征词出现的个数 x：文本或包含文本字符串的可迭代对象，默认返回sparse矩阵
#   TfidfVectorizer.fit_transform(x) 用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度 x：文本或包含文本字符串的可迭代对象，默认返回sparse矩阵

# MinMaxScaler(feature_range=(0,1))  数据预处理
#   MinMaxScaler.fit_transform(x) x：numpy array的数据格式，返回相同形状的numpy array



