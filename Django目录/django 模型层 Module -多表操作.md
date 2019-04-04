# 创建模型
Sql 语句
``` sql
CREATE TABLE publish(
                id INT PRIMARY KEY auto_increment ,
                name VARCHAR (20)
              );


CREATE TABLE book(
                id INT PRIMARY KEY auto_increment ,
                title VARCHAR (20),
                price DECIMAL (8,2),
                pub_date DATE ,
                publish_id INT ,
                FOREIGN KEY (publish_id) REFERENCES publish(id)
              );


CREATE TABLE authordetail(
                id INT PRIMARY KEY auto_increment ,
                tel VARCHAR (20)
              );

CREATE TABLE author(
                id INT PRIMARY KEY auto_increment ,
                name VARCHAR (20),
                age INT,
                authordetail_id INT UNIQUE ,
                FOREIGN KEY (authordetail_id) REFERENCES authordetail(id)
              );



CREATE  TABLE book2author(
       id INT PRIMARY KEY auto_increment ,
       book_id INT ,
       author_id INT ,
       FOREIGN KEY (book_id) REFERENCES book(id),
       FOREIGN KEY (author_id) REFERENCES author(id)
)
```
Models创建如下模型
``` python
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish_date = models.DateField()
    # 阅读数
    # reat_num=models.IntegerField(default=0)
    # 评论数
    # commit_num=models.IntegerField(default=0)

    publish = models.ForeignKey(to='Publish',to_field='nid',on_delete=models.CASCADE)
    authors=models.ManyToManyField(to='Author')
    def __str__(self):
        return self.name


class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    author_detail = models.OneToOneField(to='AuthorDatail',to_field='nid',unique=True,on_delete=models.CASCADE)


class AuthorDatail(models.Model):
    nid = models.AutoField(primary_key=True)
    telephone = models.BigIntegerField()
    birthday = models.DateField()
    addr = models.CharField(max_length=64)


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()
```
# 添加表记录
## 一对多的
``` python
方式1:
   publish_obj=Publish.objects.get(nid=1)
   book_obj=Book.objects.create(title="",publishDate="2012-12-12",price=100,publish=publish_obj)
  
方式2:
   book_obj=Book.objects.create(title="",publishDate="2012-12-12",price=100,publish_id=1)
```
``` python
# -----一对多添加
pub=Publish.objects.create(name='egon出版社',email='445676@qq.com',city='山东')
print(pub)

# 为book表绑定和publish的关系
import datetime,time
now=datetime.datetime.now().__str__()
now = datetime.datetime.now().strftime('%Y-%m-%d')
print(type(now))
print(now)
# 日期类型必须是日期对象或者字符串形式的2018-09-12（2018-9-12），其它形式不行
Book.objects.create(name='海燕3',price=333.123,publish_date=now,publish_id=2)
Book.objects.create(name='海3燕3',price=35.123,publish_date='2018/02/28',publish=pub)
pub=Publish.objects.filter(nid=1).first()
book=Book.objects.create(name='测试书籍',price=33,publish_date='2018-7-28',publish=pub)
print(book.publish.name)
# 查询出版了红楼梦这本书出版社的邮箱
book=Book.objects.filter(name='红楼梦').first()
print(book.publish.email)
```
## 多对多添加
``` python
# 当前生成的书籍对象
book_obj=Book.objects.create(title="追风筝的人",price=200,publishDate="2012-11-12",publish_id=1)
# 为书籍绑定的做作者对象
yuan=Author.objects.filter(name="yuan").first() # 在Author表中主键为2的纪录
egon=Author.objects.filter(name="alex").first() # 在Author表中主键为1的纪录

# 绑定多对多关系,即向关系表book_authors中添加纪录
book_obj.authors.add(yuan,egon)    #  将某些特定的 model 对象添加到被关联对象集合中。   =======    book_obj.authors.add(*[])
```
``` python
book = Book.objects.filter(name='红楼梦').first()
egon=Author.objects.filter(name='egon').first()
lqz=Author.objects.filter(name='lqz').first()
# 1 没有返回值，直接传对象
book.authors.add(lqz,egon)
# 2 直接传作者id
book.authors.add(1,3)
# 3 直接传列表,会打散
book.authors.add(*[1,2])
# 解除多对多关系
book = Book.objects.filter(name='红楼梦').first()
# 1 传作者id
book.authors.remove(1)
# 2 传作者对象
egon = Author.objects.filter(name='egon').first()
book.authors.remove(egon)
#3 传*列表
book.authors.remove(*[1,2])
#4 删除所有
book.authors.clear()
# 5 拿到与 这本书关联的所有作者，结果是queryset对象，作者列表
ret=book.authors.all()
# print(ret)
# 6 queryset对象，又可以继续点（查询红楼梦这本书所有作者的名字）
ret=book.authors.all().values('name')
print(ret)
# 以上总结：
# （1）
# book=Book.objects.filter(name='红楼梦').first()
# print(book)
# 在点publish的时候，其实就是拿着publish_id又去app01_publish这个表里查数据了
# print(book.publish)
# （2）book.authors.all()
```
多对多关系其它常用API：

book_obj.authors.remove()      # 将某个特定的对象从被关联对象集合中去除。    ======   book_obj.authors.remove(*[])
book_obj.authors.clear()       #清空被关联对象集合
book_obj.authors.set()         #先清空再设置　

# 基于对象的跨表查询
## 一对多查询（publish与book）
正向查询(按字段:publish)
反向查询(按表名: book_set)
``` python

# 一对多正向查询
book=Book.objects.filter(name='红楼梦').first()
print(book.publish)#与这本书关联的出版社对象
print(book.publish.name)
# 一对多反向查询
# 人民出版社出版过的书籍名称
pub=Publish.objects.filter(name='人民出版社').first()
ret=pub.book_set.all()
print(ret)
```
## 一对一查询 （Author 与 AuthorDetail）
### 正向查询 (按字段: authorDetail)
### 反向查询(按表名：author)：
``` python
# 一对一正向查询
# lqz的手机号
lqz=Author.objects.filter(name='lqz').first()
tel=lqz.author_detail.telephone
print(tel)
# 一对一反向查询
# 地址在北京的作者姓名
author_detail=AuthorDatail.objects.filter(addr='北京').first()
name=author_detail.author.name
print(name)
```
## 多对多查询 (Author 与 Book)
### 正向查询 (按字段: authors)
### 反向查询(按表名：book_set)
``` python
# 正向查询----查询红楼梦所有作者名称
book=Book.objects.filter(name='红楼梦').first()
ret=book.authors.all()
print(ret)
for auth in ret:
    print(auth.name)
    # 反向查询 查询lqz这个作者写的所有书
    author=Author.objects.filter(name='lqz').first()
    ret=author.book_set.all()
    print(ret)
```
## 注意：

你可以通过在 ForeignKey() 和ManyToManyField的定义中设置 related_name 的值来覆写 FOO_set 的名称。例如，如果 Article model 中做一下更改：
publish = ForeignKey(Book, related_name='bookList')

那么接下来就会如我们看到这般:
查询 人民出版社出版过的所有书籍

publish=Publish.objects.get(name="人民出版社")
book_list=publish.bookList.all()  # 与人民出版社关联的所有书籍对象集合

# 基础双下划线的跨表查询
###   正向查询按字段,反向查询按表名小写用来告诉ORM引擎join哪张表
### 一对多查询
``` python
# 正向查询按字段，反向查询按表名小写
# 查询红楼梦这本书出版社的名字
# select * from app01_book inner join app01_publish
# on app01_book.publish_id=app01_publish.nid
ret=Book.objects.filter(name='红楼梦').values('publish__name')
print(ret)
ret=Publish.objects.filter(book__name='红楼梦').values('name')
print(ret)
```
### 多对多查询
``` python
# 正向查询按字段，反向查询按表名小写
# 查询红楼梦这本书出版社的名字
# select * from app01_book inner join app01_publish
# on app01_book.publish_id=app01_publish.nid
ret=Book.objects.filter(name='红楼梦').values('publish__name')
print(ret)
ret=Publish.objects.filter(book__name='红楼梦').values('name')
print(ret)
# sql 语句就是from的表不一样
# -------多对多正向查询
# 查询红楼梦所有的作者
ret=Book.objects.filter(name='红楼梦').values('authors__name')
print(ret)
# ---多对多反向查询
ret=Author.objects.filter(book__name='红楼梦').values('name')
ret=Author.objects.filter(book__name='红楼梦').values('name','author_detail__addr')
print(ret)
```

### 一对一查询
``` python
# 查询lqz的手机号
# 正向查
 ret=Author.objects.filter(name='lqz').values('author_detail__telephone')
print(ret)
# 反向查
ret= AuthorDatail.objects.filter(author__name='lqz').values('telephone')
print(ret)
```
### 连续跨表
``` python
# ----进阶练习，连续跨表
# 查询手机号以33开头的作者出版过的书籍名称以及书籍出版社名称
# author_datail author book publish
# 基于authorDatail表
ret=AuthorDatail.objects.filter(telephone__startswith='33').values('author__book__name','author__book__publish__name')
print(ret)
# 基于Author表
ret=Author.objects.filter(author_detail__telephone__startswith=33).values('book__name','book__publish__name')
print(ret)
# 基于Book表
ret=Book.objects.filter(authors__author_detail__telephone__startswith='33').values('name','publish__name')
print(ret)
# 基于Publish表
ret=Publish.objects.filter(book__authors__author_detail__telephone__startswith='33').values('book__name','name')
print(ret)
```

### related_name
反向查询时，如果定义了related_name ，则用related_name替换表名
``` python
publish = ForeignKey(Blog, related_name='bookList')
复制代码
# 练习: 查询人民出版社出版过的所有书籍的名字与价格(一对多)

# 反向查询 不再按表名:book,而是related_name:bookList


queryResult=Publish.objects.filter(name="人民出版社").values_list("bookList__title","bookList__price") 
```

# 聚合查询 分组查询
## 聚合`from django.db.models import Avg, Max, Sum, Min, Max, Count`
aggregate(*args, **kwargs)
``` python
# 计算所有图书的平均价格
 from django.db.models import Avg
 Book.objects.all().aggregate(Avg('price'))
#{'price__avg': 34.35}
```
aggregate()是QuerySet 的一个终止子句，意思是说，它返回一个包含一些键值对的字典。键的名称是聚合值的标识符，值是计算出来的聚合值。键的名称是按照字段和聚合函数的名称自动生成出来的。如果你想要为聚合值指定一个名称，可以向聚合子句提供它。
``` python
Book.objects.aggregate(average_price=Avg('price'))
#{'average_price': 34.35}
```
如果你希望生成不止一个聚合，你可以向aggregate()子句中添加另一个参数。所以，如果你也想知道所有图书价格的最大值和最小值，可以这样查询：
``` python
from django.db.models import Avg, Max, Min
Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))
#{'price__avg': 34.35, 'price__max': Decimal('81.20'), 'price__min': Decimal('12.99')}
```
``` python
# 查询所有书籍的平均价格
from django.db.models import Avg,Count,Max,Min
ret=Book.objects.all().aggregate(Avg('price'))
# {'price__avg': 202.896}
# 可以改名字
ret=Book.objects.all().aggregate(avg_price=Avg('price'))
# 统计平均价格和最大价格
ret=Book.objects.all().aggregate(avg_price=Avg('price'),max_price=Max('price'))
# 统计最小价格
ret = Book.objects.all().aggregate(avg_price=Avg('price'), min_price=Min('price'))
# 统计个数和平均价格
ret = Book.objects.all().aggregate(avg_price=Avg('price'), max_price=Max('price'),count=Count('price'))
ret = Book.objects.all().aggregate(avg_price=Avg('price'), max_price=Max('price'),count=Count('nid'))
print(ret)
```
## 分组 `annotate()`
annotate()为调用的QuerySet中每一个对象都生成一个独立的统计值（统计方法用聚合函数）。
总结 ：跨表分组查询本质就是将关联表join成一张表，再按单表的思路进行分组查询。　
### 查询练习
1. 统计每一本书作者个数
``` python
from django.db.models import Avg, Max, Sum, Min, Max, Count
book_list = models.Book.objects.all().annotate(author_num=Count("authors"))
for book in book_list:
     print(book.name)
     print(book.author_num)
book_list = models.Book.objects.all().annotate(author_num=Count("authors")).values('name','author_num')
print(book_list)
```
2. 统计每一个出版社的最便宜的书
``` python
publishList=Publish.objects.annotate(MinPrice=Min("book__price"))
for publish_obj in publishList:
    print(publish_obj.name,publish_obj.MinPrice)
```
annotate的返回值是querySet,如果不想遍历对象,可以用上valuelist
``` python
queryResult= Publish.objects.annotate(MinPrice=Min("book__price")).values_list("name","MinPrice")
print(queryResult)
```
3. 统计每一本以py开头的书籍的作者个数
` queryResult=Book.objects.filter(title__startswith="Py").annotate(num_authors=Count('authors'))`
4. 统计不止一个作者的图书(作者数量大于1)
``` python
ret=models.Book.objects.annotate(author_num=Count("authors")).filter(author_num__gt=1).values('name','author_num')
print(ret)
```
5. 根据一本图书作者数量的多少对查询集QuerySet进行排序
`Book.objects.annotate(num_authors=Count('authors')).order_by('num_authors')`
6. 查询各个作者出的书的总价格
`ret=models.Author.objects.annotate(sum_price=Sum("book__price")).values("name", "sum_price")`
7. 查询没个出版社的名称和书籍个数
`ret=models.Publish.objects.all().annotate(c=Count('book__name')).values('name','c')`




























