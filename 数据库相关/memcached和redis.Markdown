# Memcached  对比 redis 

1. 由于Redis只使用单核，而Memcached可以使用多核,但是存储小数据的时候,redis的性能更高,而100k以上的数据,Memcached的性能更高.

2. 内存的使用率来说,使用简单的key-value,Memcached的内存利用率更高,而如果redis采用hash结构来存储key-value,redis的内存利用率更高.

3. 如果你对数据的持久化和数据同步有所要求的,那么推荐你选择reds,因为这两个特性,Memcached 都不具备.及时你只希望在升级或者重启系统后缓存数据不会丢失,选择redis

4. Memcached 只支持 "字符串的数据结构" ,redis 支持五大数据结构,

----
# Memcached 
> 通过在内存中缓存数据和对象来减少读取数据库的次数.

### 安装:
``` shell
	wget http://memcached.org/latest
	tar -zxvf memcached-1.x.x.tar.gz
	cd memcached-1.x.x
	./configure && make && make test && sudo make install
	 
	PS：依赖libevent
	       yum install libevent-devel
	       apt-get install libevent-dev
```

### 启动Memcached:

> memcached -d -m 10    -u root -l 10.211.55.4 -p 12000 -c 256 -P /tmp/memcached.pid

- 参数说明:
    -d 是启动一个守护进程
    -m 是分配给Memcache使用的内存数量，单位是MB
    -u 是运行Memcache的用户
    -l 是监听的服务器IP地址
    -p 是设置Memcache监听的端口,最好是1024以上的端口
    -c 选项是最大运行的并发连接数，默认是1024，按照你服务器的负载量来设定
    -P 是设置保存Memcache的pid文件

### Memcached命令:

> 存储命令: set/add/replace/append/prepend/cas
> 获取命令: get/gets
> 其他命令: delete/stats..

----
## Python操作Memcached.
### 安装api
> python操作Memcached使用Python-memcached模块
>   下载安装：https://pypi.python.org/pypi/python-memcached
>
> ####  1. 第一次操作
``` python
import memcache
 
mc = memcache.Client(['10.211.55.4:12000'], debug=True)
mc.set("foo", "bar")
ret = mc.get('foo')
print ret

Ps：debug = True 表示运行出现错误时，现实错误信息，上线后移除该参数。
```
#### 天生支持集群
