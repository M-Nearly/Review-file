## 跳转语句 goto ，break ， continue

1. 三个语法都可以配合标签使用
2. 标签名区分大小写，若不使用会造成编译错误
3. break 与 continue 配盒标签可用于多层循环跳出
4. goto 是调整执行位置，与其他2个语句配合标签的结果并不相同

``` go
func main(){
  LABEL:
  for {
    for i :=0;i <10;i++{
      if i > 2{
        break LABEL
      }else {
        fmt.Println(i)
      }
    }
  }
}


func main(){
  for {
    for i :=0;i <10;i++{
      if i > 2{
        goto LABEL
      }else {
        fmt.Println(i)
      }
    }
  }
LABEL :
	  xxxx
}
```

