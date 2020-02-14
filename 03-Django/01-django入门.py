# 大多数的web开发框架使用MVC框架
# M:module  V:view  C: control
# Django采用的是MVT框架，它的核心控制部分是view
# T: 代表template相当于mvc框架中的view，负责呈现内容到浏览器
# V:核心，负责接受请求、获取数据、返回结果
# M:负责与数据库交互

# linux创建虚拟环境virtualenv 环境名（新的环境默认存储与home目录下）
# 进入虚拟环境：activate/source 环境名
# 退出虚拟环境deactivate

# 新建django项目：django-admin startproject mysite（创建的项目在当前目录下）
# 创建app：python manage.py startapp testbook
# 在urls.py里写域名关系
# 在views.py里写函数
# 启动django程序：python manage.py runserver 127.0.0.1:8000

# ===========================设计模型============================
# 在app中的models.py创建模型类（sql结构）
# 激活模型：编辑setting.py文件，将创建的应用加入到installed_apps中
# 生成迁移：根据模型类生成sql语句  python manage.py makemigrations
# 执行迁移：python manage.py migrate
# 使用python manage.py shell 往表中添加数据（也可以登陆管理员页面添加数据）
# 先要导入模块from testbook.models import *
# 为类创建对象，对象.属性='值' 来输入数据
# 查看添加的数据：BookInfo.objects.all()
# 选中数据：b = BookInfo.objects.get(pk=?)  # pk(primary key)
# 选中数据后才能执行修改或删除操作（重新赋值即修改；对象.delete()删除数据）
# 执行完更改增加操作后要b.save()保存
# ===========================管理站点============================
# 创建管理员：python manage.py createsuperuser  按提示输入用户名、邮箱、密码
# 登陆：127.0.0.1:8000/admin
# 在admin.py中注册到管理员
# 可直接在admin页面管理app
# =============================视图==============================
# 在项目文件夹下创建模板文件夹，在其中放好html文件
# 在urls.py中配置好url对应的函数
# 在views中写好函数用render渲染html
# 在settings.py中的TEMPLATES列表中添加DIRS，将模板文件夹放入


# 将Django默认的sqlite3数据库导出：