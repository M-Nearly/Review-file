[toc]



----

# django

## JWT实现用户认证 (Json Web Token)

```txt



```





解决XSS和XSRF问题)

解决跨域问题 

 - 使用nginx反向代理



****

## 常用的模块



salstack

paramiko

time / datetime os sys json&pickle configparser hashlib subprocess  logging re 

re

``` python 


	django
https://www.cnblogs.com/liuqingzheng/p/9506212.html
    re
https://www.cnblogs.com/linhaifeng/articles/6384466.html#_label13
```



## wsgi 协议

gunicorn

bjoern

----

## Django 路由

```python
from django.urls import path,re_path
import views
```

###有名分组

`re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),`

命名正则表达式组的语法是**`(?P<name>pattern)`**，其中`name` 是组的名称，`pattern` 是要匹配的模式

###  路由分发

`from django.conf.urls import url,include`

``

### 反向解析

``` python
# 在视图函数中使用

url=reverse('test')
url=reverse('test',args=(10,20))
```



### 名称空间

``` python

 url(r'app01/',include('app01.urls',namespace='app01')),
 url(r'app02/',include('app02.urls',namespace='app02'))

在视图函数反向解析的时候，指定是那个名称空间下的
 url=reverse('app02:index')
 print(url)
 url2=reverse('app01:index')
 print(url2)

在模版里：
<a href="{% url 'app02:index'%}">哈哈</a>
```











----

## django 视图

### 常用HttpResponse响应对象的几种形式

```python
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, JsonResponse

from django.urls import reverse # 反向解析
```

### CBV 和 FBV

**CBV基于类的视图(Class base view)和FBV基于函数的视图（Function base view）**

```python
from django.views import View
class AddPublish(View):
    def dispatch(self, request, *args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
        # 可以写类似装饰器的东西，在前后加代码
        obj=super().dispatch(request, *args, **kwargs)
        return obj

    def get(self,request):
        return render(request,'index.html')
    def post(self,request):
        request
        return HttpResponse('post')
```





----

## Django models

### 表查询

一对一 OneToOneField

一对多 ForeignKey 放在多的

​	先找一个表的对象, 然后拿着对象 去别的表联合去查,分两步.

​	基于对象跨表查询 (正向字段名. 反向表名_set) 

​	

​	直接一条查询语句写在一起

​	基于双下划线跨表查询 (正向查询按字段,反向查询按表名小写__字段名)

​		

多对多 ManyToManyField (放在哪里都也一样)

​	基于对象 (正向字段名. 反向表名_set)

​	基于双下划线(正向查询按字段,反向查询按表名小写用来告诉ORM引擎join哪张表)



如果指定related_name, 反向查询的时候直接related_name__ ,则用related_name替换表名

聚合 和 分组查询

```python
from django.db.models import Avg, Max, Sum, Min, Max, Count, F, Q

```



### ORM 的字段和参数

https://www.cnblogs.com/liuqingzheng/articles/9627915.html

多对多创建三张表 三种方式

1. 自行创建第三张表并通过外键相关联

2. 通过 manyToManyField 自动创建第三张表

3. 设置ManyTomanyField并指定自行创建的第三张表

注意:

​	我们需要在第三张关系表中存储额外的字段时，就要使用第三种方式



### 查询优化 - 减少SQL查询的数量

**select_related** 和 普通查询

​	链式操作(.)

select_related         主要针一对一和多对一关系进行优化

prefetch_related()  对于多对多字段（ManyToManyField）和一对多字段



### extra 表达复杂的 `WHERE` 子句

除非万不得已,尽量避免这样做

```python
extra(select=None, where=None, params=None, 
      tables=None, order_by=None, select_params=None)
```

https://www.cnblogs.com/liuqingzheng/articles/9805991.html



### 使用原生 sql

``` python
from django.db import connection, connections

cursor = connection.cursor() # connection=default数据
cursor = connections['db2'].cursor()

cursor.execute("""SELECT * from auth_user where id = %s""", [1])

row = cursor.fetchone()
row = cursor.fetchall()
```



``` python
ret=models.Author.objects.raw('select * from app01_author where nid>1')
    print(ret)
    for i in ret:
        print(i)
    print(ret.query)
    # 会把book的字段放到author对象中
    ret=models.Author.objects.raw('select * from app01_book where nid>1')
    print(ret)
    for i in ret:
        print(i.price)
        print(type(i))

```





### 整体插入 bulk_create()

```python
Entry.objects.bulk_create([
    Entry(headline="Python 3.0 Released"),
    Entry(headline="Python 3.1 Planned")
])
```





### 事务操作

```python
# 事务操作
    from django.db import transaction
    with transaction.atomic():
```



### defer 和 only

defer('id','name'):取出对象，字段除了id和name都有
only('id','name'):取的对象，只有id和name
如果点，依然能点出其它列，但是不要点了，因为取没有的列，会再次查询数据库

```python
    ret=models.Author.objects.only('nid')
    for i in ret:
        # 查询不在的字段，会再次查询数据库，造成数据库压力大
        print(i.name)
```



----

## Django form 组件

`form.cleaned_data`

```python
from django import forms
from django.forms import widgets
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
class UserForm(forms.Form):
  pass
```

https://www.cnblogs.com/liuqingzheng/articles/9509775.html

1. 校验字段功能

2. 渲染标签功能

3. 渲染错误信息功能

4. 组件的参数配置

   ```python
   class Ret(Form):
       name = forms.CharField(max_length=10, min_length=2, label='用户名',
                              error_messages={'required': '该字段不能为空', 'invalid': '格式错误', 'max_length': '太长',
                                              'min_length': '太短'},
                              widget=widgets.TextInput(attrs={'class':'form-control'}))
       pwd = forms.CharField(max_length=10, min_length=2, widget=widgets.PasswordInput(attrs={'class':'form-control'}))
       email = forms.EmailField(label='邮箱', error_messages={'required': '该字段不能为空', 'invalid': '格式错误'})
   ```

5. 局部钩子

   ```python
   from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
   def clean_name(self):
   
           val=self.cleaned_data.get("name")
   
           ret=UserInfo.objects.filter(name=val)
   
           if not ret:
               return val
           else:
               raise ValidationError("该用户已注册!")
   ```

6. 全局钩子

   ```python
       def clean(self):
           pwd=self.cleaned_data.get('pwd')
           r_pwd=self.cleaned_data.get('r_pwd')
   
           if pwd and r_pwd:
               if pwd==r_pwd:
                   return self.cleaned_data
               else:
                   raise ValidationError('两次密码不一致')
           else:
   
               return self.cleaned_data
   ```



----

## Cookie 和 Session

https://www.cnblogs.com/liuqingzheng/articles/9509779.html

http 无状态

###cookie

django 中操作 Cookie

- 获取

  ```python
  request.COOKIES['key']
  request.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)
  
  # 参数：
  default: 默认值 
  salt: 加密盐
  max_age: 后台控制过期时间
  
  ```

- 设置

  ```python
  rep = HttpResponse(...)
  rep ＝ render(request, ...)
  
  rep.set_cookie(key,value)
  rep.set_signed_cookie(key,value,salt='加密盐')
  
  ```

- 删除 cookie

  ```python
  def logout(request):
      rep = redirect("/login/")
      rep.delete_cookie("user")  # 删除用户浏览器上之前设置的usercookie值
      return rep
  ```

- 



### Session

Cookie虽然在一定程度上解决了“保持状态”的需求，但是由于Cookie本身最大支持4096字节，以及Cookie本身保存在客户端，可能被拦截或窃取，因此就需要有一种新的东西，它能支持更多的字节，并且他保存在服务器，有较高的安全性

Django session 相关用法

``` python
# 获取、设置、删除Session中数据
request.session['k1']
request.session.get('k1',None)
request.session['k1'] = 123
request.session.setdefault('k1',123) # 存在则不设置
del request.session['k1']


# 所有 键、值、键值对
request.session.keys()
request.session.values()
request.session.items()
request.session.iterkeys()
request.session.itervalues()
request.session.iteritems()

# 会话session的key
request.session.session_key

# 将所有Session失效日期小于当前日期的数据删除
request.session.clear_expired()

# 检查会话session的key在数据库中是否存在
request.session.exists("session_key")

# 删除当前会话的所有Session数据(只删数据库)
request.session.delete()
　　
# 删除当前的会话数据并删除会话的Cookie（数据库和cookie都删）。
request.session.flush() 
    这用于确保前面的会话数据不可以再次被用户的浏览器访问
    例如，django.contrib.auth.logout() 函数中就会调用它。

# 设置会话Session和Cookie的超时时间
request.session.set_expiry(value)
    * 如果value是个整数，session会在些秒数后失效。
    * 如果value是个datatime或timedelta，session就会在这个时间后失效。
    * 如果value是0,用户关闭浏览器session就会失效。
    * 如果value是None,session会依赖全局session失效策略。
```

Django中使用session时，做的事：

```
# 生成随机字符串
# 写浏览器cookie -> session_id: 随机字符串
# 写到服务端session：
    # {
    #     "随机字符串": {'user':'alex'}
    # }
```

Django 中 session 配置

``` python
1. 数据库Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）

2. 缓存Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置

3. 文件Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
SESSION_FILE_PATH = None                                    # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir() 

4. 缓存+数据库
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'        # 引擎

5. 加密Cookie Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'   # 引擎

其他公用设置项：
SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
```



## 中间件组件

https://www.cnblogs.com/liuqingzheng/articles/9509739.html

![img](data:image/png;base64,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)

## django Auth 模块 (自带用户认证模块)

https://www.cnblogs.com/liuqingzheng/articles/9628105.html

```python
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# 扩展用户表使用的
from django.contrib.auth.models import AbstractUser
```

提供的方法:

1. authenticate()
2. login()
3. logout()
4. is_authenticated 是否通过认证
5. login_required()  装饰器
6. Create_user()
7. create_superuser()
8. check_password(password)
9. set_password(password) # 一定要调用 user.save()方法



user 对象属性

1. is_staff: 是否拥有网站管理权
2. is_active 是否允许用户登录, 

扩展默认的auth_user表

​	继承内置的 AbstractUser 类，来定义一个自己的Model类。

----

## ContentType 组件

https://www.cnblogs.com/liuqingzheng/articles/9800526.html



## **Rest Framework**

https://www.cnblogs.com/liuqingzheng/p/9506212.html



### Restful 规范

架构风格 --> 表征状态转移

API 设计

1. api 与 用户通信协议 https

2. 域名

   - https://api.example.com             尽量将API部署在专用域名（会存在跨域问题）
   - https://example.org/api/            API很简单

3. 版本

   - URL，如：https://api.example.com/v1/
   - 请求头                         跨域时，引发发送多次请求

4. 路径 视网络上任何东西都是资源, 均使用名词表示(可复数)

   - https://api.example.com/v1/zoos
   - https://api.example.com/v1/animals
   - https://api.example.com/v1/employees

5. method 

   - GET   ：从服务器取出资源（一项或多项）
   - POST  ：在服务器新建一个资源
   - PUT   ：在服务器更新资源（客户端提供改变后的完整资源）
   - PATCH ：在服务器更新资源（客户端提供改变的属性）
   - DELETE ：从服务器删除资源

6. 过滤 通过在 url 上传参数的形式传递搜索条件

   - https://api.example.com/v1/zoos?limit=10：指定返回记录的数量
   - https://api.example.com/v1/zoos?offset=10：指定返回记录的开始位置
   - https://api.example.com/v1/zoos?page=2&per_page=100：指定第几页，以及每页的记录数
   - https://api.example.com/v1/zoos?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序
   - https://api.example.com/v1/zoos?animal_type_id=1：指定筛选条件

7. 状态码

   ```http
   200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。
   201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
   202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
   204 NO CONTENT - [DELETE]：用户删除数据成功。
   400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
   401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
   403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
   404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
   406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
   410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
   422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
   500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。
   
   更多看这里：http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
   ```

8. 错误处理

   ```json
   {
     ``error: ``"Invalid API key"
   }
   ```

9. 返回结果, 针对不同的操作,服务器向用户返回的结果应该符合以下规范。

   ```json
   GET ``/``collection：返回资源对象的列表（数组）
   GET ``/``collection``/``resource：返回单个资源对象
   POST ``/``collection：返回新生成的资源对象
   PUT ``/``collection``/``resource：返回完整的资源对象
   PATCH ``/``collection``/``resource：返回完整的资源对象
   DELETE ``/``collection``/``resource：返回一个空文档
   ```

10. Hypermedia API，RESTful API最好做到Hypermedia，即返回结果中提供链接，连向其他API方法，使得用户不查文档，也知道下一步应该做什么。

    ```json
    {``"link"``: {
     ``"rel"``:  ``"collection https://www.example.com/zoos"``,
     ``"href"``: ``"https://api.example.com/zoos"``,
     ``"title"``: ``"List of zoos"``,
     ``"type"``: ``"application/vnd.yourformat+json"
    }}
    ```



Django 实现

​	JsonResponse / HttpResponse 构建Json 返回内容

``` python
urlpatterns = [
    url(r'^users/$', views.Users.as_view()),
    url(r'^users2/$', views.user2),

]
```



``` python
import json

def  user2(request):
    if request.method=='GET':
        dic = {'status':200,'name': 'lqz2', 'age': 18}
        return HttpResponse(json.dumps(dic))
    elif request.method=='POST':
        dic = {'status': 200, 'msg': '修改成功'}
        return JsonResponse(dic)

class Users(View):
    def get(self, request):
        dic = {'status':200,'name': 'lqz', 'age': 18}
        return HttpResponse(json.dumps(dic))

    def post(self, request):
        dic = {'status': 200, 'msg': '修改成功'}
        return JsonResponse(dic)
```



### APIview

cnblogs.com/liuqingzheng/articles/9766374.html

安装 djangorestframework



### 序列化组件

serializers

ModelSerializers



### 视图组件

```
as_view
```











****



##  前后端混合开发之layui

```python
https://www.layui.com/doc/element/layout.html#adminhttps://www.layui.com/doc/element/layout.html#admin
```

## 前后端混合开发之xadmin

### 

## 前后端分离之vue-admin

```python
# 介绍地址
https://panjiachen.github.io/vue-element-admin-site/zh/guide/
  
# 集成版本（高级版本）
https://github.com/PanJiaChen/vue-element-admin
# 演示地址
https://github.com/PanJiaChen/vue-element-admin/blob/master/README.zh-CN.md
  
# 基础版本
https://github.com/PanJiaChen/vue-admin-template
  
# 桌面版
https://github.com/PanJiaChen/electron-vue-admin
```

## 图表展示

### Highchars

### echars (百度)



##Linux

###  Tcp三次握手四次挥手

###  基于Tcp的socket套接字

