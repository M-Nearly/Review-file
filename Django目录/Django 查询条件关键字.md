### Django基于双下划线的模糊查询：
``` django

__exact 精确等于 like ‘aaa’ 
__iexact 精确等于 忽略大小写 ilike ‘aaa’ 
__contains 包含 like ‘%aaa%’ 
__icontains 包含 忽略大小写 ilike ‘%aaa%’，但是对于sqlite来说，contains的作用效果等同于icontains。 
__gt 大于 
__gte 大于等于 
__lt 小于 
__lte 小于等于 
__in 存在于一个list范围内 
__startswith 以…开头 
__istartswith 以…开头 忽略大小写 
__endswith 以…结尾 
__iendswith 以…结尾，忽略大小写 
__range 在…范围内 
__year 日期字段的年份 
__month 日期字段的月份 
__day 日期字段的日 
__isnull=True/False

User.objects.filter(state__gt=0)//查询状态大于0 
User.objects.filter(state__isnull=True)//查询状态为空
```

## 查询api
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
