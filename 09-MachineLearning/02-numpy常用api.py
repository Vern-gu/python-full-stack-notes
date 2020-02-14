import numpy as np

# np.array()    创建一个二维数组[[],[],...]，矩阵
# np.sort()     将集合直接按从小到大排序
# np.argsort()  将集合元素按照下标，或者位置去排序，得到sortindex
# np.loadtxt()  用此方法直接读取文件中的数据，第一个参数为文件名，第二个参数为delimiter="分隔符"，返回一个二维数组
#   converters参数可以将数据第n列通过函数转换为另一个数据，converters={0,function}
#   skiprows参数表示跳过某一行，skpirows=1 表示跳过第一行的数据
#   usecols参数表示使用某几列的数据，usecols=(6,17,18) 表示使用第6第17第18列数据（从0开始）
#   unpack参数默认为false，改为True后可以将二维数组展开得到多个一维数组
# np.savetxt()  将数据保存到文件，第二个参数接收数组（数据），delimiter="分隔符"，fmt(数据类型)="%d" 以整型的方式保存
# np.random.shuffle()   数据打乱1000次
# np.square()   矩阵自平方
# np.sqrt()     矩阵自开方
# np.sum()      默认会将一个矩阵中的值都加起来变成一个数，可以指定参数axis=1使其按行相加（将同一行的数值相加）
# np.max()      获取数据中最大的值
# np.min()      获取数据中最小的值
# np.mean()     计算平均值
# np.std()      计算标准差
# np.power(x,y) 计算x的y次方
# np.shape(ARRAY)/ARRAY.shape    获取矩阵的形状
# np.dot(A,B)   A、B两个矩阵的点乘
# np.expand_dims()  扩展矩阵的维度，接收一个axis参数，axis=1使其增加列数，axis=0使其增加行数
# np.ones(shape=(n,m)) 创造一个所有元素为1的矩阵，矩阵形状由shapes参数决定
# np.append(A,B,axis=1)    将两个矩阵按水平方向拼接，若不接收axis参数则默认降维增加
# 矩阵.T      矩阵的转置
# np.exp(n)    自然底数e做若干次运算后所得到的值，即e的n次幂
# np.linspace(a,b,n)    将a~b中的数分为n份
# np.apply_along_axis(func, axis, array)    数组的轴向汇总，沿着数组中所指定的轴向，调用处理函数，并将每次调用的返回值重新组织成数组返回
#   axis的值为0或者1，0代表沿着列方向（竖直方向）对数据进行处理

# numpy显示设置：
#   np.set_printoptions(threshold = np.inf)  使所有数据都能显示，而不是用省略号表示，np.inf表示一个足够大的数
#   np.set_printoptions(suppress = True)  使结果不以科学计数显示
