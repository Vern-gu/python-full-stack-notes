## matplotlib是一个画二维图表的python库

简单示例：
```python
import matplotlib.pyplot as plt
plt.figure()
plt.plot([1,0,9],[4,5,6])
plt.show()
```

## matplotlib三层结构：

* 容器层
  * 画板层：底层已创建
  * 画布层：plt.figure(title='') 创建画布
  * 绘图区（坐标系axis）
* 辅助显示层：坐标刻度，图例等
* 图像层：各种图表

## 折线图绘制与保存：

1.创建画布 `plt.figure(figsize=(),dpi=)`<br>
&emsp; figsize：接受元组，指定图像长宽<br>
&emsp; dpi：图像的清晰度<br>
2.绘制图像 `plt.plot(xarray, yarray, label='')`<br>
3.保存图片 `plt.savefig('test.png')`<br>
4.显示图像 `plt.show()` 调用show方法后会释放figure资源，因此该方法总是最后调用

## 修改x，y轴的刻度，添加网格：

* `plt.xticks(val_list,text_list)`<br>
`plt.yticks(val_list,text_list)`<br>
&emsp;修改x，y轴刻度数值<br>
&emsp; val_list：刻度值的数组<br>
&emsp; text_list：每个刻度的文本数组<br>
* `plt.xlim(min,max)`<br>
`plt.ylim(min,max)`<br>
&emsp; 设置坐标轴的可视区域[min, max]
* `plt.xlabel('')`<br>
`plt.ylabel('')`<br>
&emsp; 设置坐标轴的描述信息
* `plt.grid(True,linestyle=':',alpha=0.5)`<br>
&emsp; 添加网格
* `plt.title('')`<br>
&emsp; 设置图表标题
* `plt.legend()`<br>
&emsp; 显示图例 

## 绘制子图：

* `plt.subplot(rows, cols, n)`&nbsp;*此方法目前很少用*<br>
&emsp; rows：矩阵行数<br>
&emsp; cols：矩阵列数<br>
&emsp; n：子图编号

* `figure, axes = plt.subplots(rows, cols, **fig_kw)`&nbsp;创建一个带有多个坐标系的图<br>
&emsp; fig_kw：为figure()方法中的一些参数<br>
&emsp; 会返回一个图像和绘图区<br>
&emsp; 最后使用axes的切片（如`axes[0].plot()`）来绘制图形

## 绘制各种常见图形：

* 绘制折线图：*体现事物随某种特征增长而产生的变化*<br>
`plt.plot(x,y)`
* 绘制散点图：*用于判断变量之间是否存在数量关联趋势，栈是分布规律*<br>
`plt.scatter(x,y)`
* 绘制柱状图：*统计各个数据的大小，体现他们的差别*<br>
`plt.bar(x,y,width,align='center',color=['r','b',...])`<br>
&emsp; width：柱子宽度<br>
&emsp; align：柱子位置的对齐方式（'center','edge'）
* 绘制直方图：*绘制连续性的数据展示一组或多组数据的分布状况*<br>
`plt.hist(x,bins,density=None)`<br>
&emsp; x：数据<br>
&emsp; bins：组数 *组数=极差//组距* <br>
&emsp; density：布尔值是否显示频率（默认不显示）
* 绘制饼图：*表示分类数据的占比情况*<br>
`plt.pie(x,labels,autopct='%1.2f%%',colors)`<br>
&emsp; x：数量（自动算百分比）<br>
&emsp; labels：每部分名称<br>
&emsp; autopct：指定占比显示（1：占一个字符；.2：保留两位小数）<br>
`plt.axis('equal')` ：使饼图等比显示
