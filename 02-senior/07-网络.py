# tcp/ip协议(族)：所有网络协议的总称包含成百上千协议，规范网络数据传递
# 链路层(物理层+数据链路层)→传输层→网络层→应用层(会话层+表示层+应用层)
# 端口：就好比是噫个房子的门，是出入这间房子的必经之路，相同的应用间传输数据会使用同样的端口(端口来区分进程)
# 端口号：端口号只有整数，范围是0到65535（端口号是按照一定的规定进行分配的）
# 端口号分为知名端口和动态端口
# 知名端口号范围为0到1023，一般作用都是固定的，80端口为HTTP服务；21端口为FTP服务；22端口为SSH
# 动态端口范围为1024到65535，它就不是固定被分配某种服务，而是动态分配
# 在Linux系统中输入命令 netstat -an 查看端口状态

# ip地址的作用是标记唯一的一台电脑，相当于家庭地址
# 每一个ip地址包括两部分：网络地址和主机地址（主机地址最大值与最小值都不能用）
# 网络号+ 0 代表网络号；网络号+ 255（最大值）代表广播地址
# A类地址范围：1.0.0.1 ~ 126.255.255.254    网络地址最高位必须是0
# B类地址范围：128.1.0.1 ~ 191.255.255.254  网络地址最高位必须是10
# C类地址范围：192.0.1.1 ~ 223.255.255.254  网络地址最高位必须是110
# D类地址用于多点广播，其ip地址第一个字节以1110开始他是一个专门保留的地址
# 在那么多类地址中，有一小部分ip是用于局域网的，属于私有ip，不在公网中使用
# 10.0.0.0 ~ 10.255.255.255
# 172.16.0.0 ~ 172.31.255.255
# 192.168.0.0 ~ 192.168.255.255
# 127.0.0.0 ~ 127.255.255.255 这个范围内的ip地址用于回路测试

# http协议属于应用层；TCP、UDP属于传输层

print("==========socket(套接字)==========")
from socket import *
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1.创建套接字
# 以上为tcp套接字，特点速度不是很快，但稳定
s = socket(AF_INET,SOCK_DGRAM)
# udp套接字，特点速度快，但容易丢数据
sendAddr = ("192.168.1.103",8080)  # 接收方IP地址和端口
sendData = input("输入要发送的内容：")
s.sendto(sendData.encode("utf-8"),sendAddr)  # 2. 发送
# 字符串.encode("utf-8") 编码转译，sendto方法只支持byte类型
# decode("GB2312") 解码


print("==========绑定端口==========")
udpSocket = socket(AF_INET,SOCK_DGRAM)  # 1.创建
bindAddr = ("",7777)  # IP地址一般不用写
udpSocket.bind(bindAddr)
# 2.绑定程序的端口号，如果不写，程序会随机分配端口
receiveData = udpSocket.recvfrom(1024)  # 1024表示本次接受的最大字节数
print(receiveData.decode("gb2312"))  # 3.接收并显示对方发送的数据
udpSocket.close()


print("==========udp广播==========")  # 广播只能在udp中使用
broadcastSocket = socket(AF_INET,SOCK_DGRAM)  # 创建udp套接字
broadcastSocket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
destAddr = ('<broadcast>',7788)  # 目标的广播地址
s.sendto(b"hi",destAddr)


print("==========tcp服务端创建==========")
serviceSocket = socket(AF_INET,SOCK_STREAM)  # 创建tcp套接字
serviceSocket.bind(("",1234))  # 绑定端口
serviceSocket.listen(5)  # 可同时处理五个客户端
clientSocket,clientAddr = serviceSocket.accept()  # 被动接收客户端信息，并创建了客户端套接字
clientData = clientSocket.recv(1024)  # 从客户端套接字接受信息
clientSocket.send(b"asdasd")  # 向客户端套接字发送信息
print("%s:%s"%(str(clientAddr),clientData))
clientSocket.close()
serviceSocket.close()
# 在tcp传输中，如果有一方收到了对方的数据，就一定会发送ack确认包给对方
# 而在udp中却没有这个过程，因此tcp稳定而udp不稳定

print("==========tcp客户端创建==========")
cSocket = socket(AF_INET,SOCK_STREAM)  # 创建tcp套接字
cSocket.connect(("192.168.116.189",1234))  # 连接到服务端ip和端口
cSocket.send(b"asdsad123")  # 给服务端发送信息
recvData = cSocket.recv(1024)  # 接收服务端信息
print(recvData)


print("==========socket(套接字) 属性==========")
v = serviceSocket.family  # 获取地址类型（IPV4/IPV6/unix本地）
v2 = serviceSocket.type  # 获取套接字类型（UDP/TCP）
serviceSocket.getsockname()  # 获得服务端绑定的地址和端口
serviceSocket.fileno()  # 获得文件描述符
clientSocket.getpeername()  # 获得客户端（连接端）的套接字地址和端口
serviceSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)  # 设置套接字选项（大选项、小选项、值）
serviceSocket.setblocking(False)  # 将套接字设置为非阻塞，默认为True阻塞
serviceSocket.settimeout(3)  # 设置套接字只阻塞三秒


print("==========struct结构，将数据结构化==========")
import struct
st = struct.Struct("f3si")  # 构建数据的结构（浮点、三字符、整型）
data = st.pack(9.02, b'hai', 4)  # 将数据按照之前定义的结构打包
print(data)
data2 = st.unpack(data)  # 将数据按照之前定义的结构解包
print(data2)

# ip地址与网络掩码按位与运算即可获得网络号
# 多台电脑连接组成网络时需要用到集线器（hub）
# 两台电脑之间能够进行通信的前提是，他们处于同一网段（网络号）内
# icmp协议：ping一个ip地址（ping通需要IP地址和mac地址）
# arp协议：以广播方式获取一个电脑的网卡号（mac地址/物理地址）
# rarp协议：根据mac地址找ip地址
# 路由器可以连接不同网段的网络，使他们之间能够通信
# mac地址在两个设备间通信时会变化(目标会变为相邻的两个路由或主机的mac地址)；而ip地址在整个通信中都不会发生任何变化
# 如果要发送的ip不在同一网段内，则会把这个数据转发给默认网关
# dns解析域名（udp协议）、DHCP自动给没有IP的电脑分配ip

# 访问百度的过程：
# 1.使用arp获取默认网关的mac
# 2.将数据发送至默认网关，默认网关将数据转给路由器
# 3.路由器选择合适路径转发给目的地的默认网关，目的网关再把数据交给dns服务器
# 4.dns解析域名获取IP地址后原路返回给发出请求的client
# 5.获得ip后，发出tcp数据（3次握手）
# 6.并使用http协议发送请求数据给web服务器
# 7.web收到请求，发送数据至客户端
# 8.浏览器显示网页，并关闭tcp连接（4次挥手）

# tcp连接：
# 三次握手：一方先发syn请求数据，另一方收到后返回syn+ack，收到后再返回ack（建立通道）
# 四次挥手：一方调用close()后发送fin+ack数据包，另一方接收后返回ack数据包
# 并也调用close()，然后再将已经调用close的情况告知对方(fin包)，对方收到后再返回ack包

# 长连接：在三次握手四次挥手内，就将数据全部传输完毕，如在线视频
# 短链接：数据不是一次全部传输完毕而是分批次传输，期间进行多次三次握手四次挥手，如网页

# ping一个地址时，会在末尾有一个TTL数据。ttl代表经过的路由器个数，128-n，经过的路由器越多，数字越小
# MSL：指一个数据包在网络上能存活的最大时间（1-2分钟）
# 客户端四次挥手中TIME_WAIT状态到CLOSED的状态的时间等于2MSL
# NAT网络地址转换器，将自己的局域网ip转换为公有ip

