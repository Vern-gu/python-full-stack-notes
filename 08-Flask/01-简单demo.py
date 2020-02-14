"""
1.导入flask扩展
2.创建flask应用程序实例
3.定义路由及视图函数
4.启动程序
"""
from flask import Flask


app = Flask(__name__)  # 需要传入‘__name__’，作用是为了确定资源所在的路径


@app.route('/', methods=['POST', 'GET'])  # flask中定义路由是通过装饰器来实现的
def index():
    return 'awesome!'


@app.route('/orders/<int:order_id>', methods=['GET'])
# <>内可以定义路由的参数，需要为该参数起名，int：是为了限制用户传入的参数类型必须为int
def order(order_id):  # 视图函数内需要传入参数名，后续才可以使用该参数
    print(type(order_id))
    return str(order_id)


if __name__ == '__main__':
    app.run(debug=True)  # 运行一个简易服务器，测试用
