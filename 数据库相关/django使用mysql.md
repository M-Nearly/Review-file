```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lqz',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'ATOMIC_REQUEST': True,
        'OPTIONS': {
            "init_command": "SET storage_engine=MyISAM",
        }
    }
}
'''
'NAME':要连接的数据库，连接前需要创建好
'USER':连接数据库的用户名
'PASSWORD':连接数据库的密码
'HOST':连接主机，默认本机
'PORT':端口 默认3306
'ATOMIC_REQUEST': True,
设置为True统一个http请求对应的所有sql都放在一个事务中执行（要么所有都成功，要么所有都失败）。
是全局性的配置， 如果要对某个http请求放水（然后自定义事务），可以用non_atomic_requests修饰器 
'OPTIONS': {
             "init_command": "SET storage_engine=MyISAM",
            }
设置创建表的存储引擎为MyISAM，INNODB
'''

```

- 如果提示 `django.db.utils.InternalError: (1193, u"Unknown system variable 'storage_engine'")`

修改
``` python
        'OPTIONS': {
            "init_command": "SET default_storage_engine=INNODB",
        }
```


