import tensorflow as tf


tf.compat.v1.disable_eager_execution()
# 使用tf自实现一个线性回归
# 1.准备数据
with tf.compat.v1.variable_scope("prepare_data"):
    x = tf.random.normal((100,1),name='feature')
    y = tf.matmul(x,[[0.8]]) + 0.7
    print(x,y)
# 2.构建模型
with tf.compat.v1.variable_scope("create_model"):
    weights = tf.Variable(initial_value=tf.random.normal((1,1)),name='weights')
    bias = tf.Variable(initial_value=tf.random.normal((1,1)),name='bias')
    predict = tf.matmul(x,weights) + bias
# 3.构造损失函数
with tf.compat.v1.variable_scope("create_loss"):
    loss = tf.reduce_mean(tf.square(predict-y))
# 4.优化损失
with tf.compat.v1.variable_scope("optimizer_loss"):
    optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)
# 5.初始化变量
init = tf.compat.v1.global_variables_initializer()

# 收集变量：
tf.compat.v1.summary.scalar('loss',loss)
tf.compat.v1.summary.histogram('weights',weights)
tf.compat.v1.summary.histogram('bias',bias)
# 合并变量：
merged = tf.compat.v1.summary.merge_all()

# 6.开启会话：
with tf.compat.v1.Session() as sess:
    sess.run(init)
    file_writer = tf.compat.v1.summary.FileWriter('./summary',graph=sess.graph)  # 创建事件文件
    print("训练前权重为%f，偏置为%f，损失为%f" % (weights.eval(), bias.eval(), loss.eval()))
    for i in range(100):
        sess.run(optimizer)

        summary = sess.run(merged)  # 运行合并变量操作
        file_writer.add_summary(summary,i)  # 将每次迭代后的变量写入事件文件

    print("训练后权重为%f，偏置为%f，损失为%f" % (weights.eval(), bias.eval(), loss.eval()))

