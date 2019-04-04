MySQL MySQL是一个关系型数据库管理系统
##基本操作
	创建数据库 create database xx default charset utf8 ;
用户相关:
	创建用户
		create user 'user'@'IP地址/*' identified  by 'password';
	删除用户
		drop user 'user'@'IP地址/*'
	修改用户
		rename user 'user'@'IP地址/*' to 'new user'@'IP地址/*'
	修改密码
		set password for 'user'@'IP地址' = password('new password')

	-- mysql user 表中
授权管理
	查看权限
		show grants for 'user'@'IP地址' 
	授权
		grant 权限 on 数据库.表 to 'user'@'IP地址'
	取消授权
		revoke 权限 on 数据库.表 from 'user'@'IP地址'

	例子:
    grant all privileges on db1.tb1 TO '用户名'@'IP'
    grant select on db1.* TO '用户名'@'IP'
    grant select,insert on *.* TO '用户名'@'IP'
    revoke select on db1.tb1 from '用户名'@'IP'
	***
	flush privileges，将数据读取到内存中，从而立即生效。
数据表 
	1. 创建表
		create table 表名(
		    列名  类型  是否可以为空，
		    列名  类型  是否可以为空
		)ENGINE=InnoDB DEFAULT CHARSET=utf8

		类型
			空 null / not null
			默认值 default x,
			自增列 auto_increment    ** 表中只能有一个自增列 所以基本连用 **
			对于自增可以设置步长和起始值
	             show session variables like 'auto_inc%';
	             set session auto_increment_increment=2;
	             set session auto_increment_offset=10;

	             shwo global  variables like 'auto_inc%';
	             set global auto_increment_increment=2;
	             set global auto_increment_offset=10;

	        主键 primary key
		        主键，一种特殊的唯一索引，不允许有空值，如果主键使用单个列，则它的值必须唯一，如果是多列，则其组合必须唯一。
		        create table tb1(
		            nid int not null auto_increment primary key,
		            num int null
		        )
		        或
		        create table tb1(
		            nid int not null,
		            num int not null,
		            primary key(nid,num)
		        )

	        外键 一个特殊的索引，只能是指定内容

	            creat table color(
	                nid int not null primary key,
	                name char(16) not null
	            )

	            create table fruit(
	                nid int not null primary key,
	                smt char(32) null ,
	                color_id int not null,
	                constraint fk_cc foreign key (color_id) references color(nid)
	            )

    2. 删除表
    	drop table 表名
	3. 清空表
		delete from 表名
		truncate table 表名
	4. 修改表
		添加列 
			alter table 表名 add 列名 类型 ;
		删除列
			alter table 表名 drop column 列名
		修改列
			alter table 表名 modity column 列名 类型 ;
			alter table 表名 change 原列名 新列名 类型 ;
		添加主键
			alter table 表名 add primary key(列名)
		删除主键
			alter table 表名 drop primary key ;
			alter table 表名 modify 列名 int, drop primary key ;

		添加外键
			alter table 表名 add constraint 外键名称(比如,FK_从表_主表) foreign key 从表(外键字段) references 主表(主键字段) ;
		删除外键
			alter table 表名 drop foreign key 外键名称

		修改默认值：ALTER TABLE testalter_tbl ALTER i SET DEFAULT 1000;
		删除默认值：ALTER TABLE testalter_tbl ALTER i DROP DEFAULT; 

	5. 基本的数据类型
		1. 

	6. 操作表内容
		1. 增
			insert into 表(列名,列名..) values(值,值..)
			insert into 表(列名,列名..) values(值,值..),(值,值..)
			insert into 表(列名,列名..) select (列名,列名..) from 表;
		2. 删
			delete from 表
			delete from 表 where id=1 and name='egon'
		3. 改
			update 表 set name = 'egon' where id>1 
		4. 查
			select * from 表
			select * from 表 where id>1
			select  nid,name,gender as gg from 表 where id>1
		5. 其他
			a. 条件 where
				select * from 表 where id> 1 and name != 'xx' ;		
				select * from 表 where id between 5 and 16 ;
				select * from 表 where id in / not in (1,2,3)
				select * from 表 where id in (select nid from 表)

			b. 通配符 like
				select * from 表 wheree name like 'xx%' -- 以xx开头的字符串(多个字符)
				select * from 表 wheree name like 'xx_' -- 以xx开头的字符串(1个字符)

			c. 限制 limit
				select * from 表 limit 5 ; --前5行
				select * from 表 limit 4,5 ; --从第4行开始的5行
				select * from 表 limit 5  offset 4 ; --从第4行开始的5行

			d. 排序 order by
				select * from 表 order by 列 asc
				select * from 表 order by 列 desc
				select * from 表 order by 列1 desc ,列2 asc

			e. 分组 group by  having 
				select num from 表 group by num
				select num,nid from 表 group by num,nid
				select num,nid,count(*),sum(score),max(score),min(score) from 表 group by num,nid

 
				select num from 表 group by num having max(id) >10
				** 特别的：group by 必须在where之后，order by之前
			f. 连表
				无对应关系则不显示
					select A.num ,A.name,B.name
					from A,B
					where A.nid = B.nid
				无对应关系则不显示
					select A.num,A.name,B.name
					from A inner join B
					on A.nid = B.nid

				A表有所显示,如果B中无对应关系,则值为null,
					select A.num,A.name,B.name
					from A right join B
					on A.nid = B.nid

				B表有所显示,如果B中无对应关系,则值为null
					select A.num,A.name,B.name
					from A right join B
					onA.nid = B.nid

			g. 组合
				组合,自动处理重合
				select nickname 
				from A
				union
				select name
				from B

				组合,不处理重合
				select nickname
				from A
				union all
				select name
				from B

