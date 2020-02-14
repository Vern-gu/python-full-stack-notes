# nginx的默认目录结构：
# 所有的配置文件都在/etc/nginx下，并且每个虚拟主机已经安排在了/etc/nginx/sites-available下
# 程序文件在/usr/sbin/nginx
# 日志放在了/var/log/nginx中
# 并已经在/etc/init.d/下创建了启动脚本nginx
# 默认的虚拟主机的目录设置在了/var/www/nginx-default
# (有的版本 默认的虚拟主机的目录设置在了/var/www, 请参考/etc/nginx/sites-available里的配置)

# ---
# 检查配置文件是否正确：nginx -t
# 查看编译选项：nginx -V
# 重启nginx：nginx -s reload (-s 表示service)
# 关闭nginx：nginx -s stop
# 优雅停止服务：nginx -s quit（等待客户端传送完数据，不再有连接后关闭服务）
# ubuntu可以使用 service nginx status/start/reload/stop 来查看状态/开启/重启/关闭nginx服务

# ---
# nginx配置：
# nginx配置文件主要分为六个区域：
# main 全局设置
#   user 指定worker进程运行用户以及用户组，默认nobody
#   worker_processes 指定nginx开启的子进程数
#   error_log 定义全局错误日志文件路径，输出级别有debug、info、notice、warn、error、crit（debug最详细，crit最简略）
#   pid 用来指定进程id的存储文件位置
#   worker_rlimit_nofile 指定一个nginx进程可以打开的最多文件描述符数目
# events 指定nginx工作模式以及连接数上限
#   use 用来指定nginx工作模式，（select、poll、kqueue、epoll、rtsig、/dev/poll，linux首选epoll）
#   worker_connections 用于定义nginx每个进程的最大连接数，即接收前端的最大请求数，由processes和connections决定
# http http设置，核心模块，负责http服务器相关属性的配置，其中server和upstream子模块至关重要
#   include 设定文件的mine类型，在配置文件下的mine.type文件定义，告诉nginx来识别文件类型
#   default_type application/octet-stream; 设定了默认的类型为二进制流，当文件类型未定义时使用该方法，例如在没有配置asp的locate环境时，nginx不予解析，此时用浏览器访问asp文件就会出现下载
#   sendfile 用于开启高效文件传输模式。将tcp_nopush和tcp_nodelay两个指令设置为on用于防止网络阻塞
#   keepalive_timeout 设置客户端连接保持活动的超时时间。在超过这个时间后，服务器会关闭该连接
#   sever 主机设置，是http的一个子模块，用来定义一个虚拟主机
#       listen 监听的端口
#       sever_name 服务器域名
#       location URL配置 用于定位，支持正则匹配，可以对动、静态网页进行过滤处理（根据路径选择相应的代理）
#   upstream 负载均衡服务器设置


# python中的fabric库可以实现自动化部署服务器

