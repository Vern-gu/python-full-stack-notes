## 什么是pandas

pandas（panel+data+analysis）一种数据处理工具，集成了numpy以及matplotlib。
* 它拥有比numpy更便捷的数据处理能力
* 读取文件更方便快捷

## pandas核心数据结构

pandas拥有三类核心数据结构，分别为：
* Panel：`pd.Panel(data,items,major_axis,minor_axis)`存储三维数组的结构，相当于是dataframe的容器，从不同的维度切入可以获得不同的二维数组。
  * items：axis0，每个项目对应于内部包含的数据帧(dataframe)
  * major_axis：axis1，每个数据帧(dataframe)的行索引
  * minor_axis：axis2，每个数据帧(dataframe)的列索引
* Dataframe：`pd.DataFrame(data, index=[], columns=[])`既有行索引又有列索引的二维数组
index为行索引，columns为列索引
  * 属性：shape、index(行索引)、columns(列索引)、values(不带索引)、T(转置)
  * 方法：head(n)默认返回前5行数据、tail(n)默认返回末5行数据
  * 索引设置：
    * 修改行列索引值：必须重新设置索引值`array.index=new_array`（不能单独修改某行索引名）
    * 重设索引：`array.reset_index(drop=False)`初始化下标索引，默认不删除原来索引（较少用到）
    * 设置新索引：`array.set_index(keys,drop=True)`以某列值设为新索引，keys为列索引名称或列索引名称列表，默认删除原来列。
    当设置多个索引名称后，index属性会返回一个multiindex对象
* Series：`pd.Series(data，index=[])`(也可以通过传入字典创建带索引的数组)带索引的一维数组，也可以理解为datafarme是series的容器
  * 属性：index、values

其中我们平时使用最多的是dataframe结构，从0.20.0版本开始Panel数据类型已被弃用，可以使用dataframe的multiIndex代替

## pandas基本数据操作

#### 索引操作

* 直接使用行列索引（先列后行）：`data['column_name']['index_name']`
* 按名字索引：`data.loc['index_name','column_name']`与上面的直接索引类似，用了loc属性后可以先行后列
* 按数字索引：`data.iloc[1,0]`使用了iloc属性后可以和numpy索引类似，用数字取第二行第一列的元素

#### 赋值操作

直接使用`data.column_name = value` or `data[column_name] = value`将二维数组中一整列的数据都替换(此方法不能用在行操作上)。<br>
也可以配合上述的索引操作直接赋值。

#### 排序操作

* 对内容进行排序：`data.sort_values(by=, ascending=)`<br>
by 按单个键或多个键进行排序<br>
ascending=False 降序排列（，默认为升序）
* 对索引进行排序：`data.sort_index(ascending=)`<br>
直接按照行索引进行排序，默认按照行索引升序进行排序

## pandas运算

#### 算术运算

可以直接使用算术运算符或者使用add、sub等算数函数进行计算

#### 逻辑运算

* 逻辑运算符：`<、>、|、&` ，同numpy一样也是可以进行布尔索引的，并能够直接实现复合逻辑判断eg:<br>
`data[(data['open']>2) & (data['change']>10)]`
* 逻辑运算函数：
  * query('expression')：使用query函数实现上述的复合逻辑判断会更简单`data.query("open > 2 & change > 15")`
  * isin([values])：判断某列元素中是否存在某些数值 eg：<br>
  `data['low'].isin([1.1, 2.4])`
  
#### 统计运算

与numpy类似，min最小值, max最大值, mean均值, median中值, var方差, std标准差<br>
`data.describe()` 该函数可以直接将每一列的元素所有的统计数值返回<br>
`data.idxmax()` `data.idxmin()` 返回最大/小值所在的索引，默认都是按列统计，也可以添加axis=参数改变统计方向
* 累计统计函数：
  * cumsum()：计算前n个数的和
  * cummax()：计算前n个数的最大值
  * cummin()：计算前n个数的最小值
  * cumprod()：计算前n个数的积
  
#### 自定义运算

`data.apply(func,axis=0)` func为自定义函数，默认axis=0按列来计算，eg：<br>
`data.apply(lambda x: x.max()-x.min(), axis=0)`

## 使用pandas画图

`DataFrame.plot(x=None, y=None, kind='line')`<br>
&emsp; kind为画图的种类：'line' 'bar' 'barh' 'hist' 'pie' 'scatter'

## pandas文件读取与存储

* csv：
  * 读取csv文件：`pd.read_csv(path, use_cols=[], names=[])`<br>
    path：文件路径，use_cols：选择导入的字段，names：如果文件里不包含表头，可以使用names自行添加
  * 存储csv文件：`data.to_csv(path, columns=[], mode='', index=True, header=True)`<br>
    columns：要保存的列，mode：‘w’重写‘a’追加，index：是否保留行索引，header：是否保留表头
* HDF5：该类型的文件读取和存储需要指定一个键，值为要存储的dataframe，可以存储三维数组
  * `pd.read_hdf(path, key)` key：指定要读取哪一个二维数组
  * `dataframe.to_hdf(path, key)` key：为该二维数组取名
* json：
  * `pd.read_json(path, orient='records', lines=True)`<br>
  orient：指定这个json以怎样的形式展示，lines：是否按行读取json对象
  * `dataframe.to_json(path, orient, lines)`