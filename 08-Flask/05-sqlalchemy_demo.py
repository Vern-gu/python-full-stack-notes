from flask import Flask
from flask_sqlalchemy import SQLAlchenmy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1110@127.0.0.1/flask_db'
db = SQLAlchenmy(app)
"""
定义两张表：
角色表（ID/（管理员/普通用户））
用户表（ID/用户名/外键(角色ID)）
"""


class Role(db.Model):  # 继承db.Model后说明该类为数据库的一张表（模型）
    # 定义表名
    __tablename__ = 'roles'
    # 定义字段
    id = db.Colume(db.Integer, primery_key=True)
    name = db.Column(db.String(16), unique=True)

    # 一对多，在一的一方写关联
    # 表示和User模型发生了关联，增加了一个users属性
    # backref反向引用
    users = db.relationship('User', backref='Role')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primery_key=True)
    uname = db.column(db.String(16), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # user中需要添加一个role属性以便显示哪些用户是管理员，但是该属性的定义需要在另一个模型中定义


@app.route('/')
def index():
    return 'flask'


if __name__ == '__main__':
    app.run(debug=True)

