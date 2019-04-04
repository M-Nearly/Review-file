# ORM 简介

ORM是“对象-关系-映射”的简称。
> 实现了数据模型与数据库的解耦，即数据模型的设计不需要依赖于特定的数据库，通过简单的配置就可以轻松更换数据库，这极大的减轻了开发人员的工作量，不需要面对因数据库变更而导致的无效劳动

# 单表操作
### 创建模型 - 创建表
``` python
from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    pub_data = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.CharField(max_length=12)
    def __str__(self):
        return self.name
```
### 更多的字段和参数
#### 字段
``` python
AutoField(Field)
        - int自增列，必须填入参数 primary_key=True
SmallIntegerField(IntegerField):
        - 小整数 -32768 ～ 32767
PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
        - 正小整数 0 ～ 32767        - 
IntegerField(Field)
        - 整数列(有符号的) -2147483648 ～ 2147483647
PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
        - 正整数 0 ～ 2147483647
BigIntegerField(IntegerField):
        - 长整型(有符号的) -9223372036854775808 ～ 9223372036854775807

自定义无符号整数字段
class UnsignedIntegerField(models.IntegerField):
	def db_type(self, connection):
		return 'integer UNSIGNED'

BooleanField(Field)
        - 布尔值类型
NullBooleanField(Field):
        - 可以为空的布尔值
CharField(Field)
        - 字符类型
        - 必须提供max_length参数， max_length表示字符长度
TextField(Field)
        - 文本类型
EmailField(CharField)：
        - 字符串类型，Django Admin以及ModelForm中提供验证机制
IPAddressField(Field)
        - 字符串类型，Django Admin以及ModelForm中提供验证 IPV4 机制
URLField(CharField)
        - 字符串类型，Django Admin以及ModelForm中提供验证 URL
SlugField(CharField)
        - 字符串类型，Django Admin以及ModelForm中提供验证支持 字母、数字、下划线、连接符（减号）
FilePathField(Field)
        - 字符串，Django Admin以及ModelForm中提供读取文件夹下文件的功能
        - 参数：
                path,                      文件夹路径
                match=None,                正则匹配
                recursive=False,           递归下面的文件夹
                allow_files=True,          允许文件
                allow_folders=False,       允许文件夹

FileField(Field)
        - 字符串，路径保存在数据库，文件上传到指定目录
        - 参数：
            upload_to = ""      上传文件的保存路径
            storage = None      存储组件，默认	  django.core.files.storage.FileSystemStorage

ImageField(FileField)
        - 字符串，路径保存在数据库，文件上传到指定目录
        - 参数：
            upload_to = ""      上传文件的保存路径
            storage = None      存储组件，默认django.core.files.storage.FileSystemStorage
            width_field=None,   上传图片的高度保存的数据库字段名（字符串）
            height_field=None   上传图片的宽度保存的数据库字段名（字符串）

DateTimeField(DateField)
        - 日期+时间格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]

DateField(DateTimeCheckMixin, Field)
        - 日期格式      YYYY-MM-DD

TimeField(DateTimeCheckMixin, Field)
        - 时间格式      HH:MM[:ss[.uuuuuu]]

DurationField(Field)
        - 长整数，时间间隔，数据库中按照bigint存储，ORM中获取的值为datetime.timedelta类型

FloatField(Field)
        - 浮点型

DecimalField(Field)
        - 10进制小数
        - 参数：
            max_digits，小数总长度
            decimal_places，小数位长度

BinaryField(Field)
        - 二进制类型
```
#### 参数
``` python
(1)null
 
如果为True，Django 将用NULL 来在数据库中存储空值。 默认值是 False.
 
(1)blank
 
如果为True，该字段允许不填。默认为False。
要注意，这与 null 不同。null纯粹是数据库范畴的，而 blank 是数据验证范畴的。
如果一个字段的blank=True，表单的验证将允许该字段是空值。如果字段的blank=False，该字段就是必填的。
 
(2)default
 
字段的默认值。可以是一个值或者可调用对象。如果可调用 ，每有新对象被创建它都会被调用。
 
(3)primary_key
 
如果为True，那么这个字段就是模型的主键。如果你没有指定任何一个字段的primary_key=True，
Django 就会自动添加一个IntegerField字段做为主键，所以除非你想覆盖默认的主键行为，
否则没必要设置任何一个字段的primary_key=True。
 
(4)unique
 
如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的
 
(5)choices
由二元组组成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，<br>而且这个选择框的选项就是choices 中的选项。

DateField和DateTimeField
auto_now_add
配置auto_now_add=True，创建数据记录的时候会把当前时间添加到数据库。

auto_now
配置上auto_now=True，每次更新数据记录的时候会更新该字段。

    verbose_name        Admin中显示的字段名称
    blank               Admin中是否允许用户输入为空
    editable            Admin中是否可以编辑
    help_text           Admin中该字段的提示信息
    choices             Admin中显示选择框的内容，用不变动的数据放在内存中从而避免跨表操作
                        如：gf = models.IntegerField(choices=[(0, '何穗'),(1, '大表姐'),],default=1)

    error_messages      自定义错误信息（字典类型），从而定制想要显示的错误信息；
                        字典健：null, blank, invalid, invalid_choice, unique, and unique_for_date
                        如：{'null': "不能为空.", 'invalid': '格式错误'}

    validators          自定义错误验证（列表类型），从而定制想要的验证规则
                        from django.core.validators import RegexValidator
                        from django.core.validators import EmailValidator,URLValidator,DecimalValidator,\
                        MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator
                        如：
                            test = models.CharField(
                                max_length=32,
                                error_messages={
                                    'c1': '优先错信息1',
                                    'c2': '优先错信息2',
                                    'c3': '优先错信息3',
                                },
                                validators=[
                                    RegexValidator(regex='root_\d+', message='错误了', code='c1'),
                                    RegexValidator(regex='root_112233\d+', message='又错误了', code='c2'),
                                    EmailValidator(message='又错误了', code='c3'), ]
                            )
```
#### 元信息
ORM对应的类里面包含另一个Meta类,而Meta类封装了一些数据库的信息,主要的字段如下:
``` python
 class UserInfo(models.Model):
        nid = models.AutoField(primary_key=True)
        username = models.CharField(max_length=32)
        class Meta:
            # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
            db_table = "table_name"

            # 联合索引
            index_together = [
                ("pub_date", "deadline"),
            ]

            # 联合唯一索引
            unique_together = (("driver", "restaurant"),)
			
			#指定默认按什么字段排序
			#只有设置了该属性,我们查询到的结果才可以被reverse() ****
			ordering = ('name')
			
            # admin中显示的表名称
            verbose_name=''

            # verbose_name加s
            verbose_name_plural=''
```

### 关系字段
#### ForeignKey
外键类型在ORM中用来表示外键关联关系，一般把ForeignKey字段设置在 '一对多'中'多'的一方。

ForeignKey可以和其他表做关联关系同时也可以和自身做关联关系。
to 
> 设置要关联的表

to_field
>设置要关联的表的字段

related_name
> 反向操作时,使用的字段名,用于代替原反向查询时的  '表名_set'
> 
``` python
class Classes(models.Model):
    name = models.CharField(max_length=32)

class Student(models.Model):
    name = models.CharField(max_length=32)
    theclass = models.ForeignKey(to="Classes")
复制代码
复制代码
当我们要查询某个班级关联的所有学生（反向查询）时，我们会这么写：

models.Classes.objects.first().student_set.all()
当我们在ForeignKey字段中添加了参数 related_name 后，

class Student(models.Model):
    name = models.CharField(max_length=32)
    theclass = models.ForeignKey(to="Classes", related_name="students")
当我们要查询某个班级关联的所有学生（反向查询）时，我们会这么写：

models.Classes.objects.first().students.all()
```
related_query_name
> 反向查询操作时,使用的连接前缀,用于替换表名

on_delete
>当删除关联表中的数据时,当前表与其关联的行为
``` python
　　models.CASCADE
　　删除关联数据，与之关联也删除

　　models.DO_NOTHING
　　删除关联数据，引发错误IntegrityError

　　models.PROTECT
　　删除关联数据，引发错误ProtectedError

　　models.SET_NULL
　　删除关联数据，与之关联的值设置为null（前提FK字段需要设置为可空）

　　models.SET_DEFAULT
　　删除关联数据，与之关联的值设置为默认值（前提FK字段需要设置默认值）

　　models.SET

　　删除关联数据，
　　a. 与之关联的值设置为指定值，设置：models.SET(值)
　　b. 与之关联的值设置为可执行对象的返回值，设置：models.SET(可执行对象)
　　
　　def func():
    return 10

    class MyModel(models.Model):
        user = models.ForeignKey(
            to="User",
            to_field="id"，
            on_delete=models.SET(func)
        )
```
db_constraint
> 是否在数据库中创建外键约束,默认为True

### OneToOneField
一对一字段
通常一对一字段用来扩展已有字段
一对一的关联关系多用在当一张表的不用字段查询频次差距过大的情况下,将本可以存储在一张表的字段拆开放置在两张表中,然后将两张表建立一对一的关系
``` python
class Author(models.Model):
    name = models.CharField(max_length=32)
    info = models.OneToOneField(to='AuthorInfo')
    

class AuthorInfo(models.Model):
    phone = models.CharField(max_length=11)
    email = models.EmailField()
```
to
> 设置要关联的表

to_field
> 设置要关联的字段

on_delete
> 同ForeignKey字段

### ManyToManyField
用于表示多对多的关联关系,在数据库中通过第三张表;来创建关联关系
to
> 设置要关联的表

related_name
> 同ForeignKey

related_query_name
> oreignKey字段

symmetrical
> 于多对多自关联时，指定内部是否创建反向操作的字段。默认为True。

举个例子：
```
class Person(models.Model):
​    name = models.CharField(max_length=16)
​    friends = models.ManyToManyField("self")
此时，person对象就没有person_set属性。

class Person(models.Model):
​    name = models.CharField(max_length=16)
​    friends = models.ManyToManyField("self", symmetrical=False)
此时，person对象现在就可以使用person_set属性进行反向查询。
```

through
> 在使用ManyToManyField 字段时,django 将自动生成一张表来管理多对多的关联关系
> 但我们也可以手动创建第三张表来管理多对多关系,此时就需要通过through来指定第三张表的表名

through_field
> 设置关联的字段

db_table
> 默认创建第三张表时,数据库中表的名称.

#### 多对多关联关系的三种方式
##### 自行创建第三张表
``` python
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者姓名")


# 自己创建第三张表，分别通过外键关联书和作者
class Author2Book(models.Model):
    author = models.ForeignKey(to="Author")
    book = models.ForeignKey(to="Book")

    class Meta:
        unique_together = ("author", "book")
```
##### 通过ManyToManyField 自动创建第三张表
``` python
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")


# 通过ORM自带的ManyToManyField自动创建第三张表
class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者姓名")
    books = models.ManyToManyField(to="Book", related_name="authors")
```
##### 方式三, 设置ManyToManyField 并指定自行创建的第三张表
``` python
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")


# 自己创建第三张表，并通过ManyToManyField指定关联
class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者姓名")
    books = models.ManyToManyField(to="Book", through="Author2Book", through_fields=("author", "book"))
    # through_fields接受一个2元组（'field1'，'field2'）：
    # 其中field1是定义ManyToManyField的模型外键的名（author），field2是关联目标模型（book）的外键名。


class Author2Book(models.Model):
    author = models.ForeignKey(to="Author")
    book = models.ForeignKey(to="Book")

    class Meta:
        unique_together = ("author", "book")
```
##### 注意,
当我们需要在第三张表中存储额外的字段时,就要使用第三中方式
但是当我们使用第三张方式创建多对多关联关系时,就无法使用set,add,remove,clear,方法来管理多对多的关系了,需要通过第三章表的model来管理多对多的关系.


# Settings 配置数据库

若想将模型转为mysql数据库中的表，需要在settings中配置：
``` python
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
```
### 注意1：
NAME即数据库的名字，在mysql连接前该数据库必须已经创建，而上面的sqlite数据库下的db.sqlite3则是项目自动创建 USER和PASSWORD分别是数据库的用户名和密码。设置完后，再启动我们的Django项目前，我们需要激活我们的mysql。然后，启动项目，会报错：no module named MySQLdb 。这是因为django默认你导入的驱动是MySQLdb，可是MySQLdb 对于py3有很大问题，所以我们需要的驱动是PyMySQL 所以，我们只需要找到项目名文件下的__init__,在里面写入：
``` python
import pymysql
pymysql.install_as_MySQLdb()
```
最后通过两条数据库迁移命令即可在指定的数据库中创建表
`python manage.py makemigrations`
`python manage.py migrate`
### 注意2
确保配置文件中的INSTALLED_APPS中写入我们创建的app名称
``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "book"
]
```
### 注意3 果报错如下
`django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.7.11.None`
MySQLclient目前只支持到python3.4，因此如果使用的更高版本的python，需要修改如下：

通过查找路径C:\Programs\Python\Python36-32\Lib\site-packages\Django-2.0-py3.6.egg\django\db\backends\mysql
这个路径里的文件把
``` python
if version < (1, 3, 3):
     raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)
```
注释掉就可以了

### 注意4 果想打印orm转换过程中sql,需要在settings中进行如下配置
``` python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
```


# 增加 删除字段
删除 直接注释掉字段,执行数据库迁移命令即可
新增字段,在类里直接新增字段,执行执行数据库迁移命令会提示输入默认值,此时需要设置
`publish = models.CharField(max_length=12,default='人民出版社',null=True)`


#### 注意
　　1. 据库迁移记录都在 app01下的migrations里

　　2. 用showmigrations命令可以查看没有执行migrate的文件

　　3. makemigrations是生成一个文件，migrate是将更改提交到数据量

# 添加表记录
### 方式1 
`# create方法的返回值book_obj就是插入book表中的python葵花宝典这本书籍纪录对象`
`book_obj=Book.objects.create(title="python葵花宝典",state=True,price=100,publish="苹果出版社",pub_date="2012-12-12")`

### 方式2 
`book_obj=Book(title="python葵花宝典",state=True,price=100,publish="苹果出版社",pub_date="2012-12-12")`
`book_obj.save()`

# 查询表记录
## 查询API
``` python
<1> all():                  查询所有结果
  
<2> filter(**kwargs):       它包含了与所给筛选条件相匹配的对象
  
<3> get(**kwargs):          返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
  
<4> exclude(**kwargs):      它包含了与所给筛选条件不匹配的对象
 
<5> order_by(*field):       对查询结果排序('-id')
  
<6> reverse():              对查询结果反向排序
  
<8> count():                返回数据库中匹配查询(QuerySet)的对象数量。
  
<9> first():                返回第一条记录
  
<10> last():                返回最后一条记录
  
<11> exists():              如果QuerySet包含数据，就返回True，否则返回False
 
<12> values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
                            model的实例化对象，而是一个可迭代的字典序列
<13> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
 
<14> distinct():            从返回结果中剔除重复纪录
```
## 基于双下划线的模糊查询
``` python
Book.objects.filter(price__in=[100,200,300])
Book.objects.filter(price__gt=100)
Book.objects.filter(price__lt=100)
Book.objects.filter(price__gte=100)
Book.objects.filter(price__lte=100)
Book.objects.filter(price__range=[100,200])
Book.objects.filter(title__contains="python")
Book.objects.filter(title__icontains="python")
Book.objects.filter(title__startswith="py")
Book.objects.filter(pub_date__year=2012)
```
## 删除表记录
删除方法就是 delete(), 它运行时立即删除对象而不返回任何值. 如下:
`model_obj.delete()`
你也可以一次性删除多个对象. 每个QuerySet都有一个delete()方法,它一次性删除 QuerySet 中所有的对象
例如,下面的代码将删除 pub_date 是2005年的Entry 对象:
`Entry.objects.filter(pub_date__year=2005).delete()`
在 Django 删除对象时，会模仿 SQL 约束 ON DELETE CASCADE 的行为，换句话说，删除一个对象时也会删除与它相关联的外键对象。例如：
```
b = Blog.objects.get(pk=1)
# This will delete the Blog and all of its Entry objects.
b.delete()
```
要注意的是： delete() 方法是 QuerySet 上的方法，但并不适用于 Manager 本身。这是一种保护机制，是为了避免意外地调用 Entry.objects.delete() 方法导致 所有的 记录被误删除。如果你确认要删除所有的对象，那么你必须显式地调用：

Entry.objects.all().delete()　
如果不想级联删除，可以设置为:

pubHouse = models.ForeignKey(to='Publisher', on_delete=models.SET_NULL, blank=True, null=True)

## 修改表记录
`Book.objects.filter(title__startswith="py").update(price=120)`
此外，update()方法对于任何结果集（QuerySet）均有效，这意味着你可以同时更新多条记录update()方法会返回一个整型数值，表示受影响的记录条数。

#  在Python脚本中调用Django环境
``` python
import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled15.settings")
    import django
    django.setup()

    from app01 import models

    books = models.Book.objects.all()
    print(books)
```

# Django终端打印SQL语句
``` python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
```


# 测试数据
``` python
def index(request):
    # 添加表记录++++++++++++++++++++++++++++++++++
    # 方式一
    # book=Book(name='红楼梦',pub_data='2015-10-12',price=88,publish='老男孩出版社')
    # book.save()
    # 方式二
    # Book.objects.create(name='Python红宝书',pub_data='2010-10-12',price=100,publish='人民出版社')
    # 查询表记录++++++++++++++++++++++++++++++++++
    # QUerySet数据类型（类似于一个列表，里面放着一些对象）
    # 1 方法的返回值是什么
    # 2 方法的调用者
    # (1) all方法 返回一个QuerySet对象
    # book_list=Book.objects.all()
    # print(book_list[1].name)
    # print(book_list)
    # for obj in book_list:
    #     print(obj.name)
    # (2)first last：调用者是queryset对象，返回值是对象
    # book=Book.objects.all().first()
    # book2=Book.objects.all().last()
    # print(book)
    # print(book2)
    # (3) filter  返回值是queryset对象(相当于where语句)
    # 可以加多个过滤条件
    # book=Book.objects.filter(name='红楼梦').first()
    # print(book)
    # (4)get方法 有且只有一个查询结果才有意义 返回值是一个对象
    # book=Book.objects.get(name='红楼梦')
    # print(book)
    # 直接报错
    # book = Book.objects.get(name='红楼梦eee')
    # --------------最常用-----------------
    # (5)exclude 除了查询之外的 返回值也是queryset
    # ret=Book.objects.exclude(name='红楼梦')
    # print(ret)
    # （6）order_by(默认升序，加个- 就是降序),可以多个过滤条件调用者是queryset返回值也是queryset
    # book_list=Book.objects.all().order_by('id')
    # book_list=Book.objects.all().order_by('-id','price')
    # print(book_list)
    # （7）count() 调用者是queryset，返回值是int
    # ret=Book.objects.all().count()
    # print(ret)
    # (8)exist()判断是是否有值，不能传参数，
    # ret=Book.objects.all().exists()
    # print(ret)
    # （9）values方法
    # 查询所有书籍的名称(里面传的值，前提是表有这个字段)也是queryset但是里面放的是字典
    '''
    values原理
    temp=[]
    for obj in Book.objects.all():
        temp.append({'name':obj.name})
    '''
    # ret=Book.objects.all().values('name')
    # print(ret)
    # 不加.all()也可以,调用是queryset返回值也是queryset
    # ret=Book.objects.values('price')
    # print(ret)
    # （10）value_list
    # ret=Book.objects.all().values_list('price','name')
    # print(ret)
    # (11) distinct  seletc * 的时候没有意义
    # SELECT DISTINCT name from app01_book;
    # 没有任何意义，不要这样么用
    # Book.objects.all().distinct()
    # ret=Book.objects.all().values('name').distinct()
    # print(ret)

    # 双下划线模糊查询-----------------------
    # 查询价格大于100的书
    # ret=Book.objects.filter(price__gt=100)
    # print(ret)
    # 查询大于50小于100的书
    # ret=Book.objects.filter(price__gt=50,price__lt=100)
    # print(ret)
    # 查询已红楼开头的书
    # ret=Book.objects.filter(name__startswith='红楼')
    # print(ret)
    # 查询包含‘红’的书
    # ret= Book.objects.filter(name__contains='红')
    # print(ret)
    # icontains  不区分大小写
    # 价格在50，88，100 中的
    # ret=Book.objects.filter(price__in=[50,88,100])
    # print(ret)
    # 出版日期在2018年的
    # ret=Book.objects.filter(pub_data__year=2015,pub_data__month=2)
    # print(ret)
    # 删除，修改------------------------
    # delete：调用者可以是queryset也可以是model对象
    # 删除价格为188的书有返回值 (1, {'app01.Book': 1}) 删除的个数，那张表，记录数
    # ret=Book.objects.filter(price=188).delete()
    # print(ret)
    # ret=Book.objects.filter(price=100).first().delete()
    # print(ret)

    # 修改 update只能queryset来调用 返回值为int
    # ret=Book.objects.filter(name='红楼梦1').update(name='红楼梦')
    # print(ret)
    # 报错
    # Book.objects.filter(name='红楼梦').first().update(name='红楼梦1')

    # ret=Book.objects.filter(name='红楼梦1').first()
    # print(ret.delete())
    # aa=Publish.objects.filter(name='人民出版社')
    # print(type(aa))
    # aa.delete()

    return HttpResponse('ok')
    ```




