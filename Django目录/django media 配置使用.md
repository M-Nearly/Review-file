1.setting.py配置

```python
#用户文件上传至media
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
```

2.url.py配置

```python
#导入正则路径
from django.urls import re_path

from django.views.static import serve
from MyAPP.settings import MEDIA_ROOT

urlpatterns=[
    #添加media正则路径
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
]
```

3.templates文件配置

```html
    <img src="/media/{{路径}}">
```





4. 浏览器访问

    <http://127.0.0.1:8000/media/Python%20%E6%AD%A3%E5%88%99.png>

   可以直接放问图片.或者查看文件内容

