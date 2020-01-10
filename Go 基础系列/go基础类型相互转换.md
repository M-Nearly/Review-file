##### s[i]和(for _,v range)的v的区别是什么

```go
var s string = "AB"
fmt.Println(reflect.TypeOf(s[0]))
for _, v := range s {
   fmt.Println(reflect.TypeOf(v))
}
```

##### a.(),和 a(b) 的区别是什么？

```go
var v interface{} = 1
var s uint8 = 1

temp1 := int(s)
temp2 := v.(int)

fmt.Println(temp1,temp2)
```

#### Go的类型系统了解

##### Go的类型

Go语言是一门静态编译型语言，是一门强类型语言，Go语言中类型分为两种：**命名类型(已定义类型)和未命名类型(组合类型)**，我举例说一下

1. 命名类型（已定义类型）

```
uint8(byte) uint16 uint32 uint64 int int8 int16 int32(rune) int64 bool string
float32 float64 complex64 complex128
```

上面举例类型归为三大类：，数值类型，字符串类型， 布尔值类型，我们使用type定义的任何类型也被称为命名类型，如下

```
//也是命名类型
type MyBool bool 
```

1. 未命名类型 (组合类型)

```
slice map chan function interface struct pointer
```

上面举例的类型有容器类型，函数类型，指针类型，结构体类型，通道类型，接口类型

##### 自定义类型和底层类型

Go允许通过type关键字定义一个类型
Go的每一个类型都一个底层类型，类型的底层类型有如下规律

1. 每一个命名类型的底层类型都是自己
2. 每一个组合类型的底层类型都是自己
3. 在一个类型的声明中，新声明的类型和原类型的底层类型是共享的

如下代码,请问这段代码能够编译成功吗？为什么？首先这段代码是编译失败的，i的类型是MyInt，j的类型是int，虽说她们的底层类型都是int，但不能相互赋值，也就说明命名类型间是不能相互赋值的，即便是低限制往高限制赋值，比如 int32 赋给 int64也是编译失败的

```go
type MyInt int
func CustomType() {
   var i MyInt = 2
   var j int = 1
   j = i
   i = j
   fmt.Println(i == j)
}
```

下面这段代码会打印这两个变量的基本类型和底层类型，

```go
//输出MyInt int
fmt.Println(reflect.TypeOf(i), reflect.TypeOf(j))
//输出int int
fmt.Println(reflect.TypeOf(i).Kind(), reflect.TypeOf(j).Kind())
```

我们再来看一个Demo,下面这段代码编译会报错吗，如果把int32改成int64呢？答案是编译报错，改成int64也会编译报错，只有j和int32同时改成i和int64,才会编译成功。因为这时m和n的底层类型是完全相同的。

```go
type MyM struct {
   i int64
}
type MyN struct {
   j int32
}
func TestStruct() {
   n := MyN{j: 10}
   var m MyM
   m = MyM(n)
  fmt.Println(n,m)
}
```

##### 如何追踪朔源一个类型的的底层类型

如下代码，说说这些类型的底层类型是什么？

```go
type MyInt int
type I MyInt
type Ints []int
type MyInts []MyInt
type M map[string]string
type CustomM M
```

MyInt的底层类型是int
I的底层类型时int
Ints的底层类型是[]int
MyInts的底层类型是slice
M的底层类是map
CustomM的底层类是map

**规律就是直到找到的一个内置类型（Go内置的类型）或者未命名类型（组合类型）结束，这个类型就是当前类型的底层类型**

怎么通过代码获取一个类型的底层类型呢?通过下面代码获取

```go
reflect.TypeOf(variable).Kind()
```

##### 类型别名

什么是类型别名呢？Go中有两个类型别名 byte，对应的真实类型是uint8，rune,对应的真实类型是int32，我们可以源代码中这两个的定义如下

```go
// byte is an alias for uint8 and is equivalent to uint8 in all ways. It is
// used, by convention, to distinguish byte values from 8-bit unsigned
// integer values.
type byte = uint8

// rune is an alias for int32 and is equivalent to int32 in all ways. It is
// used, by convention, to distinguish character values from integer values.
type rune = int32
```

从这个就能就能解决最开始的第一个问题，s[index]取得是字符串转换成字节后的某一个字节，而range指的是循环字符串s的每一个字符(range会隐式的unicode解码)， 但字符区分字母和汉字，一个字母占用一个字节，一个汉字可不是了，看如下代码，你可以获取byte和rune的底层类型

```go
var r rune = 'c'
var b byte = 1
fmt.Println(reflect.TypeOf(r).Kind()) //int32
fmt.Println(reflect.TypeOf(b).Kind()) //uint8
```

如何定义一个类型别名呢？其实很简单，知道怎么定义一个类型，那么定义一个类型别名就很简单了，参考上面的byte和rune，如下我们为int64定义一个别名(**从Go1.9开始支持**)，类型别名是可以被声明在函数体内的

```go
//相比定义一个类型多了一个=号
type alaisInt64 = int64
```

##### 类型转换和断言

**类型转换**是用来在类型不同但相互兼容的类型之间的相互转换的方式，如果不兼容，则无法相互转换，编译会报错,通常写法是 a(b),把b转换成a

**类型断言**是在接口之间进行，本质也是类型转换，写法是a.(b),含义是把a转换成b

如下代码，做一些错误的和正确的示范

```go
//这个转换时类型不同，也不兼容，所以编译报错
s := "ab"
i := int(s)

//这个转换类型不同，但兼容，所以OK
var j int8 = 1
m := int(j)

//这个转换是失败的，系统会检测到类型不匹配，直接panic
var k interface{} = "s"
l := k.(int)
//但我们可以通过一个参数来判断,只有f为true时，才会转换成功
l,f := k.(int)
//这个转换是成功的
p,f := k.(string)
```

#### 类型转换的实践，勤加练习才能理解

##### 数字类型之间转换

从低位转高位没有什么问题，从高位转低位时(会丢失精度)，int64转int8，这个转换的过程如下：
128的二进制：.........00000000_**1**0000000
因为是从int64转int8，所以截取128的后八位 ：**1**0000000
此时最高位是1，表示这是一个负数，此时结果是就是：-128

```go
//这个转换没有任何问题，都OK
var i int8 = 123
var j int16 = int16(i)
//这个转换会丢失精度，从高位转低位
var m int64 = 128
var n int8 = int8(m) //n的结果是-128，因为int8能表达的最大值是127，最小值是-128，
```

##### 字符串，字节，数字，字符互相转换

```go
var s1,s2 string = "AbcD","1234"
//转字节
bs1 := []byte(s1); bs2 := []byte(s2)

//字节数组转字符串
s11 := string(bs1); s22 := string(bs2)
//单个字节转字符串
ss := string(bs1[0])
fmt.Println(s11, s22, ss)

//s2转数字 ,err 表示是否能转换成功，比如s1就会转换失败
i, err := strconv.Atoi(s2)
//数字转字符串
s := strconv.Itoa(i)

//字符串转字符数组
runes := []rune(s1)

//字符数组转字符串
ss1 := string(runes)
//单个字符转字符串
ss2 := strconv.QuoteRune(runes[0])

//字符转字节
bss := make([]byte, 0)
bss = strconv.AppendQuoteRune(bss, runes[0])
fmt.Println(err, s, ss1, ss2, runes[0], bss, string(bss))
//除开rune和byte底层的类型的区别，在使用上，
//rune能处理一切的字符，而byte仅仅局限在ascii

//整形转字节
x := int32(68)
bytesBuffer := bytes.NewBuffer([]byte{})
binary.Write(bytesBuffer, binary.BigEndian, x)
//字节转整形
var y int32
binary.Read(bytesBuffer, binary.BigEndian, &y)
```

##### 接口到具体类型的转换

```go
//由接口类型转换为具体的类型
var i interface{} = 1
t, f := i.(int)
if f { //转换成功
   fmt.Println(t)
} else {//转换失败
   fmt.Println(reflect.TypeOf(i).Kind(), reflect.TypeOf(i))
}
```