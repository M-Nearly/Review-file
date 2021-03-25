

## Python操作上传下载



### sdk 方便

<https://cloud.tencent.com/document/product/436/12269>

#### 使用 pip 安装（推荐）

```sh
pip install -U cos-python-sdk-v5
```





#### 初始化

``` python
# -*- coding=utf-8
# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 BucketName-APPID 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
# import logging
# logging.basicConfig(level=logging.INFO, stream=sys.stdout)


secret_id = 'COS_SECRETID'      # 替换为用户的 secretId
secret_key = 'COS_SECRETKEY'      # 替换为用户的 secretKey

region = 'COS_REGION'     # 替换为用户的 Region  桶的区域 ap-nanjing

token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)
# 参照下文的描述。或者参照 Demo 程序，详见 https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py
```

----

我的信息

secret_id = 'AKIDMUM0RdMIk6C2eHftqYDmBPedWFicNyHN'      # 替换为用户的 secretId
secret_key = 'ziXAWZy8JJ2UlmWzGk160LVQ7YiiUXOy'      # 替换为用户的 secretKey

region = "ap-nanjing"

AppID= "1256150061"

#### 创建存储桶

```python
response = client.create_bucket(
   Bucket='examplebucket-1250000000' # 桶名称
   ...
)

--- 
可以添加其他选项
ACL="public-read" 		# 'private'|'public-read'|'public-read-write',  # 桶的选项


---
后期还可以修改桶的信息
config = {
    ...
}
```



##### 注意

`qcloud_cos.cos_exception.CosServiceError: {'code': 'AccessDenied', 'message': 'Access Denied.', 'resource': 'dsadsad-212312321.cos.ap-nanjing.myqcloud.com', 'requestid': 'NjA1MmQ3NDBfMjk1NGU0MDlfMjMzOGFfOTVhZTZkZQ==', 'traceid': 'OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODc0OWRkZjk0ZDM1NmI1M2E2MTRlY2MzZDhmNmI5MWI1OTA2NzIxMzRkNDExNDJiYWZmM2ExNTVhMjIxMzhjNDI2ZmI2NmEzODlhMGIxMzFlYWZkYWY4ODQ3NTZiZDcyMDg='}`

创建桶名称是 -数字  这个数字是你的appID 



#### 查询存储桶列表

```python
response = client.list_buckets(
)
```

#### 上传文件

``` python
#### 高级上传接口（推荐）
# 根据文件大小自动选择简单上传或分块上传，分块上传具备断点续传功能。
response = client.upload_file(
   Bucket='meng-1256150061',
   # LocalFilePath='local.txt', # 要上传本地文件的路径
   Key='picture.jpg',  			# 上传到桶之后的文件名
   PartSize=1,     				# 后面三个可传可省略
   MAXThread=10,
   EnableMD5=False
)
print(response['ETag'])


```





