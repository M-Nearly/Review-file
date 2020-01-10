# 配置MariaDB数据库服务端远程访问

## 

## 开启远程访问权限

连接MariaDB数据库，执行以下命令开启远程访问。

```sql
grant all privileges on *.* to 'root'@'ip' identified by 'password';
flush privileges;
```

如果需要任意IP地址访问，就把IP地址换成`%`。



## 修改配置文件

在网络上能搜索到的资料都只说了第一点，然而亲测之后并没有用。因为MariaDB默认绑定了本地IP。
具体的文件存放位置和数据库的版本有关。我当时就找了一些时间才找到。
`/etc/mysql/my.cnf/mariadb.conf.d/50-server.cnf`
把`bind-address = 127.0.0.1`这一行注释掉。

## 重启MariaDB服务