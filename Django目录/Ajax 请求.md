# django 与 Ajax

## 什么是ajax
> AJAX（Asynchronous Javascript And XML）翻译成中文就是“异步Javascript和XML”。即使用Javascript语言与服务器进行异步交互，传输的数据为XML（当然，传输的数据不只是XML,现在更多使用json数据）。

- 同步交互.客户端发出一个请求后,需要等待服务器响应结束后,才能发出第二个请求
- 异步交互,客户端发出一个请求后,无需等待服务器响应结束,就可以发出第二个请求

AJAX除了异步的特点外,还有一个就是浏览器页面的局部刷新

## 基于jQuery的Ajax的实现
``` JavaScript

<button class="send_Ajax">send_Ajax</button>
<script>

       $(".send_Ajax").click(function(){

           $.ajax({
               url:"/handle_Ajax/",
               type:"POST",
               data:{username:"Yuan",password:123},
               success:function(data){
                   console.log(data)
               },
         　　　　　　
               error: function (jqXHR, textStatus, err) {
                        console.log(arguments);
                    },

               complete: function (jqXHR, textStatus) {
                        console.log(textStatus);
                },

               statusCode: {
                    '403': function (jqXHR, textStatus, err) {
                          console.log(arguments);
                     },

                    '400': function (jqXHR, textStatus, err) {
                        console.log(arguments);
                    }
                }

           })

       })

</script>
```
