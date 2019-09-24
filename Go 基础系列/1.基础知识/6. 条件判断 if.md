## 判断语句 if
1. 条件表达式没有括号
2. 支持一个初始化表达式
3. 左大括号必须和条件语句或else 同一行
4. 支持单行模式
5. 初始化语句中的变量为block级别，同时隐藏外部同名变量

``` go

func main(){
	a := true
	if  a,b,c := 1,2,3; a+b+c > 6 {
		fmt.Println("> 6")
	}else {
		fmt.Println("< 6")
		fmt.Println(a)
	}
	fmt.Println(a)
}
```

