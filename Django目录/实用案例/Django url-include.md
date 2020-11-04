```
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
```



## 路由分发



```python
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("^app01/", include("app01.urls"), name="app"),
    re_path("^send/sms", apvi.send_sms)
]
```

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("^app01/", include("app01.urls",namespace="app01")), # "app01:register"
    re_path("^web/", include("web.urls",namespace="web")),
    re_path("^send/sms", apvi.send_sms)
]