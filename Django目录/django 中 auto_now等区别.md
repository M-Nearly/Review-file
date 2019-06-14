
## auto_now_add 参数
	设置为true时,会在model对象第一次被创建时, 将字段的值设置为创建时的时间,以后修改对象时,字段的值也不会更新
	 该属性通常被用在存储"创建时间"的场景下.


​	 
## auto_now
	每次保存对象时,自动将字段值设置为当前时间,能后再保存该字段时,将其值设置为当前时间,并且每次修改model,都会自动更新,
	该属性通常用在存储"最后修改时间"的场景下,常用类似"last-modified"或者"updatetime"字段


​	
## 在admin中实现可编辑
	anto_now 和 auto_now_add 被设置为True后,在样做会导致字段成为 editable=False 和 blank=True 的状态
	editable=False 将导致地段不会被呈现在admin中,blank=True 表示允许在表单中不输入值.
	此时,如果在admin的fields 或 fieldset 中强行加入该日期时间字段,name程序会报错,admin无法打开,
	如果在admin中修改对象时,想要看到日期和时间,可以将日期时间字段添加到admin类中readonly_fields 中 `readonly_fields = ('save_date', 'mod_date',)`
	
	实际场景中,往往即虚妄在对象的创建时间默认被设置为当前值,又希望能在日后修改它,怎么实现这种需求?
	django中的所有model字段都拥有一个default参数,用来给字段设置默认值.
	
	可以用default=timezong.now来天幻auto_now=True 或者 auto_now_add=True
	
	timezone.now 对用着django.utils.timezone.now 


​	
## 自定义日期格式,
> 刚创建的django应用,日期格式跟 language 和 TIME_ZONE 有关
> 
如果不习惯这种格式,自己定义显示格式的配置如下,更下Django的setting.py文件
``` python
USE_L10N = False
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'
```
注意事项: 如果USE_L10N 设置为True,name语言环境规定的格式具有更高的优先级并将被应用,即DATE_FORMAT 不生效

