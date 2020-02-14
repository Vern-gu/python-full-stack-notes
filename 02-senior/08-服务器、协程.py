"""
常见网络攻击：
1.tcp半链接攻击：也称syn flood是一种DoS攻击，向服务器不断发送syn数据包，却不返回ack数据包，使其经不住负荷失去响应
2.dns攻击：将一个域名指向另一个IP地址
3.arp攻击：arp主要是获取dest的mac地址，而arp攻击则可以给出虚假的mac地址欺骗对方
4.csrf跨域攻击：网页会随机生成一个值用来匹配用户，保证同源策略
"""

print("==========多任务服务器==========")
'''
from multiprocessing import Process
from socket import *

def connect(clSocket,clAddr):
    while True:
        recvData = clSocket.recv(1024)
        if len(recvData) > 0:
            print("%s:%s" % (str(clAddr), recvData))
        else:
            print("%s已终止连接" % str(clAddr))
            break
    clSocket.close()

def main():
    severSocket = socket(AF_INET, SOCK_STREAM)
    severSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 重复使用绑定的端口信息,即不用等待2msl
    severSocket.bind(("", 9090))
    severSocket.listen(5)

    try:
        while True:
            clSocket, clAddr = severSocket.accept()
            clProcess = Process(target=connect,args=(clSocket,clAddr))
            clProcess.start()
            clSocket.close()  # 因为多进程中数据不共享，当子进程拷贝了父进程中的套接字后就可以关闭
    finally:
        severSocket.close()

if __name__ == "__main__":
    main()
'''

print("==========单任务非堵塞服务器==========")
"""
from socket import *

serSocket = socket(AF_INET,SOCK_STREAM)
serSocket.bind(("",9090))
serSocket.listen(5)
serSocket.setblocking(False)  # 使这个套接字变为非堵塞
clAddrList = []  # 用来保存所有已连接的客户端信息
while True:
    try:
        clSocket,clAddr = serSocket.accept()
    except:
        pass
    else:
        print("一个新的客户端到来%s"%str(clAddr))
        clSocket.setblocking(False)
        clAddrList.append((clSocket,clAddr))

    for clSocket,clAddr in clAddrList:
        try:
            clData = clSocket.recv(1024)
        except:
            pass
        else:
            if len(clData) > 0:
                print("%s:%s"%(str(clAddr),clData))
            else:
                clSocket.close()
                clAddrList.remove((clSocket,clAddr))
                print("客户端%s断开连接"%str(clAddr))
"""

print("==========select版服务器（单任务）==========")
# 优点：跨平台；缺点：32位机器可以监控的套接字最多只能有1024个，64位2048个,效率较低
# 后开发出了poll，其使用方法与select一致，但没有套接字数量限制，但是poll与select都是采用的轮询方式，效率都较低
'''
from socket import *
from select import *

sever = socket(AF_INET,SOCK_STREAM)
sever.bind(("",9090))
sever.listen(5)
socketsInput = [sever]
while True:
    readable,writable,exceptional = select(socketsInput,[],[])  # 阻塞等待符合条件的套接字
    for socket in readable:
        if socket == sever:
            client,clAddr = socket.accept()
            socketsInput.append(client)
        else:
            clData = socket.recv(1024)
            if clData:
                socket.send(clData)
            else:
                socket.close()
                socketsInput.remove(socket)
'''

# 对象.fileno() ----> 是一个数字，称为文件描述符
# sys.stdin标准输入（键盘 0）；sys.stdout标准输出（屏幕 1）；sys.stderr标准错误（屏幕 2）
print("==========epoll==========")
"""
# 没有使用轮询，而是采用了事件通知机制，效率较高
from socket import *
import select

s = socket(AF_INET,SOCK_STREAM)
s.bind(("",8900))
s.listen(10)
epoll = select.epoll()  # 创建一个epoll对象
epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)
# 注册事件到epoll中，将创建的套接字添加至epoll的事件监听中
# EPOLLIN表示只检测是否有接收事件，EPOLLET表示ET模式，默认为LT模式
# LT模式，当有事件时，若不及时处理，下一次仍会通知；ET模式，有事件时必须立即处理，下一次不会通知
# | 竖杠表示或运算，相当于在原有基础上添加了功能
# ET 效率大于LT
clSockets = {}
clAddr = {}
while True:
    epoll_list = epoll.poll()
    # epoll进行fd扫描，将有事件的对象放入列表中，未指定超时时间则堵塞
    for fd,event in epoll_list:
        if fd == s.fileno():
            client,addr = s.accept()
            print("新客户端%s到来"%str(addr))
            clSockets[client.fileno()] = client
            clAddr[client.fileno()] = addr
            epoll.register(client.fileno(),select.EPOLLIN|select.EPOLLET)
        elif event == select.EPOLLIN: # 判断事件是否为收数据的事件
            clData = clSockets[fd].recv(1024)
            # 根据文件描述符找到对应的客户端套接字
            if clData:
                print("%s:%s"%(str(clAddr[fd]),clData))
            else:
                print("%s已断开连接"%str(clAddr[fd]))
                epoll.unregister(fd)
                clSockets[fd].close()
"""
# 计算密集型：需要计算机不停的计算，需占用大量cpu资源，由于多线程无法充分发挥多核性能，因此要用多进程处理
# IO密集型：需要网络功能，大多的时间用来等待网络数据的到来，多线程、协程处理较好
print("==========协程==========")
import time
def test1():
    while True:
        print("---1---")
        yield None   # 若在函数内部添加了yield则这个函数就不会被执行直到调用next
        time.sleep(0.5)
def test2():
    while True:
        print("---2---")
        yield None
        time.sleep(0.5)

t1 = test1()
t2 = test2()
while True:
    t2.__next__()
    next(t1)
