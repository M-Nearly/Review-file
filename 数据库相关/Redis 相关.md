# Redis
redis是一个key-value存储系统。
支持存储的value类型相对更多，包括string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）
redis支持各种不同方式的排序
数据都是缓存在内存中
redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。

## 1. 使用Redis有哪些好处？

(1) 速度快，因为数据存在内存中，类似于HashMap，HashMap的优势就是查找和操作的时间复杂度都是O(1)

(2) 支持丰富数据类型，支持string，list，set，sorted set，hash

(3) 支持事务，操作都是原子性，所谓的原子性就是对数据的更改要么全部执行，要么全部不执行

(4) 丰富的特性：可用于缓存，消息，按key设置过期时间，过期后将会自动删除

## 2. redis相比memcached有哪些优势？

(1) memcached所有的值均是简单的字符串，redis作为其替代者，支持更为丰富的数据类型

(2) redis的速度比memcached快很多

(3) redis可以持久化其数据

## 3. redis常见性能问题和解决方案：

(1) Master最好不要做任何持久化工作，如RDB内存快照和AOF日志文件

(2) 如果数据比较重要，某个Slave开启AOF备份数据，策略设置为每秒同步一次

(3) 为了主从复制的速度和连接的稳定性，Master和Slave最好在同一个局域网内

(4) 尽量避免在压力很大的主库上增加从库

(5) 主从复制不要用图状结构，用单向链表结构更为稳定，即：Master <- Slave1 <- Slave2 <- Slave3...

这样的结构方便解决单点故障问题，实现Slave对Master的替换。如果Master挂了，可以立刻启用Slave1做Master，其他不变。

## 4. MySQL里有2000w数据，redis中只存20w的数据，如何保证redis中的数据都是热点数据

相关知识：redis 内存数据集大小上升到一定大小的时候，就会施行数据淘汰策略。redis 提供 6种数据淘汰策略：

- voltile-lru：从已设置过期时间的数据集（server.db[i].expires）中挑选最近最少使用的数据淘汰
- volatile-ttl：从已设置过期时间的数据集（server.db[i].expires）中挑选将要过期的数据淘汰
- volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意选择数据淘汰
- allkeys-lru：从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰
- allkeys-random：从数据集（server.db[i].dict）中任意选择数据淘汰
- no-enviction（驱逐）：禁止驱逐数据

## 5. Memcache与Redis的区别都有哪些？

1)、存储方式
Memecache把数据全部存在内存之中，断电后会挂掉，数据不能超过内存大小。
Redis有部份存在硬盘上，这样能保证数据的持久性。

2)、数据支持类型
Memcache对数据类型支持相对简单。
Redis有复杂的数据类型。

3），value大小
redis最大可以达到1GB，而memcache只有1MB

## redis 最适合的场景


Redis最适合所有数据in-momory的场景，虽然Redis也提供持久化功能，但实际更多的是一个disk-backed的功能，跟传统意义上的持久化有比较大的差别，那么可能大家就会有疑问，似乎Redis更像一个加强版的Memcached，那么何时使用Memcached,何时使用Redis呢?

如果简单地比较Redis与Memcached的区别，大多数都会得到以下观点：

1 、Redis不仅仅支持简单的k/v类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
2 、Redis支持数据的备份，即master-slave模式的数据备份。
3 、Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用。

（1）、会话缓存（Session Cache）

最常用的一种使用Redis的情景是会话缓存（session cache）。用Redis缓存会话比其他存储（如Memcached）的优势在于：Redis提供持久化。当维护一个不是严格要求一致性的缓存时，如果用户的购物车信息全部丢失，大部分人都会不高兴的，现在，他们还会这样吗？

幸运的是，随着 Redis 这些年的改进，很容易找到怎么恰当的使用Redis来缓存会话的文档。甚至广为人知的商业平台Magento也提供Redis的插件。

（2）、全页缓存（FPC）

除基本的会话token之外，Redis还提供很简便的FPC平台。回到一致性问题，即使重启了Redis实例，因为有磁盘的持久化，用户也不会看到页面加载速度的下降，这是一个极大改进，类似PHP本地FPC。

再次以Magento为例，Magento提供一个插件来使用Redis作为全页缓存后端。
此外，对WordPress的用户来说，Pantheon有一个非常好的插件  wp-redis，这个插件能帮助你以最快速度加载你曾浏览过的页面。

（3）、队列

Reids在内存存储引擎领域的一大优点是提供 list 和 set 操作，这使得Redis能作为一个很好的消息队列平台来使用。Redis作为队列使用的操作，就类似于本地程序语言（如Python）对 list 的 push/pop 操作。

如果你快速的在Google中搜索“Redis queues”，你马上就能找到大量的开源项目，这些项目的目的就是利用Redis创建非常好的后端工具，以满足各种队列需求。例如，Celery有一个后台就是使用Redis作为broker，你可以从这里去查看。

（4），排行榜/计数器

Redis在内存中对数字进行递增或递减的操作实现的非常好。集合（Set）和有序集合（Sorted Set）也使得我们在执行这些操作的时候变的非常简单，Redis只是正好提供了这两种数据结构。所以，我们要从排序集合中获取到排名最靠前的10个用户–我们称之为“user_scores”，我们只需要像下面一样执行即可：

当然，这是假定你是根据你用户的分数做递增的排序。如果你想返回用户及用户的分数，你需要这样执行：

ZRANGE user_scores 0 10 WITHSCORES
Agora Games就是一个很好的例子，用Ruby实现的，它的排行榜就是使用Redis来存储数据的，你可以在这里看到。

（5）、发布/订阅

最后（但肯定不是最不重要的）是Redis的发布/订阅功能。发布/订阅的使用场景确实非常多。我已看见人们在社交网络连接中使用，还可作为基于发布/订阅的脚本触发器，甚至用Redis的发布/订阅功能来建立聊天系统！（不，这是真的，你可以去核实）。

Redis提供的所有特性中，我感觉这个是喜欢的人最少的一个，虽然它为用户提供如果此多功能。


## 一、Redis安装和基本使用
``` shell
wget http://download.redis.io/releases/redis-3.0.6.tar.gz
tar xzf redis-3.0.6.tar.gz
cd redis-3.0.6
make
```
### 启动服务端
`src/redis-server`
### 启动客户端
``` shell
src/redis-cli
redis> set foo bar
OK
redis> get foo
"bar"
```
## 二、Python操作Redis
```
sudo pip install redis
or
sudo easy_install redis
or
源码安装
详见：https://github.com/WoLpH/redis-py
```
## API 使用
redis-py 的API的使用可以分类为：
- 连接方式
- 连接池
- 操作
	- String 操作
	- Hash 操作
	- List 操作
	- Set 操作
	- Sort Set 操作
- 管道
- 发布订阅

### 1. 操作模式
redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py。
``` python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import redis
 
r = redis.Redis(host='10.211.55.4', port=6379)
r.set('foo', 'Bar')
print r.get('foo')
```
### 2、连接池
redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。
``` python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import redis
 
pool = redis.ConnectionPool(host='10.211.55.4', port=6379)
 
r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar')
print r.get('foo')
```
### 3、操作
#### String操作
- redis中的String在在内存中按照一个name对应一个value来存储

##### set(name, value, ex=None, px=None, nx=False, xx=False)  ***
在Redis中设置值，默认，不存在则创建，存在则修改
参数：
​     ex，过期时间（秒）
​     px，过期时间（毫秒）
​     nx，如果设置为True，则只有name不存在时，当前set操作才执行
​     xx，如果设置为True，则只有name存在时，岗前set操作才执行

##### setnx(name, value)
- 设置值，只有name不存在时，执行设置操作（添加）

##### setex(name, value, time)
```
# 设置值
# 参数：
    # time，过期时间（数字秒 或 timedelta对象）
```
##### psetex(name, time_ms, value)
设置值
参数:
​	 time_ms，过期时间（数字毫秒 或 timedelta对象）
##### mset(*args, **kwargs)  ***
批量设置值
```
    mset(k1='v1', k2='v2')
    或
    mget({'k1': 'v1', 'k2': 'v2'})
```

##### get(name)
- 获取值

##### mget(keys, *args)
- 批量获取
```
    mget('ylr', 'wupeiqi')
    或
    r.mget(['ylr', 'wupeiqi'])
```
##### getset(name,value)
- 设置新值并获取原来的值

##### getrange(key, start, end)
- 获取子序列(根据字节获取,非字符)
- 参数:
	- name，Redis 的 name
    - start，起始位置（字节）
    - end，结束位置（字节）
    - 如 : "武沛齐" ，0-3表示 "武"
##### setrange(name, offset, value)
- 修改字符串内容,从指定字符串索引开始向后替换(新值太长时,则向后添加)
- 参数:
	- offset，字符串的索引，字节（一个汉字三个字节）
	- value，要设置的值
##### setbit(name, offset, value)
- 对name对应值的二进制表示的位进行操作
- 参数
	- name  redis的name
	- offset, 位的索引(将值变换成二进制后再进行索引)
	- value, 值只能是1或0
- 注 :如果在redis中有一个对应:n1 = "foo"
    那么字符串foo的二进制表示为：01100110 01101111 01101111
    所以，如果执行 setbit('n1', 7, 1)，则就会将第7位设置为1，
    那么最终二进制则变成 01100111 01101111 01101111，即："goo"
- 扩展,转换二进制表示:
- 






















