## this 

每个函数都是一个作用域, 在他的内部都会存在this, 谁调用的函数, 那么this就是谁

``` javascript
function func(){
    var name = "111"
    console.log(name)  // 111
}
func()  // func() = window.func()

----

var name = "111"
function func(){
    var name = "222"
    console.log(this.name)  // 111
}
func() // func() = window.func()

----

var name = 111
info = {
    name: "222",
    func: function (){
        console.log(this.name) // 222  this = info
    }
}
info.func()
// 总结: 每个函数都是一个作用域, 在他的内部都会存在this, 谁调用的函数, 那么this就是谁
----

var name = "111"
info = {
    name: "222",
    func: function (){
        console.log(this.name) // 222  info.name
        function test(){
            console.log(this.name) 
        }
        test() // 如果没有前缀 那就是window.test()  111
    }
}
info.func()
----

var name = "111"
info = {
    name: "222",
    func: function (){
        var that = this;
        function test(){
            console.log(that.name)  // 222 info.name
        }
        test()
    }
}
info.func()

```

