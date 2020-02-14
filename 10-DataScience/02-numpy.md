## Numpy优势：

Numpy（Numerical python）一个数值计算的python库，用于快速处理任意维度的数组<br>
其底层由c语言编写，因此运行速度很快

## ndarray属性：

* `ndarray.shape` or `np.shape(ndarray)` 查看数组的形状
* `ndarray.ndim` or `np.ndim(ndarray)` 查看数组的维度
* `ndarray.size` or `np.size(ndarray)` 查看数组中的元素数量
* `ndarray.dtype` or `np.dtype(ndarray)` 查看数组中元素的类型
* `ndarray.itemsize` or `np.itemsize(ndarray)` 查看数组中单个元素所占的字节

## ndarray方法：

#### 生成数组的方法：

* 生成全0或全1的数组：<br>
`np.zeros(shape=())`<br>
`np.ones(shape=())`
* 从现有数组中生成：<br>
`np.array()` 深拷贝<br> 
`np.copy()` 深拷贝<br>
`np.asarray()` 浅拷贝
* 生成固定范围的数组：<br>
`np.linspace(0,1,100)` [0,1]中等距离的生成100个数<br>
`np.arange()` 与range()是类似的用法
* 生成随机数：np.random模块<br>
  * 均匀分布：落在每一组的可能性都一样<br>
  `np.random.uniform(low,high,size)`从一个均匀分布中随机采样（左闭右开）<br>
  * 正态分布：由平均值和标准差控制的连续型随机变量分布，平均值为图形的对称轴，方差越大图形越扁即数据更加分散<br>
  `np.random.normal(loc,scale,size)`从一个正太分布中随机采样

#### ndarray形状修改：

* `ndarray.reshape(shape)` 将数组中的元素重新排列，改变矩阵的形状
* `ndarray.resize(shape)` 效果同reshape，但是不会返回新的ndarray，直接更改原有数组
* `ndarray.T` 矩阵转置，即行列互换，返回一个新数组

#### ndarray类型修改：

* `ndarray.astype(dtype)` 改变数组中元素的类型
* `ndarray.tostring()` 将数组序列化到本地，转换为bytes类型

#### 数组去重：

* `np.unique(ndarray)`

## ndarray运算：

#### 逻辑运算

* 逻辑判断：数组直接与数字比较（ndarray>0）,返回一个布尔值填充的矩阵
* 布尔索引：与逻辑判断配合使用（ndarray[ndarray>0]），返回数组中满足条件的元素
* 通用判断函数：
  * `np.all(bool)` ：只要数组中有一个元素为false就返回false；元素全为true才返回true
  * `np.any(bool)`：只要数组中有一个true就返回true；元素全为false才返回false
* 三元运算符：`np.where(bool,设置判断为true的值,设置判断为false的值)`<br>
复合逻辑需要搭配`np.logical_and` 和 `np.logical_or`使用，例如：<br>
`np.where(np.logical_and(ndarray>0.5, ndarray<2), 1, 0)`

#### 统计运算

* 统计指标函数：
  * min最小值, max最大值, mean均值, median中值, var方差, std标准差
  * 可使用`np.min(ndarray, axis=)` 或者 `ndarray.min(axis=)`<br>
  axis=0，按照**列**来统计；axis=1，按照**行**来统计数据
* 返回最大、最小值所在的位置：
  * `np.argmax(ndarray, axis)`
  * `np.argmin(ndarray, axis)`

#### 数组间运算

* 数组与数运算
* 数组与数组运算：不同形状的数组间运算会用到广播机制
* 矩阵运算：矩阵必须是二维的，且只有同形矩阵才可以加减
  * 矩阵乘法：第一个矩阵的列数等于另一个矩阵的行数时，这两个矩阵才可以相乘（行*列）（矩阵乘法不满足交换律）<br>
  api: `np.dot(matrix1,matrix2)` 或 `matrxi1 @ matrix2`

#### 数组的合并、分割

* 合并：
  * `np.hstack((a,b))` 水平拼接
  * `np.vstack((a,b))` 竖直拼接
  * `np.concatenate((a,b),axis=)` axis=1水平方向拼接
* 分割：
  * `np.split(ndarray, n)` 将数组分为n份；n为列表时，则按照索引进行分割
  
#### IO操作和数据处理

* 读取文件：`data=np.genfromtxt('filename',delimiter=',')`<br>
无法读取字符串，字符串与缺失值都会显示为"nan"
* 处理缺失值：
  * 删除缺失值样本
  * 替换（插补）缺失值
