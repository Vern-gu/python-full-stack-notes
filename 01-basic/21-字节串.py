# 创建空字节串：ｂ''
# 创建非空字节串：b'abcd'
# 字节串的构造函数：bytes
#   bytes() 生成一个空字节串，等同于b''
#   bytes(整型可迭代对象) 用可迭代对象初始化一个字节串
#   bytes(整数n) 生成n个值为0的字节串
#   bytes(字符串，encoding='utf8') 用字符串的转换编码生成一个字节串

# bytes 与 str  的区别：
#   bytes 存储字节（0-255）
# 　str   存储字符（用来表示文字信息，值为 0-65535或更大）

# bytes 与 str转换
#            编码（encode） 　　
# 　str  --------------------> bytes
#   b=s.encode('gbk')
#
#            解码(decode)
# 　bytes  ------------------> str
#   s=b.decode('gbk')



