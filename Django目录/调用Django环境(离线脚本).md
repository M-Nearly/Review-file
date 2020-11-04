## django离线脚本

### 离线脚本
离线

​	跟web是否运行没有任何关系. 非运行时
脚本
​	一个或几个py文件

在某个py文件中对django的项目做一些处理.

## 示例
1. 在脚本运行向django插入数据




```python
import os
import sys
if __name__ == '__main__':
    # 找到配置文件目录, 加到环境变量中
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)
    # 调用django的settings配置文件
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled15.settings")
    import django
    django.setup()

    from app01 import models

    books = models.Book.objects.all()
    print(books)
```

或者直接在当前目录下
`python manage.py shell`

```python
>>> import django
>>> django.setup()
```





### 为什么要使用离线脚本.

- 单次的 不常使用的
- 临时变化大的
- 需要手动执行的









