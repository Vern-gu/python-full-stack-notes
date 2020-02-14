def count(string):
    """获取字符串中各个字符出现的次数"""
    dic = {}
    for i in string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


if __name__ == '__main__':
    string = "asfsfaslkjvkjasfjqoiwjoijwq;';;;';()$%^&<>/.,,"
    print(count(string))
