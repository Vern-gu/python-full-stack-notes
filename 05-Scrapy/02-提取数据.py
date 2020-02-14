import re
from urllib.request import *

"""
正则匹配
pattern = re.compile(r'\d+')
m = pattern.match('122112asd')
a = m.group()
print(a)
"""

url = 'http://www.baidu.com/'
header = {'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"}
request = Request(url, headers=header)
response = urlopen(request)
html = response.read().decode("utf-8")
pattern = re.compile(r'<div id="u1">(.*?)</div>', re.S)
content = pattern.findall(html)
print(content)

"""
xpath匹配
from lxml import etree  # 导入xpath匹配模块
comtent = etree.HTML(html)  # 解析html文档
content.xpath()  # 匹配xpath，返回列表
"""




