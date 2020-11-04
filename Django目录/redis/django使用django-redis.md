### django-redis

- 不方便: 使用redis + 连接池
- 推荐: django-redis







- django-redis，在django中“方便的”使用redis。

  - 安装：`django-redis`

    ```
    pip3 install django-redis
    ```

  - 使用

    ```python
    # 配置文件 settings.py (建议local_settings.py)
    
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://10.211.55.28:6379", # 安装redis的主机的 IP 和 端口
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "CONNECTION_POOL_KWARGS": {  ## 连接池信息
                    "max_connections": 1000,
                    "encoding": 'utf-8'
                },
                "PASSWORD": "foobared" # redis密码
            }
        },
        "master": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://10.211.55.29:6379", # 安装redis的主机的 IP 和 端口
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "CONNECTION_POOL_KWARGS": {
                    "max_connections": 1000,
                    "encoding": 'utf-8'
                },
                "PASSWORD": "foobar999ed" # redis密码
            }
        }
    }
    ```

    ```python
    
    
    ##  使用
    from django.shortcuts import HttpResponse
    
    from django_redis import get_redis_connection
    
    def index(request):
        # 去连接池中获取一个连接
        conn = get_redis_connection("default") # 默认去default中  选择redis库
        
        conn.set('nickname', "武沛齐", ex=10)
        value = conn.get('nickname')
        print(value)
        return HttpResponse("OK")
    ```