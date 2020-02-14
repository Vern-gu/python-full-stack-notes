## 缺失值处理

缺失值在numpy或pandas中一般是以NaN表示的。

* 判断数据中是否存在NaN：
  * `pd.isnull(data)` 在有缺失值的地方返回True
  * `pd.notnull(data)` 在不是缺失值的地方标记为True
* 删除含有缺失值的样本：<br>
`data.dropna(axis='rows',inplace=False)` 删除含有缺失值的行。<br>
默认需要接收返回值，当inplace为True时直接在原有数据上修改，没有返回值。
* 替换/插补：<br>
`data.fillna(value,inplace=False)` 将缺失值替换为设定的value值。

然而有些数据并不是缺失值，而是有默认标记，如"?"等符号时该如何处理呢？

* 将"?"替换为np.nan：`data.replace(to_replace="?", value=np.nan)`<br>
to_replace：要替换的值，value：替换后的值

## 数据离散化

one-hot编码（哑变量）<br>
<br>
pandas进行数据离散化的流程：
* 对数据进行分组
  * 自动分组：`sr=pd.qcut(data, bins)` data：要分组的数据；bins：组数
  * 自定义分组：`sr=pd.cut(data, [])` 将设定好的组区间以列表传入（每组数的边界）
  * 可以用`sr.value_counts()`统计每个分组包含的元素数量
* 对分好组的数据求哑变量
  * `pd.get_dummies(sr, prefix=)` sr：分组后得到的对象；prefix：title前缀

## 合并

* 按方向拼接：`pd.concat([data1,data2],axis=0)` 默认竖直方向拼接
* 按索引拼接：`pd.merge(left,right,how="inner",on=[索引])` 
  * left：左表；right：右表；how：拼接方式"outer" "left" "right"（默认内连接）；on：按照哪一个索引拼接

## 交叉表和透视表

交叉表与透视表常用于探索两个变量之间的关系<br>
用于计算一列数据对于另外一列数据的分组个数(寻找两个列之间的关系)

#### 交叉表：

* `pd.crosstab(column1, column2)`

#### 透视表：

* `data.pivot_table([要统计的列], index=[按某一个列分组])` 

## 分组与聚合

* `data.groupby(key="", as_index=False)["要聚合的列"].聚合函数()` key：要分组的列<br>
只有添加了聚合函数后才会返回分组后的结果，否则只会返回一个内存对象
