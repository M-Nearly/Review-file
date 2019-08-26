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

            //预先发送csrf值，防止出现403错误
            $.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}'}});
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



``` python
view视图函数

from django.views.generic import View
from django.db.transaction import atomic

#此处采用django内置的View视图基类，不重构视图类
class Register(View)
    #加上数据库事务，减少对数据库的影响
    @atomic
    def post(self,request)：
        username = request.POST.get('username','')
        password = request.POST.get('password','')

```



```
# serialize

            $("#MyBtn").click(function () {
                let form1 = $("#Mydata").serialize();
                console.log($("#Mydata").serialize())
                $("#MyContent").html("<p class='bg-info'> loading ... </p>")
                $.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}'}});
                $.ajax({
                    url: "{% url 'other:arreportdetail' %}",
                    type: "GET",
                    data: form1,
                    cache: false,
                    processData: false,
                    contentType: false,
                    success: function (data) {
                        $("#MyContent").html(data)

                    },
                    error:function () {
                        $("#MyContent").html("<p class='bg-danger center'> something is going wrong. pls try again !</p>")
                    }
                })
            })

            ```


```
# FormData
        $("#MySave").click(function () {
            {#$("input[name='Myfile']")#}
            let formData = new FormData()
            formData.append("file", $("input[name='Myfile']")[0].files[0]);
            formData.append("csrfmiddlewaretoken",$("[name='csrfmiddlewaretoken']").val());
            console.log("1111")
            console.log($("input[name='Myfile']")[0].files[0])
            console.log(formData)
            $.ajax({
                url: "{% url 'inventory:srfdetail' %}",
                type:"POST",
                data:formData,
                processData:false,
                contentType:false,
                success:function (data) {
                    console.log(data)
                }
            })

        })
    })

    ```


            $.ajax({
            url: '{% url "device:face" %}', //调用django服务器计算函数
            type: 'POST', //请求类型
            beforeSend:function (xhr,setting) {
                xhr.setRequestHeader("X-CSRFToken","{{ csrf_token }}");
            },
            data: formData,
            dataType: 'json', //期望获得的响应类型为json
            processData: false,
            contentType: false,
            success: function (data) {
                console.log(data)
            }


        })