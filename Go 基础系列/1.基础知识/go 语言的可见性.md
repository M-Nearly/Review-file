1. 如果想使用别的包的函数,结构体成员,结构体类型

   函数名,类型名,结构体成员变量名,首字母必须大写,可见

   如果首字母是小写,只能是同一个包里使用

   包名.函数名

   包名.结构体的类型名







**只有数组是值传递, slice map 都是地址传递**


在GOPATH 目录下新建三个文件夹
bin: 用来存放编译后生成的可执行文件
pkg:用来存放编译后生成的归档文件
src:用来存放源码文件
scr 是自己的代码 上传到github.com  等


## 常用命令:
	go build   编译
	go run		编译运行
	go install  编译 到bin目录下







## go变量常量 
	声明方式:
		var 变量名 类型
		var meng string
		var ( 
			多个
			)
		声明变量没赋值,默认为该类型的0值


		推到声明
		var name = "meng"
		:= (只能在函数内部使用) 
		name := meng

	匿名变量 _ 用于接收不需要的值

	同一个作用域不能重复声明变量


常量的声明支持简写

const 必须赋值,不支持修改
const (
    pi = 3.1415
    e = 2.7182
)
const (
    n1 = 100
    n2	 // 100
    n3  //100
)


// iota 
// 0.const声明中如果不写,默认就和上一行一样
// 1. 遇到const 初始化为0
// 2. const中没新增一行变量声明就递增1



printf  %s 占位符  %f  %d 


## 字符串的方法 string



## if 分支

if {
	
}else if {
	
}else {
	
}



## for 

for {
	
}

for range(键值循环)
Go语言中可以使用for range遍历数组、切片、字符串、map 及通道（channel）。 通过for range遍历的返回值有以下规律：

数组、切片、字符串返回索引和值。
map返回键和值。
通道（channel）只返回通道内的值。


## case 语句

## goto 
	goto + label
	break + label
	continue + label


https://www.liwenzhou.com/posts/Go/01_var_and_const/

![go文件的代码结构](assets/go文件的代码结构.png)