# 应用层：解决要传递什么数据
# 传输层：解决如何传数数据（udp   tcp）
# 网络层： 对方的IP地址
# 链路层：具体的传输工具

print("==========HTTP协议==========")
# http：超文本传输协议
# 是一种发布和接受HTML页面的方法
# https在http下加入了ssl层（安全套接层），在传输层对网络连接进行加密，保证数据传输的安全
# http默认端口80、https端口为443
'''
http请求方式：
get 获取数据
post 修改数据
put 保存数据
delete 删除数据
option 询问服务器的某种支持特性
head 返回报文头
'''
# URL：全局资源定位

# 请求头-请求体
# 响应头-响应体


print("==========静态web服务器==========")
import re
from socket import *
from multiprocessing import Process


# 设置静态文件根目录
ROOT_DIR = "c:/users/问杰/Desktop/python笔记"


def recv_request(clSocket):
    """处理客户端请求"""
    response_headers = "Sever: My sever\r\n"
    # 浏览器传输来的数据也是byte格式
    request = clSocket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    for lines in request_lines:
        print("request:", lines)
    request_start_line = request_lines[0]  # 解析请求报文
    file_name = re.match(r"\w+\s+(/[^ ]*)", request_start_line).group(1)
    print(file_name)
    # 提取请求的路径
    if "/" == file_name:
        file_name = "/index.html"
    try:
        htmlFile = open(ROOT_DIR + file_name,"r")
        file = htmlFile.read()
        htmlFile.close()
    except:
        response_start_line = "HTTP/1.1 404 NOT FOUND\r\n"
        response_body = "404 NOT FOUND"
    else:
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_body = file
    response = response_start_line + response_headers + "\r\n" + response_body
    clSocket.send(response.encode("utf-8"))
    # 网络传输的必须是byte类型，因此也可以是send(bytes(response,"utf-8"))
    # print("response:", response)
    clSocket.close()


def main():
    webS = socket(AF_INET, SOCK_STREAM)
    webS.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    webS.bind(("", 8000))
    webS.listen(128)
    while True:
        client, addr = webS.accept()
        print("[%s:%s] has connected"%addr)  # addr是元组，可以直接解包
        clp = Process(target=recv_request, args=(client,))
        clp.start()
        client.close()

if __name__ == "__main__":
    main()


# WSGI接口以实现动态网页，操作步骤：
# 在框架内导入需要实现的模块
# m = __import__(file_name)   # 模块导入
# m.application(environ,start_reponse)  # 调用该模块，该模块将相应体传回
# 模块内的响应头通过传进去的start_response方法传回来
# start_response方法主要用于处理模块内传递回来的响应头
# 在模块内主要通过application来return响应体
