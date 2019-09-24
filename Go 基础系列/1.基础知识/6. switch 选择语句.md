## 选择语句

选择语句

1. 可以使用任何类型或表达式作为条件语句
2. 不需要写break，一旦条件符合自动终止
3. 如希望继续执行下一个case，需使用`fallthrough`语句
4. 如果一个初始化表达式（可以是并行方式），右侧需跟分号
5. 左大括号必须和条件语句在同一行
6. 最后 可以   `default:`





``` go
// 1
func main(){
  a := 1
  switch a {
    case 0:
    	fmt.Println("a=0")
  	case 1 :
    	fmt.Println("a=1")
  }
}

//2 
func main(){
  a := 1 
  switch {
    case a >= 0:
    	fmt.Println("a=0")
    	fallthrough
    case a >=1:
    	fmt.Println("a=1")
  }
  fmt.Println(a)
}

//3
func main(){
  switch a := 1;{
    case a >=0:
    	fmt.Println("a>0")
    	fallthrough
    case a >=1 :
    fmt.Println("a=1")
  }
}
```



![image-20190502162208395](/Users/garry/Library/Application Support/typora-user-images/image-20190502162208395.png)



![image-20190502162232621](/Users/garry/Library/Application Support/typora-user-images/image-20190502162232621.png)





![image-20190502162247858](/Users/garry/Library/Application Support/typora-user-images/image-20190502162247858.png)

![image-20190502161944743](/Users/garry/Library/Application Support/typora-user-images/image-20190502161944743.png)



![image-20190502162040565](/Users/garry/Library/Application Support/typora-user-images/image-20190502162040565.png)