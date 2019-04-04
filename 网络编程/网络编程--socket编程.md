# python 网络编程 之 socket编程
## 客户端/服务器架构
## osi七层模型
osi七层 | 功能 | 网络协议 
- | - | - 
应用层 | 文件传输 电子邮件 文件服务 虚拟终端 | TFTP HTTP FTP SMTP DNS TELNET 
表示层 |  |  
会话层 |  |  
传输层 |  |  
网络层 |  |  
数据链路层 |  |  
物理层 |  |  

----
TCP/IP 四层 | 功能 | 协议 
- | - | - 
应用层 | 文件传输 电子邮件 文件服务 虚拟终端 | 2 
传输层 |  |  
网络层 |  |  
网络接口 |  |  

## socket层
	在 应用层 和 传输层 之间 ,socket抽象层
## socket是什么
	socket是应用层与tcp/ip协议族通信的中间软件抽象层,
	也有人说socket 是ip+port ip是用来标识互联网中的一台主机的位置,而port是用来标识这台机器上的一个应用程序,ip地址是配置到网卡上的,而port是应用程序开启的,ip与port的绑定就标识了互联网中第一无二的一个应用程序
	而程序的pid是同一台机器上不同进程或者线程的标识
## 套接字发展史及分类
1. 基于文件类型的套接字家族
	名字: AF_UNIX
2. 基于网络类型的套接字家族
	名字: AF_INET
## 套接字的工作流程
	生活场景中打电话
	服务端:服务器端先初始化socket,然后与端口绑定(bind),对端口进行监听(lensten),调用accept阻塞,等待客户端连接.
	客户端:初始化一个socket,然后连接服务器(connect)
	如果连接成功,这时客户端和服务端的链接就建立了
	客户端发送数据请求,服务器端接收请求并处理请求,然后把回应数据发送给客户端,客户端毒鼠强数据
	最后关闭链接,一次交互结束


1. 服务端套接字函数
	s.bind() 绑定(主机,端口号)到套接字
	s.listen() 开始tcp监听
	s.accept() 被动接受tcp客户的链接,(阻塞式)等待连接的到来
2. 客户端套接字函数
	s.connect() 主动初始化tcp服务器的链接
	s.connect_ex()  connect()函数的扩展版本,出错时返回出错码,而不是抛出异常

3. 公共用途的套接字函数
	s.recv()            接收TCP数据
    s.send()            发送TCP数据(send在待发送数据量大于己端缓存区剩余空间时,数据丢失,不会发完)
    s.sendall()         发送完整的TCP数据(本质就是循环调用send,sendall在待发送数据量大于己端缓存区剩余空间时,数据不丢失,循环调用send直到发完)
    s.recvfrom()        接收UDP数据
    s.sendto()          发送UDP数据
    s.getpeername()     连接到当前套接字的远端的地址
    s.getsockname()     当前套接字的地址
    s.getsockopt()      返回指定套接字的参数
    s.setsockopt()      设置指定套接字的参数
    s.close()           关闭套接字
4. 面向锁的套接字方法
	s.setblocking()     设置套接字的阻塞与非阻塞模式
    s.settimeout()      设置阻塞套接字操作的超时时间
    s.gettimeout()      得到阻塞套接字操作的超时时间
5. 面向文件的套接字的函数
	s.fileno()          套接字的文件描述符
	s.makefile()        创建一个与该套接字相关的文件

## 基于TCP的套接字
	TCP是基于链接的,必须先启动服务端,然后在启动客户端去链接服务端
服务端
``` python
ss = socket() #创建服务器套接字
ss.bind()      #把地址绑定到套接字
ss.listen()      #监听链接
inf_loop:      #服务器无限循环
    cs = ss.accept() #接受客户端链接
    comm_loop:         #通讯循环
        cs.recv()/cs.send() #对话(接收与发送)
    cs.close()    #关闭客户端套接字
ss.close()        #关闭服务器套接字(可选)
```

客户端
``` python
cs = socket()    # 创建客户套接字
cs.connect()    # 尝试连接服务器
comm_loop:        # 通讯循环
    cs.send()/cs.recv()    # 对话(发送/接收)
cs.close()            # 关闭客户套接字
```
- 链接循环 和通信循环
服务端
``` python
#_*_coding:utf-8_*_
import socket
ip_port=('127.0.0.1',8081)#电话卡
BUFSIZE=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
s.bind(ip_port) #手机插卡
s.listen(5)     #手机待机


while True:                         #新增接收链接循环,可以不停的接电话
    conn,addr=s.accept()            #手机接电话
    # print(conn)
    # print(addr)
    print('接到来自%s的电话' %addr[0])
    while True:                         #新增通信循环,可以不断的通信,收发消息
        msg=conn.recv(BUFSIZE)             #听消息,听话

        # if len(msg) == 0:break        #如果不加,那么正在链接的客户端突然断开,recv便不再阻塞,死循环发生

        print(msg,type(msg))

        conn.send(msg.upper())       #发消息,说话

    conn.close()                    #挂电话

s.close()                  #手机关机
```

客户端
``` python
import socket
ip_port=('127.0.0.1',8081)
BUFSIZE=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect_ex(ip_port)           #拨电话

while True:                             #新增通信循环,客户端可以不断发收消息
    msg=input('>>: ').strip()
    if len(msg) == 0:continue
    s.send(msg.encode('utf-8'))         #发消息,说话(只能发送字节类型)

    feedback=s.recv(BUFSIZE)            #收消息,听话
    print(feedback.decode('utf-8'))

s.close()                        #挂电话
```

## 有时候会提示 Address already in use
1. 第一种方法
``` python
#加入一条socket配置，重用ip和端口

phone=socket(AF_INET,SOCK_STREAM)
phone.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #就是它，在bind前加
phone.bind(('127.0.0.1',8080))
```
2. 第二种方法 (time_wait状态在占用地址)
``` python
发现系统存在大量TIME_WAIT状态的连接，通过调整linux内核参数解决，
vi /etc/sysctl.conf

编辑文件，加入以下内容：
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_fin_timeout = 30
 
然后执行 /sbin/sysctl -p 让参数生效。
 
net.ipv4.tcp_syncookies = 1 表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭；

net.ipv4.tcp_tw_reuse = 1 表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭；

net.ipv4.tcp_tw_recycle = 1 表示开启TCP连接中TIME-WAIT sockets的快速回收，默认为0，表示关闭。

net.ipv4.tcp_fin_timeout 修改系統默认的 TIMEOUT 时间
```

## 基于UDP的套接字
	udp是无链接的,先启动哪一段都不会报错

udp服务端
``` Python
1 ss = socket()   #创建一个服务器的套接字
2 ss.bind()       #绑定服务器套接字
3 inf_loop:       #服务器无限循环
4     cs = ss.recvfrom()/ss.sendto() # 对话(接收与发送)
5 ss.close()                         # 关闭服务器套接字
```

udp客户端
``` python
cs = socket()   # 创建客户套接字
comm_loop:      # 通讯循环
    cs.sendto()/cs.recvfrom()   # 对话(发送/接收)
cs.close()                      # 关闭客户套接字
```



















