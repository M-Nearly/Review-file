![image-20190502171223310](/Users/garry/Library/Application Support/typora-user-images/image-20190502171223310.png)





----

![image-20190502171600583](/Users/garry/Library/Application Support/typora-user-images/image-20190502171600583.png)



结构的初始化的时候,取地址符号,

赋值的时候并不需要加*

----

匿名结构

![image-20190502171757322](/Users/garry/Library/Application Support/typora-user-images/image-20190502171757322.png)

取内存地址 直接在 struct 前加&

----

结构的嵌套

![image-20190502172205040](/Users/garry/Library/Application Support/typora-user-images/image-20190502172205040.png)

----

匿名字段 

 严格按照结构类型赋值

![image-20190502172305303](/Users/garry/Library/Application Support/typora-user-images/image-20190502172305303.png)

----

![image-20190502172418337](/Users/garry/Library/Application Support/typora-user-images/image-20190502172418337.png)







----



嵌入结构 

匿名字段赋值

![image-20190502172946639](/Users/garry/Library/Application Support/typora-user-images/image-20190502172946639.png)



修改嵌入字段值

![image-20190502173050671](/Users/garry/Library/Application Support/typora-user-images/image-20190502173050671.png)

或 a.human.sex = 100 



----

https://gowalker.org



如果字段名称相同

![image-20190502174803950](/Users/garry/Library/Application Support/typora-user-images/image-20190502174803950.png)

如果 a 中没有 name 字段,两种都可以去到 name

![image-20190502174838521](/Users/garry/Library/Application Support/typora-user-images/image-20190502174838521.png)



----

![image-20190502174907464](/Users/garry/Library/Application Support/typora-user-images/image-20190502174907464.png)



可以把 c 放到 b 内



