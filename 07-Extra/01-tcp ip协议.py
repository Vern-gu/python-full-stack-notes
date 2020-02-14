# 物理传输媒介 -> 内核空间 -> 用户空间
#   数据链路层（网卡接口的网络驱动程序）包含ARP、DataLink、RARP协议
#   网络层包含ICMP、IP协议
#   传输层包含TCP、UDP协议
#   应用层包含ping、telnet、OSPF、DNS协议
# 应用层通过socket套接字来与传输层进行联系

# ARP协议（地址解析协议）与RARP协议（逆地址解析协议）分别负责IP地址和物理地址的解析和逆解析
# IP协议：根据数据包的IP地址决定如何投递信息，一般来讲就是主机在网络上的地址
# ICMP协议：IP协议的补充，用于检测网络连接，ping通一个ip地址时

# 通过封装使上层协议使用下层协议提供的服务
# 应用程序数据发送到物理网络之前，将会沿着协议栈从上往下依次传递，
# 每一层协议都在上层数据的基础上加上自己的头部信息，实现该层功能


# ===========================================================================================================
# HTTP是一个基于TCP/IP通信协议来传递数据
# HTTP是一个属于应用层的面向对象的协议，由于其简捷、快速的方式，适用于分布式超媒体信息系统。
# HTTP协议工作于客户端-服务端架构为上。浏览器作为HTTP客户端通过URL向HTTP服务端即WEB服务器发送所有请求。
# Web服务器根据接收到的请求后，向客户端发送响应信息。

# URL介绍：
# http://www.aspxfans.com:8080/news/index.asp?boardID=5&ID=24618&page=1#name
# 从上面的URL可以看出，一个完整的URL包括以下几部分：
# 1.协议部分：该URL的协议部分为“http：”，这代表网页使用的是HTTP协议。
#   在Internet中可以使用多种协议，如HTTP，FTP等等本例中使用的是HTTP协议。在"HTTP"后面的“//”为分隔符
# 2.域名部分：该URL的域名部分为“www.aspxfans.com”。一个URL中，也可以使用IP地址作为域名使用
# 3.端口部分：跟在域名后面的是端口，域名和端口之间使用“:”作为分隔符。
#   端口不是一个URL必须的部分，如果省略端口部分，将采用默认端口
# 4.虚拟目录部分：从域名后的第一个“/”开始到最后一个“/”为止，是虚拟目录部分。
#   虚拟目录也不是一个URL必须的部分。本例中的虚拟目录是“/news/”
# 5.文件名部分：从域名后的最后一个“/”开始到“？”为止，是文件名部分，
#   如果没有“?”,则是从域名后的最后一个“/”开始到“#”为止，是文件部分，如果没有“？”和“#”，
#   那么从域名后的最后一个“/”开始到结束，都是文件名部分。本例中的文件名是“index.asp”。
#   文件名部分也不是一个URL必须的部分，如果省略该部分，则使用默认的文件名
# 6.锚部分：从“#”开始到最后，都是锚部分。本例中的锚部分是“name”。锚部分也不是一个URL必须的部分
# 7.参数部分：从“？”开始到“#”为止之间的部分为参数部分，又称搜索部分、查询部分。
#   本例中的参数部分为“boardID=5&ID=24618&page=1”。参数可以允许有多个参数，参数与参数之间用“&”作为分隔符。
