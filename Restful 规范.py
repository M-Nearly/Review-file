
Restful 规范
	1. 协议
		api 与用户的通信协议,总是使用https协议
	2. 域名
		应该尽量将api部署在专用的域名之下
			https://api.example.com (会存在跨域问题)
		如果确定api很简单,不会有进一步的扩展,可以考虑放在主域名下
			https://example.org/api/
	3. 版本
		应该将api的版本号放入URL
			https://api.example.com/v1/

		另一种方法是,将版本号放在http头信息中,但是不如放在url方便和直观 (GitHub 采用这种做法)

	4. 路径
		路径又称是"终点",标识API的具体网址

		在restful 架构中,每个网址代表一种资源,所以网址中不能有动词,只能有名词,而且所用的名词往往与数据库的表格对应,

		一般来说,数据库中的表都是同种记录的"集合",所以API中的名词也应该使用复数
		例如:
			https://api.example.com/v1/zoos
			https://api.example.com/v1/animals
			https://api.example.com/v1/employees

	5. method 请求方式 7个
		常用的有下面五个
			GET（SELECT）：从服务器取出资源（一项或多项）。
			POST（CREATE）：在服务器新建一个资源。
			PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
			PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
			DELETE（DELETE）：从服务器删除资源。
		还有两个不常用
			HEAD：获取资源的元数据。
			OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的。

		例子:
			GET /zoos：列出所有动物园
			POST /zoos：新建一个动物园
			GET /zoos/ID：获取某个指定动物园的信息
			PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）
			PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）
			DELETE /zoos/ID：删除某个动物园
			GET /zoos/ID/animals：列出某个指定动物园的所有动物
			DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物
	6.过滤信息
		如果记录数量很多,服务器不可能都将它们返回给用户.API应该提供参数,过滤反馈结果

		例子:
		?limit=10：指定返回记录的数量
		?offset=10：指定返回记录的开始位置。
		?page=2&per_page=100：指定第几页，以及每页的记录数。
		?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
		?animal_type_id=1：指定筛选条件

		参数的设计允许存在冗余，即允许API路径和URL参数偶尔有重复。比如，GET /zoo/ID/animals 与 GET /animals?zoo_id=ID 的含义是相同的。

	7. 状态码
		服务器向用户返回的状态码和提示信息,常见的有以下（方括号中是该状态码对应的HTTP动词）。
		200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。
		201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
		202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
		204 NO CONTENT - [DELETE]：用户删除数据成功。
		400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
		401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
		403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
		404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
		406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
		410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
		422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
		500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。

	8. 错误处理
		如果状态码是4xx,就应该向用户返回出错信息,一般来说,返回信息的key为error,值为出错信息
		{
			'error':'Incalid API key'
		}

	9. 返回结果
		针对不同操作,服务器向用户返回的结果应该符合以下规范
		GET /collection：返回资源对象的列表（数组）
		GET /collection/resource：返回单个资源对象
		POST /collection：返回新生成的资源对象
		PUT /collection/resource：返回完整的资源对象
		PATCH /collection/resource：返回完整的资源对象
		DELETE /collection/resource：返回一个空文档

	10. Hypermedia API，RESTful API最好做到Hypermedia，即返回结果中提供链接，连向其他API方法，使得用户不查文档，也知道下一步应该做什么。

			{"link": {
			  "rel":   "collection https://www.example.com/zoos",
			  "href":  "https://api.example.com/zoos",
			  "title": "List of zoos",
			  "type":  "application/vnd.yourformat+json"
			}}
	11. 服务器向用户返回的数据尽量使用JSON格式,
