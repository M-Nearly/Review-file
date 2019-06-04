接受web请求并返回web相应


from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect

request属性

	django 将请求报文中的请求行,首部信息,内容主题 封装成HttpReq类中的属性.

		HttpReq.GET
			包含 HTTP GET 的所有参数
		HttpReq.POST
			包含 HTTP POST 的所有参数 
			if request.method == 'POST':
			文件上传 request.FILES 中
			request.list

		HttpRequ.body
			代表请求报文的主体.在处理非http形式的报文非常有用


		HttpRequest.path
			请求的路径(不包含域名)
	　　		例如："/music/bands/the_beatles/"

		HttpRequest.method	
			 http的请求方法,必须大写

		 HttpRequest.encoding
		 	标识提交的数据的编码方式,默认为 'utf-8'

	 	HttpRequest.META
		 　　一个标准的Python 字典，包含所有的HTTP 首部。具体的头部信息取决于客户端和服务器，下面是一些示例：
		　　取值：

		    CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
		    CONTENT_TYPE —— 请求的正文的MIME 类型。
		    HTTP_ACCEPT —— 响应可接收的Content-Type。
		    HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
		    HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
		    HTTP_HOST —— 客服端发送的HTTP Host 头部。
		    HTTP_REFERER —— Referring 页面。
		    HTTP_USER_AGENT —— 客户端的user-agent 字符串。
		    QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
		    REMOTE_ADDR —— 客户端的IP 地址。
		    REMOTE_HOST —— 客户端的主机名。
		    REMOTE_USER —— 服务器认证后的用户。
		    REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。
		    SERVER_NAME —— 服务器的主机名。
		    SERVER_PORT —— 服务器的端口（是一个字符串）。
		 　　从上面可以看到，除 CONTENT_LENGTH 和 CONTENT_TYPE 之外，请求中的任何 HTTP 首部转换为 META 的键时，
		    都会将所有字母大写并将连接符替换为下划线最后加上 HTTP_  前缀。
		    所以，一个叫做 X-Bender 的头部将转换成 META 中的 HTTP_X_BENDER 键。

	    HttpRequest.FILES 
	    	包含所有的上传文件信息
    	    FILES 中的每个键为<input type="file" name="" /> 中的name，值则为对应的数据。
			　　注意，FILES 只有在请求的方法为POST 且提交的<form> 带有enctype="multipart/form-data" 的情况下才会
			   包含数据。否则，FILES 将为一个空的类似于字典的对象。

	   	HttpRequest.COOKIES
	   		包含所有的cookie, 键值都为字符串

   		HttpRequest.session
   			表示当前的会话


		HttpRequest.user(用户认证组件使用)
			　　一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户。

			　　如果用户当前没有登录，user 将设置为 django.contrib.auth.models.AnonymousUser 的一个实例。你可以通过 is_authenticated() 区分它们。

			    例如：

			    if request.user.is_authenticated():
			        # Do something for logged-in users.
			    else:
			        # Do something for anonymous users.


			     　　user 只有当Django 启用 AuthenticationMiddleware 中间件时才可用。

			     -------------------------------------------------------------------------------------

			    匿名用户
			    class models.AnonymousUser

			    django.contrib.auth.models.AnonymousUser 类实现了django.contrib.auth.models.User 接口，但具有下面几个不同点：

			    id 永远为None。
			    username 永远为空字符串。
			    get_username() 永远返回空字符串。
			    is_staff 和 is_superuser 永远为False。
			    is_active 永远为 False。
			    groups 和 user_permissions 永远为空。
			    is_anonymous() 返回True 而不是False。
			    is_authenticated() 返回False 而不是True。
			    set_password()、check_password()、save() 和delete() 引发 NotImplementedError。
			    New in Django 1.8:
			    新增 AnonymousUser.get_username() 以更好地模拟 django.contrib.auth.models.User



request 常用方法
	'''
	1.HttpRequest.get_full_path()
	　　返回 path，如果可以将加上查询字符串。

	　　例如："/music/bands/the_beatles/?print=true"
	　　注意和path的区别：http://127.0.0.1:8001/order/?name=lqz&age=10

	2.HttpRequest.is_ajax()

	　　如果请求是通过XMLHttpRequest 发起的，则返回True，方法是检查 HTTP_X_REQUESTED_WITH 相应的首部是否是字符串'XMLHttpRequest'。

	　　大部分现代的 JavaScript 库都会发送这个头部。如果你编写自己的 XMLHttpRequest 调用（在浏览器端），你必须手工设置这个值来让 is_ajax() 可以工作。

	　　如果一个响应需要根据请求是否是通过AJAX 发起的，并且你正在使用某种形式的缓存例如Django 的 cache middleware，
	   你应该使用 vary_on_headers('HTTP_X_REQUESTED_WITH') 装饰你的视图以让响应能够正确地缓存。

	'''



3 HttpResponse对象
	响应对象主要有三种方式
	- HttpResponse()  直接括号内添加字符串做为响应体
	- render()
	- redirect()


- render()
render(request, template_name[, context]）
	结合一个给定的模板和一个给定的上下文字典，并返回一个渲染后的 HttpResponse 对象。
参数
	request: 用于生成响应的请求对象
	templa_name: 要使用的模板的完整名称,可选的参数
	context: 像前端返回的值

render 方法就是将一个模板页面中的模板语法进行渲染,最终渲染成一个html页面做为响应体


redirect()
传递要重定向的一个硬编码的URL

	传递要重定向的一个硬编码的URL

	def my_view(request):
	    ...
	    return redirect('/some/url/')

	也可以是一个完整的URL：
	def my_view(request):
	    ...
	    return redirect('http://www.baidu.com/')　

---------
1）301和302的区别。

　　301和302状态码都表示重定向，就是说浏览器在拿到服务器返回的这个状态码后会自动跳转到一个新的URL地址，这个地址可以从响应的Location首部中获取
  （用户看到的效果就是他输入的地址A瞬间变成了另一个地址B）——这是它们的共同点。

　　他们的不同在于。301表示旧地址A的资源已经被永久地移除了（这个资源不可访问了），搜索引擎在抓取新内容的同时也将旧的网址交换为重定向之后的网址；

　　302表示旧地址A的资源还在（仍然可以访问），这个重定向只是临时地从旧地址A跳转到地址B，搜索引擎会抓取新的内容而保存旧的网址。 SEO302好于301

 

2）重定向原因：
（1）网站调整（如改变网页目录结构）；
（2）网页被移到一个新地址；
（3）网页扩展名改变(如应用需要把.php改成.Html或.shtml)。
        这种情况下，如果不做重定向，则用户收藏夹或搜索引擎数据库中旧地址只能让访问客户得到一个404页面错误信息，访问流量白白丧失；再者某些注册了多个域名的
    网站，也需要通过重定向让访问这些域名的用户自动跳转到主站点等
------


JsonResponse
向前端返回一个json格式字符串的两种方式
    # 第一种方式
    # import json
    # data={'name':'lqz','age':18}
    # data1=['lqz','egon']
    # return HttpResponse(json.dumps(data1))

    # 第二种方式
    from django.http import JsonResponse
    # data = {'name': 'lqz', 'age': 18}
    data1 = ['lqz', 'egon']
    # return JsonResponse(data)
    return JsonResponse(data1,safe=False)




CBV和FBV

CBV基于类的视图(Class base view)和FBV基于函数的视图（Function base view）

from django.views import View
class AddPublish(View):
    def dispatch(self, request, *args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
        # 可以写类似装饰器的东西，在前后加代码
        obj=super().dispatch(request, *args, **kwargs)
        return obj

    def get(self,request):
        return render(request,'index.html')
    def post(self,request):
        request
        return HttpResponse('post')







简单的文件上传

    print(request.FILES)
    print(type(request.FILES.get('file_name')))

    file_name=request.FILES.get('file_name').name
    from django.core.files.uploadedfile import InMemoryUploadedFile
    with open(file_name,'wb')as f:
        for i in request.FILES.get('file_name').chunks():
            f.write(i)