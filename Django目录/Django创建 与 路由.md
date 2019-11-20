# Django
## MVC 与 MTV 模型

- ## MVC
	​	web 服务器开发领域著名的mvc模式.
	​		模型 M    负责业务对象与数据库的映射(ORM)
	​		控制器 C  接受用户的输入调用模型和视图完成用户的请求
	​		视图 V    负责与用户的交互(页面)

- ## MTV
	​	Django的MTV模式本质上和MVC是一样的，也是为了各组件间保持松耦合关系，只是定义上有些许不同，
	​	Django的MTV分别是值
	​		M 代表模型（Model）  ：负责业务对象和数据库的关系映射(ORM)
	​		T 代表模板 (Template)：负责如何把页面展示给用户(html)
	​		V 代表视图（View）   ：负责业务逻辑，并在适当时候调用Model和Template



## django 下载 和 基本命令

- ### 下载django
	`pip install django==1.11.9 -i http://pypi.hustunique.org/simple`   
	指定版本号，指定国内镜像
	
- ### 创建django project 
	`django-admin.py startproject mysite`
- ### 创建app
	`Python manage.py startapp blog`
- ### 启动django项目
	`Python manage.py runserver 80001`


## django 静态文件的配置
在setting 中添加静态文件的目录,
``` python
​	STATIC_URL = '/static/'
​	STATICFILES_DIRS = [
​		os.path.join(BASE_DIR,'static')
​	]
```



## Django的路由控制 *<u>`Urls`</u>*
​	本质就是:URL与要为该URL调用的视图函数之间的映射表

- 简单的路由配置
``` python
from django.conf.urls import url

urlpatterns = [
	url(正则表达式, views视图函数，参数，别名),
]
	
正则表达式: 		  一个正则表达式的字符串
views视图函数: 	   一个可调用对象,通常为一个视图函数或一个指定视图函数路径的字符串
参数: 			可选的要传递给视图函数的默认参数(字典格式)
别名: 			一个可选的name 参数


from django.urls import path,re_path
from app01 import views
	
urlpatterns = [
    re_path(r'^articles/2003/$', views.special_case_2003),
    re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
    ]
    
若要从URL 中捕获一个值，只需要在它周围放置一对圆括号。

不需要添加一个前导的反斜杠，因为每个URL 都有。例如，应该是^articles 而不是 ^/articles。

每个正则表达式前面的'r' 是可选的但是建议加上。它告诉Python 这个字符串是“原始的” —— 字符串中任何字符都不应该转义

urlpatterns中的元素按照书写顺序从上往下逐一匹配正则表达式，一旦匹配成功则不再继续
```

## APPEND_SLASH  默认为true
​	# 是否开启URL访问地址后面不为/跳转至带有/的路径的配置项
​	APPEND_SLASH=True
``` python
例子:
from django.conf.urls import url
from app01 import views

urlpatterns = [
	url(r'^blog/$', views.blog),
]
	访问 http://www.example.com/blog 时，默认将网址自动转换为 http://www.example/com/blog/ 。
	
	如果在settings.py中设置了 APPEND_SLASH=False，此时我们再请求 http://www.example.com/blog 时就会提示找不到页面。
```


## 有名分组
​	Python 正则表达式中，命名正则表达式组的语法是(?P<name>pattern)，其中name 是组的名称，pattern 是要匹配的模式。
`re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),`

```django
 path('<int:question_id>/', views.detail, name='detail'),
```

## 路由分发
``` python
from django.conf.urls import url,include
from django.urls import path,re_path,include
	
#主urls
from django.urls import path,re_path,include
from app01 import views
from app01 import urls
urlpatterns = [ 
	　　# re_path(r'^app01/',include('app01.urls')),#行
	　　# re_path(r'^app01/&',include('app01.urls')),#不行
	　　# path('app01/',include('app01.urls')),#行　
	　　#path('app01/', include(urls)),
	]
	
#分发url
from django.urls import path,re_path
from app01 import views
urlpatterns = [
	    re_path(r'^test/(?P<year>[0-9]{2})/$',views.url_test),
	]
```

## 反向解析
1. 在html代码里{% url "别名" 参数  参数%}
2. 在视图函数中：
	`from django.shortcuts import render, HttpResponse,redirect,reverse`
2.1 `url=reverse('test')`
2.2 `url=reverse('test',args=(10,20))`

	当命名你的URL 模式时，请确保使用的名称不会与其它应用中名称冲突。
	如果你的URL 模式叫做comment，而另外一个应用中也有一个同样的名称，当你在模板中使用这个名称的时候不能保证将插入哪个URL。在URL 名称中加上一个前缀，比如应用的名称，将减少冲突的可能。我们建议使用myapp-comment 而不是comment。


## 命名空间
- 在总urls.py在路由分发时，指定名称空间
``` python

path('app01/', include(('app01.urls','app01'))),
path('app02/', include(('app02.urls','app02')))
	
url(r'app01/',include('app01.urls',namespace='app01')),
url(r'app02/',include('app02.urls',namespace='app02'))
	 
url(r'app01/',include(('app01.urls','app01'))),
url(r'app02/',include(('app02.urls','app02')))


在视图函数反向解析的时候，指定是那个名称空间下的
	
url=reverse('app02:index')
print(url)

url2=reverse('app01:index')
print(url2)

在模版里：
<a href="{% url 'app02:index'%}">哈哈</a>

```


- include 用法 
``` python
from django.contrib import admin
from django.urls import path,include,re_path
# from app01 import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^app01/', include(('app01.urls','app01'),namespace='app01')),
    re_path('^app02', include(('app02.urls','app02'),namespace='app02')),

]
```
django2.0版的path  待完成





