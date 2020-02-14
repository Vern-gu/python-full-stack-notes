# ctrl+/ 注释掉选中的内容

print("==========正则表达式==========")
# 在python中需要通过正则表达式对字符串进行匹配的时候，可以使用re模块
import re
result = re.match("vern","vern")  # (规则表达式, 要匹配的字符串)
print(result.group())  # 如果上一步匹配到数据的话，就可以使用group方法提取数据
r"""
正则表达式匹配规则：
一、表示字符
.   匹配任意一个字符
[]  匹配[]中列举的字符,[]中列举的字符不用隔开，[]中加入^ 表示取反
\d  匹配数字，即0-9  == [0-9]
\D  匹配非数字，即不是数字  == [^0-9]
\s  匹配空白，即空格、tab键
\S  匹配非空白
\w  匹配字母字符，即a-z、A-Z、0-9、_  == [0-9a-zA-Z_]
\W  匹配非字母字符
二、表示数量
*   匹配前一个字符出现0次或无数次，即表示该字符可有可无
+   匹配前一个字符出现一次或无数次，即表示该字符要至少出现一次
?   匹配前一个字符出现1次或者0次，即要么有一次，要么没有
{m} 匹配前一个字符出现m次
{m,}匹配前一个字符至少要出现m次
{m,n}匹配前一个字符出现m到n次
三、原始字符串
在规则表达式前添加一个r，可以忽略掉转译的部分
四、表示边界
^   匹配字符串开头，表示必须以某个字符开头
$   匹配字符串结尾，表示必须以某个字符结尾
\b  匹配一个单词的边界，所匹配的单词必须是在边界处，即旁边有空格或tab
\B  匹配非单词边界
五、匹配分组
|   匹配左右任意一个表达式
(ab)将括号中字符作为一个分组  用groups可以找到多个分组
\num应用分组num匹配到的字符串
(?P<name>)  分组起别名，注意P大写
(?P=name)   引用别名为name分组匹配到的字符串
"""
result2 = re.search(r"\d+","浏览量208")  # search方法当找到符合条件的字符后就结束了
print(result2.group())

result3 = re.findall(r"\d+","身高182、体重65")  # findall查找所有符合条件的字符，返回列表
print(result3)  # findall没有group方法

def replace(ret):
    r = int(ret.group())+100
    return str(r)

result4 = re.sub(r"\d+",replace,"python=2000; java=1200")
# sub方法可以替换正则所搜索到的字符
print(result4)

s = "apple,banana;orange-peach"
result5 = re.split(r",|;|-",s)  # 分割字符串，返回列表
print(result5)

# 贪婪模式：前一个正则表达式会尽可能多的匹配符合的字符
str = "it's a number 234-12-45-234"
result6 = re.match(r"(.+)(\d+-\d+-\d+-\d+)",str)
print(result6.groups())

# 关闭贪婪模式：在前一段正则最后添加 ? 即可，尽可能少地匹配
result7 = re.match(r".+?(\d+-\d+-\d+-\d+)",str)
print(result7.group(1))



# 补充：
pattern = re.compile('\d')  # 将正则表达式编译为一个pattern对象
# 创建对象后，无需再定义正则
# re.I  # 忽略大小写
# re.S  # 全文匹配

