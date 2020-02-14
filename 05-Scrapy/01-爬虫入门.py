# 网页三大特征：
# 1.每个网页都有自己的url来定位
# 2.网页都使用HTML来描述页面信息
# 3.网页都使用HTTP协议来传输HTML数据
# 爬虫设计思路：
# 1.首先确定要爬取的网页URL
# 2.通过HTTP协议来获取对应的HTML页面
# 3.提取HTML中需要的数据

# 通用爬虫：搜索引擎用的爬虫系统
# 工作流程：爬取页面、存储数据、内容处理、提供检索
# 聚焦爬虫：针对某种内容进行爬虫

# HTTP请求主要分为get请求和post请求
# get从服务器上获取数据、post向服务器传送数据
# cookie：通过在客户端记录的信息确定用户的身份（本地缓存）
# session：通过在服务端记录的信息确定用户的身份（服务器端缓存）
# 只要cookie和session的值一样就表示用户是匹配的

# GET https://www.baidu.com/ HTTP/1.1  # 这一行属于协议，并不算是请求报文的一部分
# （↓headers↓）
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134  # （最重要）
# (如果没有user-agent，会很容易被识别为爬虫)
# Accept-Language: zh-CN
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Upgrade-Insecure-Requests: 1  # （http升级为https，可以不写）
# Accept-Encoding: gzip, deflate, br  # （客户端可以对数据处理的压缩方式，不可以写）
# Host: www.baidu.com  # （可以不需要）
# DNT: 1
# Connection: Keep-Alive  # （保持长连接）

import random
from urllib.request import *

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/\
        537.36 Edge/17.17134'}  # 请求头是字典类型
# 因为urlopen方法发送请求agent默认为python所以很容易被认为是爬虫
# 因此应先用Request方法构造请求
request = Request("http://www.youdao.com",headers=headers)  # Request方法构造请求对象，data参数有值就是post，否则get
# 向指定的url发送请求，并返回服务器响应的类文件对象
response = urlopen(request)  # 当输入data参数时则会发送post，否则是get请求
# 服务器响应的类文件对象支持python文件对象的操作方法
html = response.read()  # python文件的read方法
# print(html.decode("utf-8"))
response.getcode()  # 返回http的响应码
response.geturl()  # 返回实际返回数据的url
response.info()  # 服务器响应的http报头

ua_list = [  # user-agent列表，不断变更可以增强伪装
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 \
    Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'
]
user_agent = random.choice(ua_list)
request.add_header('User-Agent', user_agent)  # add_header()方法添加/修改一个http报头
print(request.get_header('User-agent'))  # 获取一个已有的http报头的值，注意只能第一个字母大写


# python2.7中import urllib, cookielib
# urllib.urlencode()可以将汉字等多个字节的字符解码，它接收的是一个字典参数

# get请求与post请求区别：
# get请求的url会附带查询参数；post请求的url不带参数
# 对于get请求查询参数在QueryString中保存（Fiddler）
# 对于post请求查询参数在form表单里保存
# 爬虫时最需要关注的不是页面信息而是页面信息的来源
# AJAX方式加载的页面，数据来源一定是JSON
# 拿到json就是拿到了网页的数据
# 如果是post请求则在请求头下空一行处有请求信息

# cookie用于保存登陆信息
# 只要在请求报头内加入cookie就能无需登录，直接进入页面


url = 'http://www.baidu.com/'
http_handler = HTTPHandler()  # 构建一个http处理器对象,支持处理http请求
# 在handler中添加debuglevel=1 参数可以使打开debug模式获得收发包的信息
proxy_handler = ProxyHandler({"http": "124.88.67.54:80"})  # 构建一个代理处理器对象，支持代理发送请求
# 其中必须接受字典参数，空字典表示无代理
# 私密代理格式{"http": "account:password@IPadress:Post"}
opener = build_opener(http_handler)
request = Request(url)
response = opener.open(request)
# 如果使用了install_opener(opener)，则之后所有的请求都可以使用urlopen()方法发送（全局）

# cookie = cookielib.CookieJar()  # 构建cookiejar()对象，用来保存cookie的值
# cookie_handler = HTTPCookieProcessor(cookie)  # 该处理器对象可以处理cookie
# opener = build_opener(cookie_handler)


