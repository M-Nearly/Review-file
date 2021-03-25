


- 文件夹 
- 文件

知识点:
    1. 模态对话框 & ajax & form校验
        2. 目录切换 : 展示当前的文件夹&文件 是否有目录的id
        3. 删除 -> 嵌套的文件和文件夹都要删除
        4. js上传文件到腾讯的cos(之前是Python向cos上传)
        5. 删除文件
        - 本地数据库删除
        - cos中文件也需要删除
        6. 上传进度条操作
        7. 下载文件

----
    - 设计   
    - 表结构
    - 单独知识点





表结构

| ID   | 项目ID     | 文件 <br/>文件夹    | 类型    | 大小     | 父目录     | key  |  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | 22 | 文件名 | 2 | null | null | null |  |
| 2 | 22 | 12.png | 1 | 1000 | null | 32132132.png |  |
| 3 | 22 | 12.png           | 1 | 1221 | 1 | dsaqw.png |  |

- key 是文件的别名 防止文件名称冲突 自定义的文件名用于区别存储
- 类型: 1-> 文件 / 2-> 文件夹



URL 设计

- URL 传参 / 不传参

  `re_path("^file/", manage.file, name="file"),`  

  ``` Python
  可以通过get传参
  # /file/
  # /file/?folder_id=40
  def file(request,project):
      folder_id = request.GET.get("folder_id"," ")
  
  ```

- 模态对话框

  bootstrap 中 模态框 嵌套 警告框

- 获取导航条

  ``` python
  可以通过get传参
  # /file/
  # /file/?folder_id=40
  def file(request,project):
      folder_id = request.GET.get("folder_id"," ")
  	url_list = []
      if not folder_id:
          pass
      else:
          file_object = models.FileReplsitory.object.filter(id=folder_id,file_type=2).first()
          # 找到父级目录
          # 循环找父级
          row_object = file_object 
          while row_object :
              url_list.insert(0, row_object.name )
              row_object = row_object.parent
          
          
          
  ```

  

## cos 上传文件: 

- Python可以直接上传文件 COS的API / SDK

- 使用 JS上传文件

  1. 使用秘钥直接上传  (不推荐 秘钥直接展示不安全)

     参考COS文档 `<https://cloud.tencent.com/document/product/436/11459>`

     ``` html
     1. 下载JS (前端的SDK)
        下载地址 https://github.com/tencentyun/cos-js-sdk-v5/blob/master/dist/cos-js-sdk-v5.min.js
     2. 引入
     	<script src="https://unpkg.com/cos-js-sdk-v5/dist/cos-js-sdk-v5.min.js"></script>
     3. 前端
     	<input id="file-selector" type="file" id="iploadFile" name="upload_file" multiple /> <!-multiple多选 ->
     	<script src="dist/cos-js-sdk-v5.min.js"></script>
     	<script src="juqery-3.4.1.min.js"></script>
     
         <script>
             var cos;
             var Bucket = 'examplebucket-1250000000';
             var Region = 'COS_REGION';     /* 存储桶所在地域，必须字段 */
             $(function(){
                 initCOS();
                 bindChangeFileInput()
             })
             
             function initCOS(){
                 var cos = new COS({
                    SecretId: 'COS_SECRETID',
                    SecretKey: 'COS_SECRETKEY',
             	});
             }
             
             function bindChangeFileInput(){
                 $("#uploadFIle").change(function () {
                     // 获取要上传的所有文件对象列表
                     // $(this)[0] 的意思是把jquery对象转成 dom 对象
                     // $(this)[0] = document.getElementById("uploadFile")
                     var files = $(this)[0].files;
                     $.each(files, function (index,fileObject){
                         var fileName = fileObject.name
                         // 上传文件 putObject操作为异步  $.each 已经处理了不然就自己用闭包解决
                         // 如果是JavaScript 就需要自己写闭包
                         cos.putObject({
                             Bucket: " ", /* 必须*/
                             Region: " ", /* 存储桶所在的区域,必须*/
                             Key: fileName, /*必须*/
                             StorageClass: "STANDARD", /*上传的标注*/
                             Body:fileObject, // 上传文件的对象
                             onProgress:function (progressData){
                                 console.log("文件上传进度--							          >",fileName,JSON.stringify(progressData))
                             }
                         },function (err,data){
                                 // 是否上传COS成功 ? 
                            		console.log("err||data")
                             }
                     );
                 })
             })
             }
         </script>
     4. 解决跨域的问题. 针对桶的设置, 需要在cos的后端设置CORS (桶的基础配置-> 安全管理)
     
     
     ```

  2. 使用临时秘钥上传 (推荐)

     1.  路由

       ``` django
       re_path("^file/", manage.demo2, name="file")
       re_path("^cos/credential/", manage.cos_credential, name="cos_credential")
       ```

     2. 视图

        ``` python
        # 获取页面的视图
        def demo2(request):
        	return render(request, "demo2.html")
        
        # 获取临时凭证的视图
        def cos_credential(request):
            # 生成一个临时凭证, 并给前端返回
            # 1. 安装一个生成临时凭证的模块
            # pip install -U qcloud-python-sts
            # 2. 写代码
            from sts.sts import Sts
            congfig = {
                # 获取秘钥有效时长, 单位是秒 (30分钟= 1800秒)
                'duration_seconds': 1800,
                # 自己的 secret_id
                'secret_id': "AKIDFPISXQEKBPXVL3TX5zf6MSLOSF7Qoikg",
                # 自己的 secret_key
                'secret_key': "yicwfzCxcQx1Z1gncKvRuSDKHySg8sMp",
                # 换成你的 bucket
                'bucket': "wangyang-1251317460",
                # 换成你bucket 所在区域
                'region': "ap-chengdu",
                # 这里改成允许的路径前缀, 可以根据自己网站的用户登录态判断允许上传的具体路径
                # 例子 a.jpg 或者 a/* 或者 * (使用通配符*存在重大安全风险, 请谨慎评估使用)
                'allow_prefix': "*",
                # 秘钥的权限列表. 简单上传和分片需要以下的权限, 其他权限列表请看https://cloud. tencent.com/document/product/436/31923
                'allow_actions': [
                    # 简单上传
                    # 'name/cos:PutObject',
                    # 表单上传对象
                    'name/cos:Postobject’,
                    # ....
                    # 'name/cos:Deleteobject’,
                    # "name/cos:uploadpart”,
                    # "name/cos:UploadPartcopy”,
                    # "name/cos:Completemultipartupload”,
                    # "name/cos:AbourtMultipartUpload",
                    # 所有操作都支持
                    "*",
                ]
            }
            sts = Sts(config)
            result_dict = sts.get_credential()
            return JsonResponse(result_dict)
        
        ```

     3. 页面

        ``` html
        	<script src="dist/cos-js-sdk-v5.min.js"></script>
        	<script src="juqery-3.4.1.min.js"></script>
        
            <script>
                var cos;
                var Bucket = 'examplebucket-1250000000';
                var Region = 'COS_REGION';     /* 存储桶所在地域，必须字段 */
                $(function(){
                    initCOS();
                    bindChangeFileInput()
                })
                
                function initCOS(){
                    var cos = new COS({
                        getAuthorization: function (options, callback){
                            // 像django后台发送请求, 获取临时凭证
                            // $.get  = $.ajax({ type:"GET"})
                            $.get("/cos/credential", {
                                // 可从 options 取所需的参数
                            }, function (data){
                                var credentials = data && data.credentials ;
                                if (!data || !creadentials ) return console.log("credentials invalid ");
                                callback({
                                    TmpSecreId: credentials.tmpSecretId,
                                    TmpsecretKey: credentials.tmpSecretKey,
                                    XCosSecurityTokey: credentials.sessionToken,
                                    // 建议返回服务器时间作为签名的开始时间，避免用户浏览器本地时间偏差过大导致签名错
                                    StartTime: data.startTime, // 时间戳，单位秒
                                    ExpiredTime: data.expriedTime // 时间戳，单位秒
                                });
                            });
                        }
                	});
                }
                
                function bindChangeFileInput(){
                    $("#uploadFIle").change(function () {
                        // 获取要上传的所有文件对象列表
                        // $(this)[0] 的意思是把jquery对象转成 dom 对象
                        // $(this)[0] = document.getElementById("uploadFile")
                        var files = $(this)[0].files;
                        $.each(files, function (index,fileObject){
                            var fileName = fileObject.name
                            // 上传文件
                            cos.putObject({
                                Bucket: " ", /* 必须*/
                                Region: " ", /* 存储桶所在的区域,必须*/
                                Key: fileName, /*必须*/
                                StorageClass: "STANDARD", /*上传的标注*/
                                Body:fileObject, // 上传文件的对象
                                onProgress:function (progressData){
                                    console.log("文件上传进度--							          >",fileName,JSON.stringify(progressData))
                                }
                            },function (err,data){
                                    // 是否上传COS成功 ? 
                               		console.log("err||data")
                                }
                        );
                    })
                })
                }
            </script>
        
        ```

        

     4. 跨域问题,与上相同 (桶的基本配置)


​     

### COS中代码添加cors 设置

``` python
# 创建bucket 中添加core config
from qcloud_cos import CosConfig
from qcloud_cos import CsoS3Client
from django.conf import settings

def create_bucket(bucket, region="ap-nanjing"):
    """
    创建桶
    :param bucket: 桶名称
    :param region: 区域 ap-nanjing
    :return:
    """
    config = CosConfig(Region=region, Secret_id=settings.TENCENT_COS_ID, Secret_key=settings.TENCENT_COS_KEY)
    client = CosS3Client(config)
    client.create_bucket(
        Bucket=bucket,
        ACL="public-read",
    )
    
    cors_config = {
        "CORSRule":[
            {
                "AllowedOrigin": "*" ,
                "AllowedMethod": ["GET", "PUT", "HEAD", "POST", "DELETE"],
                "AllowedHeader": "*" , # ["x-cos-meta-test"]
                "EXposeHeader": "*", # 
                "MaxAgeSeconds": 500 # 缓存 超时时间
            }
        ]
    }
    client.put_bucket_core(
    	Bucket=bucket,
        CORSConfiguration=core_config
    )
    
```







