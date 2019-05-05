## for循环

1. go 只有for一个循环语句关键字，但支持3种形式
2. 初始化和步进表达式可以是多个值
3. 条件语句每次循环都会被重新检查，因为不建议在条件语句中使用函数
		使用函数，尽量提前计算好条件病以变量或常量代替
4. 左大括号必须和条件语句在同一行

``` go
func main(){
	a := 1
	for {
		a++
		if a >3 {
			break
		}
	}
	fmt.Println(a)
}

// 2 
func main{
	a := 1 
	for a <= 3 {
		a++
	}
	fmt.Println(a)
}

// 3
func main(){
	a := 1 
	for i:=0;i < 3;i++{
		a++
	}
	fmt.Prntln(a)	
}
```



![image-20190502162333461](/Users/garry/Library/Application Support/typora-user-images/image-20190502162333461.png)