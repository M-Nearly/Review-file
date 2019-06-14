``` python
1.python3 manage.py makemigrations --empty 你的应用名
2.python3 manage.py makemigrations
3.python3 manage.py migrate

```



## Django根据现有数据库,自动生成models模型文件

创建一个项目，修改seting文件，在setting里面设置你要连接的数据库类型和连接名称，地址之类，和创建新项目的时候一致 
运行下面代码可以自动生成models模型文件 
Python manage.py inspectdb 
这样就可以在控制台的命令行中看到数据库的模型文件了

把模型文件导入到app中 
创建一个app 
django-admin.py startapp app 
python manage.py inspectdb > app/models.py ok模型文件已经生成好了。下面的工作就和之前一样了