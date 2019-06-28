django 链接现有数据库

python manage.py inspectdb --database="array" > arraydata/models.py


## settings.py 添加新增数据库
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'array': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meng',
        'HOST': '10.62.54.100',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'ATOMIC_REQUEST': True,
    }
}
```

## 执行 生成modules 文件
`python manage.py inspectdb --database="array" > arraydata/models.py`


## makemigrations  migrate
``` python
1. 因为数据库已经创建好,但是makemigrations modules 还是会提示create xxxx ,删除掉migrations 文件内的create 这段代码
2. `python manage.py migrate --database=array --fake` 
3. 在新增modules 类的时候 后面就是正常操作了
4. 执行mreate的时候,添加database 参数 
5. `python manage.py migrate --database=array`
```


数据导出

python manage.py dumpdata app1 --database=db1 > app1_fixture.json
python manage.py dumpdata app2 --database=db2 > app2_fixture.json
python manage.py dumpdata auth > auth_fixture.json
数据库导入

python manage.py loaddata app1_fixture.json --database=db1
python manage.py loaddata app2_fixture.json --database=db2