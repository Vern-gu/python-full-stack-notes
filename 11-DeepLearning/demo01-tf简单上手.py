import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 不显示警告
tf.compat.v1.disable_eager_execution()  # tensorflow2 使用旧版本功能需要调用该方法


def demo1():
    # 构建图：
    a=tf.constant(2,name='a')  # 设定常量
    b=tf.constant(3,name='b')
    c=tf.add(a,b,name='c')
    print(a,'\n',b)
    print(c)
    print(a.graph)

    # 执行图：
    with tf.compat.v1.Session() as sess:
        c_value=sess.run(c)
        print("c_value",c_value)
        print("sess_graph:",sess.graph)

        # 将图写入本地生成events文件
        # tf.compat.v1.summary.FileWriter("./summary", graph=sess.graph)


def tensor_demo():
    a=tf.constant(3.0)  # 标量（零阶张量）
    b=tf.constant([1,2,3,5,6,9])  # 向量（一阶张量）
    c=tf.constant([
        [1,2,3],
        [4,5,6]
    ])  # 矩阵（二阶张量）
    d=tf.constant([
        [
            [1,2],
            [2,3]
        ],
        [
            [3,4],
            [4,5]
        ]
    ])  # 三维数组（三阶张量）
    print(a,b,c,d)


def variable_demo():
    a=tf.Variable(initial_value=50,name='a')
    b=tf.Variable(initial_value=40)
    c=tf.add(a,b)
    print(a,b,c)

    init = tf.compat.v1.global_variables_initializer()

    with tf.compat.v1.Session() as sess:
        sess.run(init)
        print(sess.run(c))


if __name__ == '__main__':
    # demo1()
    # tensor_demo()
    variable_demo()


