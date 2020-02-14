
TensorFlow程序通常被组织成一个构建图阶段和执行图阶段。<br>
* 在构建阶段，数据与操作的执行步骤被描述成一个图。(定义数据和操作)
* 再执行阶段，使用会话 执行构建好的 图中的操作。(调用各方资源，将定义好的数据和操作运行起来)
* 张量（tensor）：TensorFlow中基本的数据对象
* 节点（operation）：图中所执行的操作

## 图相关操作：

#### 默认图：

当用户不自定义图时，所有的数据和操作都会欸存放在一张默认图中。<br>
<br>
查看默认图的方法：
* 调用`tf.get_default_graph()`访问
* op、sess都含有graph属性，默认都在一张图中

#### 创建图：

`new_graph = tf.Graph()`<br>
如果要在这张图中创建OP，典型用法是使用tf.Graph.as_default()上下文管理器：<br>
`with new_graph.as_default():`<br>
如果是要运行自己创建的图中操作时，需要在会话中指定图:<br>
`with tf.Session(graph=new_graph) as sess:`

## TensorBoard 可视化学习：

我们能看到自己写的程序的可视化效果，这个功能就是tensorboard。

1. 数据序列化-events文件<br>
    `tf.summary.FileWriter(path, graph)`<br>
    这行代码将会在指定路径下生成一个events文件，其名称格式如下：<br>
    `events.out.tfevents.{timestamp}.{hostname}`
2. 启动TensorBoard<br>
    在命令行中输入：`tensorboard --logdir=path` 打开可视化图
    
#### 收集变量：

* `tf.summary.scalar(name,tensor)` 收集对于损失函数和准确率等单值变量，name为变量名，tensor为值
* `tf.summary.histogram(name,tensor)` 收集高维度的变量参数
* `tf.summary.image(name,tensor)` 收集输入的图片张量能显示图片

#### 合并变量写入事件文件：

* merged=tf.summary.merge_all()
* 运行合并：summary=sess.run(merged) ，每次迭代都需运行
* 添加：FileWriter.add_summary(summary,i) ，i表示第几次的值

## OP

* 操作：operation对象，如constant等函数
* 数据：tenser对象，通过操作函数返回的数据对象，每个数据都有它的指令名称，不同图拥有各自的命名空间
* 指令名称：可以在操作函数中添加“name=”属性来修改指令名称（如果名称重复了，则会在名称后累加数字，保证不重复）

## 会话：

#### 会话创建：

* `tf.Session(graph=, taget=, config=)` 用于完整的程序当中<br>
    graph：要开启会话的图；<br>
    target：指定tf服务器地址，是的会话可以访问该服务器控制的计算机上的所有设备<br>
    config：允许指定一个tf.ConfigProto()便于控制会话的行为（生成日志，了解每一个操作运行在哪一个设备上）
* `tf.InteractiveSession()` 用于交互式上下文中的Tensorflow，例如shell<br>
    如果在交互会话中想要查看某操作后的值也可以使用`value.eval()`方法，而不用sess.run()
* 创建会话时其实需要消耗资源，因此当会话结束后需要用`sess.close()`回收，一种常用的方式就是使用上下文管理器
* 会话的run(fetches, feed_dict) 通过sess.run()方法来运行operation<br>
    fetches：单一的operation对象，或者列表和元组（其他不属于tensorflow的类型不行）<br>
    feed_dict：允许覆盖图中张量的值（该参数需要与tf.placeholder()搭配使用，为占用符定义初始值）<br>
    * `tf.placeholder(dtype, shape)`可以定义占位符
    
## 张量（Tensor）

TensorFlow的张量就是一个n维数组（n阶），其类型为tf.Tensor。tensor具有两个重要属性：<br>
* type：数据类型
* shape：形状（阶）

#### 创建张量

* `tf.zeros(shape,dtype=tf.float32,name)` 创建所有元素为0的张量
* `tf.ones(shape,dtype=float32,name)` 创建所有元素为1的张量
* `tf.constant(value,shape,dtype=float32,anme)` 创建一个常数张量
* `tf.random_normal(shape,mean=0,stddev=1,dtype=float32,seed,name)` 从正态分布中输出随机值

......

#### 张量的变换

* 类型改变
  * `tf.string_to_number(string_tensor,out_type,name)` 字符串转换为数字
  * `tf.to_float(x,name)` 转换为浮点数
  * `tf.cast(x,dtype,name)` 将张量转换为任意指定类型
* 形状改变<br>
静态形状 - 初始创建张量时的形状，没有完全固定下来时才能更改<br>
动态形状 - 强行改变已经固定的静态形状
  * 改变静态形状：`tf.set_shape(tensor,shape)` or `tensor.set_shape(shape)`
  * 改变动态形状：`tf.reshape(tensor,shape)` of `tensor.reshape(shape)`

#### 张量的数学运算

* 算数运算符：tf.add 等
* 基本数学函数：tf.pow 等
* 矩阵运算：tf.matmul 等
* reduce操作（降维）：tf.reduce_all/reduce_mean 等
* 序列索引操作

## 变量操作

变量为tensorflow中一个专门的组件，是表示程序处理的共享持久状态的最佳方法（用于存储模型参数）。其特点为：<br>
* 存储持久化
* 可修改值
* 可指定被训练

#### 创建变量

`tf.Variable(initial_value=None,trainable=True,collection=None,name=None)`<br>
* initial_value：初始化的值
* trainable：是否被训练，设置为False后该值将无法通过训练而改变

变量需要显示初始化才能运行， 
```python
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
```
另外可以使用tf.variable_scope()修改变量的命名空间，以使得结构更加清晰：
```
with tf.variable_scope('feature'):
    feature = tf.Variable(initial_value=4)
    feature_2 = tf.variable(initial_value=0)

with tf.variable_scope('label'):
    label = tf.Variable(initial_value=0)
```

## 其它api：

#### 基础api：

* tf.app
* tf.image
* tf.gfile
* tf.summary
* tf.python_io
* tf.train
* tf.nn

#### 高级api：

* tf.keras
* tf.layers
* tf.contrib
* tf.estimator

#### 其它api：

* tf.slice(tensor,[n],[l]) 将一维数组切片，[n]起始，[l]切片长度
* tf.transpose(tensor,[1, 2, 0]) 数组转置，将第一个维度转成最后一个维度

## 模型的保存与加载：

`saver = tf.train.Saver(var_list=None,max_to_keep=5)` 保存和加载模型（保存文件格式：checkpoint文件）<br>
var_list：指定将要保存和还原的变量<br>
max_to_keep：指定要保留的最近检查点文件的最大的数量。创建新文件时，会删除较旧的文件。

1. 先实例化saver
2. 保存`saver.save(sess,path)` 路径需要精确到文件名'.ckpt'
3. 加载`saver.restore(sess,path)`

## 命令行参数使用

1. `tf.app.flags` 支持应用从命令行接收参数，可以用来指定集群配置等。
    * `tf.apps.flags.DEFINE_integer(flag_name='max_step',default_value=0,docstring='训练模型的步数')`  
    * `tf.apps.flags.DEFINE_string(flag_name,default_value,docstring)`
    * `tf.apps.flags.DEFINE_float()`
    * `tf.apps.flags.DEFINE_boolean()`
2. `flags = tf.app.flags.FLAGS` 定义获取命令行参数
3. `flags.{flag_name}` 获取到命令行参数

## 数据IO操作：

QueueRunner：基于队列的输入管道从TensorFlow图形开头的文件中读取数据。（多线程+队列 实现）

#### 文件读取流程：

1. 构造文件名队列
  * `file_queue = tf.train.string_producer(string_tensor,shuffle=True)`
      * string_tensor：含有文件名+路径的1阶张量（列表）
      * num_epochs：设置过数据的次数，默认多次以满足批处理队列的大小
      * return 文件队列
2. 读取与解码：阅读器默认每次只读取一个样本<br>

**读取：**

  * 读取文本：`tf.TextLineReader()`
    * 阅读文本文件csv格式，默认按行读取
    * return 读取器实例
  * 读取图片：`tf.WholeFileReader()`
    * return 读取器实例
  * 读取二进制文件：`tf.FixedLengthRecordReader(record_bytes)`
    * 读取每个记录是固定数量字节的二进制文件
    * record_bytes：整型，指定每次读取（一个样本）的字节数
    * return 读取器实例
  * 读取TFRecords文件：`tf.TFRecordReader()`
    * return 读取器实例
  
> 所有读取器实例都有一个通用的read()方法，使用该方法读取文件名队列后，会返回key和value。<br>
* `key,value = reader.read(file_queue)`
  * key：文件名
  * value：一个样本内容
  * 由于默认只会读取一个样本，因此进行批处理时需要使用`tf.train.batch`或者`tf.train.shuffle_batch`进行批处理操作，便于之后指定每批次多个样本的训练。

**解码：**

  * 解码文本文件内容：`tf.decode_csv()`
  * 解码JPEG编码图像：`tf.image.decode_jpeg(contents)`
    * 将jpeg图像解码为unit8张量
    * return unit8张量，3-D形状 [height， width， channels]
  * 解码png编码图像：`tf.decode_png(contents)`
    * 将png图像解码为unit8张量
    * return unit8张量，3-D形状 [height， width， channels]
  * 解码二进制文件内容：`tf.decode_raw()`
    * 二进制读取为unit8类型
    
  > 解码阶段默认所有内容都被转换为unit8类型，可以使用`tf.cast()`转换为其他指定类型。

3. 批处理队列
  > 解码之后，可以直接获取默认的一个样本内容了，但如果想要获取多个样本，需要加入到新的队列进行批处理。
  * 读取指定大小（个数）的张量：`tf.train.batch(tensors,batch_size,num_threads=1,capacity=32,name=None)`
    * tensors：包含张量的列表，批处理的内容放到列表中
    * batch_size：从队列中读取的批处理大小
    * num_threads：进入队列的线程数
    * capacity：整数，队列中元素的最大数量
    * return tensors
  * `tf.train.shuffle_batch()`

4. 手动开启线程
  > 以上用到的队列都是tf.train.QueueRunner对象
  * 实例化线程协调器：`coord = tf.train.Coordinator()`
  * 开启线程：`tf.train.start_queue_runners(sess=None, coord=None)`
    * sess：所在的线程
    * coord：线程协调器
    * return 所有线程
  * 回收线程：
    * `coord.request_stop()`
    * `coord.join(threads)`

## 图片数据处理：

在进行图像识别时，每个图片样本的特征数量要保持一致，所以要将所有图片张量大小统一转换。
* `tf.image.resize_images(images,size)` 缩小放大图片
  * images：要改变形状的图片数据4-D形状（多张图片）或3-D形状（单张图片）
  * size：1-D形状 int32 张量[new_height, new_width]
  * return 3-D或4-D形状图片

> 存储时一般使用unit8格式以便节约空间，矩阵计算时使用float32格式以提高精度

## TFRecords文件处理：

TFRecords文件也是一种二进制文件，她能够更好的利用内存，更方便复制和移动，并且不需要单独的标签文件。

#### 写入TFRecords文件使用步骤：

1. 获取数据
2. 将数据填入到Example协议内存块
3. 将协议内存块序列化为字符串，并通过`tfwriter=tf.python_io.TFRecordWriter(path)`写入到TFRecords文件（文件格式：*.tfrecords）
4. `tfwriter.write(record)` 将序列化后的文件写入一个example
5. `tfwriter.close()` 关闭文件写入器

#### Example结构解析：

```
features{
    feature{
        key:"image"
        value{
            bytes_list{
                value:"\377\374\375\372\356\351\365\361\350\356\352..."
            }
        }
    }
    feature{
        key:"label"
        value{
            int64_list{
                value:9
            }
        }
    }
}
```
* 写入tfrecords文件：`tf.train.Example(features=None)`
  * features：tf.train.Features类型的特征实例
  * return：example格式协议块
* 构建每个样本的信息键值对：`tf.train.Features(feature=None)`
  * feature：字典数据，key为要保存的名字
  * value为tf.train.Feature实例
  * return Feature类型
* `tf.train.Feature(options)`
  * options：例如：
    * bytes_list=tf.train.BytesList(value=[Bytes])
    * int64_list=tf.train.Int64List(value=[Value])
    * float_list=tf.train.FloatList(value=[value])
    
```
example = tf.train.Example(features=tf.train.Features(feature={
    "image":tf.train.Feature(bytes_list=tf.train.BytesList(value=[image])),
    "label":tf.train.Feature(int64_list=tf.train.Int64List(value=[label]))
}))

example.SerializeToString()  # 序列化example
```

#### 读取TFRecords文件

读取TFRecords文件基本和读取其他类型文件一样，只是在读取和解析之间还有一个解析Example的步骤。<br>

* 使用解析器：`tf.parse_single_example(serialized,features=None,name=None)`
  * serialized：变量字符串tensor，一个序列化的Example
  * features：dict字典，键为读取的名字，值为FixedLenFeature
  * return：一个键值对组成的字典，键为读取的名字
* `tf.FixedLenFeature(shape,dtype)`
  * shape：输入数据的形状，一般不指定。为空列表
  * dtype：输入数据的类型，与存储进文件的类型要一致
  * 类型只能是float32，int64，string
```
feature = tf.parse_single_example(values,features={
    "image":tf.FixedLenFeature([],tf.string),
    "label":tf.FixedLenFeature([],tf.int64)
})

image = feature["image"]
label = feature["label"]
```
