# 接受web请求，并返回web响应
# 视图就是一个python函数，被定义在views.py中
# 响应可以是一张网页的HTML内容，一个重定向，一个404错误等
# 响应处理过程：
# 1.用户输入网址
# 2.django获取用户输入的地址
# 3.使用正则匹配url的信息，记录下对应的方法名称
# 4.调用找到的方法，接收request以及正则中获取的值，处理并返回response对象


# include()、path()方法还可以在最后添加一个name(namespace)参数，用于url的反向解析


# request对象：
# 构建视图函数时，第一个传入的参数永远是request
# 我们可以获得request参数的部分属性
# path：一个字符串，表示请求的页面的完整路径，不包含域名
# method：一个字符串，表示http请求的方法
# encoding：一个字符串，表示提交的数据的编码格式
#           如果为None则表示使用浏览器的默认设置，一般为utf-8
#           该属性可写，可以通过修改他来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的编码
# GET：一个类似于字典的对象，包含get请求方式的所有参数
# POST：一个类似于字典的对象，包含post请求方式的所有参数
# FILES：一个类似于字典的对象，包含所有的上传文件
# COOKIES：一个标准的python字典对象，包含所有cookie，键值都是字符串
# session：一个可读写的类似字典对象，表示当前的会话（只有django启用会话支持才可用）
# is_ajax()：如果请求是通过XMLHttpRequest发起的，则返回True

# 上述的类似的字典对象实际是定义在django.http.QueryDict中的对象
# python字典对象是不允许键重复的，但QueryDict允许键重复（即一个键有多个值）
# get()方法来可以据键获取值，若有多个值则获取最后一个值
# 使用方法：dict.get('键',default) 或 dict['键']
# getlist()方法可以根据一个键获取所有值，dict.getlist('键',default)

# get请求参数体现在url中，?参数=值&参数=值....


# response对象：
# write(content):以文件的方式写
# flush():以文件的方式输出缓存区
# set_cookie(key,value='',max_age=None,expires=None):设置cookie
#       max_age指定秒数后过期
#       expires是一个datetime对象，在指定的日期/时间后过期
#       max_age与expires二选一使用


# session使用：
# 启用会话后，每个HttpRequest对象将有一个session属性，类字典对象
# get(key,default=None):根据键获取会话的值
# clear():清除所有会话
# flush():删除当前的会话数据，并删除会话的cookie
# del request.session['member_id']:删除会话
# set_expiry(value):设置会话过期时间
# value是一个整数表示多少秒没有活动h后过期
# 如果value=0则表示关闭浏览器就过期
# 如果value=None则永不过期

# SESSION_ENGINE='django.contrib.sessions.backends.db'  存储于数据库中
# SESSION_ENGINE='django.contrib.sessions.backends.cache  存储于缓存
# SESSION_ENGINE='django.contrib.sessions.backends.cached_db'  同时存于缓存和数据库中

