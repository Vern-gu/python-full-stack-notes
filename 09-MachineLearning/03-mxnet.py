form mxnet import nd  # nd即为NDArray，与numpy的多维数组非常类似 

# nd.arange(n)			创建一个长度为n的一维数组
# ARRAY.shape			获取矩阵的形状
# ARRAY.size			获得矩阵中元素的总数
# ARRAY.reshape(n,m)	将原矩阵转化为n行m列的矩阵
#	也可以优先只确定行或者列，另一个数由-1自动填充

# nd.zeros((i,n,m))		构造元素为0，形状为(i,n,m)的张量
# nd.ones((i,n,m))		构造元素为1，形状为(i,n,m)的张量
# nd.random.normal(0,1,shape=(3,4))		形状为（3，4）每个元素随机采样于均值0、标准差为1的正态分布的矩阵

# ARRAY1.exp(ARREY2)	按元素做指数运算，numpy中无法使用
# nd.dot()				点乘两个矩阵
# ARRAY.T				矩阵转置

# nd.concat(a,b,dim=0)	将a，b两个矩阵在行方向上连结，dim=1在列方向上连结
# ARRAY.asscalar()		可以将矩阵转换为python标量
# nd.ones_like(a)		创建与a矩阵形状相同，用元素1填充的矩阵，同理zeros_like()

# ARRAY.asnumpy()		将NDArray转换为numpy的矩阵
# nd.array(nparray)		将numpy的矩阵转换为ndarray
