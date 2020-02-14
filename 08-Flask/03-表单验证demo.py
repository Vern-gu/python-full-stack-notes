"""
简单的登录逻辑处理
1.路由需要有get和post两种请求方式
2.获取到提交的表单信息
3.检查表单参数是否都有填写
4.核对表单信息
"""
"""
flash模块用于和模板传递消息
flash中的内容需要加密，因此需要设置secret_key
模板中需要遍历消息 get_flashed_messages()
"""

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'alab'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not all([username, password, password2]):
            flash('信息不完整')
        elif password2 != password:
            flash('密码不相同')
        else:
            return '注册成功！'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
