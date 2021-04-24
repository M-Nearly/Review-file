## 富文本编辑器

ckeditor









## markdown 编辑器 

mdetior

mdeditor 文件编辑插件

<https://github.com/pandao/editor.md>

<https://pandao.github.io/editor.md/examples/index.html>

<https://www.mdeditor.net/>

### 使编辑框变成markdown编辑框

1. textare 框通过div包裹

   `<div id="editor">   </div>`

2. 导入js和css

   `{% load  static %}` 

   `<link rel="stylesheet" href="{% static 'plugin/editor-md/css/editormd.min.css' %}">`

   `<script src="{% static 'plugin/editor-md/editormd.min.js' %}"> </script>`

3. 初始化

   ``` html
   <script>
       $(function () { 
           initEditor();
       });
   // Markdown 编辑器
       function initEditor(){
           editormd("editor",{
               placeholder:"请输入内容",
               height:500,
               path:"{% static 'plugin/editor-md/lib/' %}"  // lib依赖文件的位置
           })
       }
       
     </script>
   
   ```

   ​	全屏显示问题解决

   ``` html
   <style>
   	.editormd-fullscreen {
       	        z-index: 1001;
   	}
   </style>
   ```

### 预览窗口变成markdown格式的

1. 内容区域 包裹起来

   ```html
   <div id="previewMarkdown">
       <textarea>
           {{ wiki_object.content }}
       </textarea>
   </div>
   
   ```

2. 引入css 引入js

   ``` html
       <link rel="stylesheet" href="{% static 'plugin/editor-md/css/editormd.preview.min.css' %}">
   
   
       <script src="{% static 'plugin/editor-md/editormd.min.js' %}"></script>
       <script src="{% static 'plugin/editor-md/lib/jquery.flowchart.min.js' %}"></script>
       <script src="{% static 'plugin/editor-md/lib/flowchart.min.js' %}"></script>
       <script src="{% static 'plugin/editor-md/lib/marked.min.js' %}"></script>
       <script src="{% static 'plugin/editor-md/lib/prettify.min.js' %}"></script>
       <script src="{% static 'plugin/editor-md/lib/raphael.min.js' %}"></script>
       <script src="{% static 'plugin/editor-md/lib/sequence-diagram.min.js' %}"></script>
       <script src="{% static 'plugin/editor-md/lib/underscore.min.js' %}"></script>
   
   
   
   ```

3. 初始化

   ``` html
   <script>
   // Markdown
           function initPreviewMarkdown(){
               editormd.markdownToHTML("previewMarkdown",{
                   htmlDecode:"style,script,iframe",  // 过滤这些内容
               });
           }
   </script>
   ```

4. 更多参数 查看例子 官网等

   

   

### 通过 markdown 组件进行上传图片功能

使用腾讯的cos

接收markdown上传的文件在上传到cos

- markdown上传图片

  Html

  ```javascript
  {
      imageUpload    : false,
      imageFormats   : ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
      imageUploadURL : "./php/upload.php",
  }
  ```

  JSON data

  ```json
  {
      success : 0 | 1,           // 0 表示上传失败，1 表示上传成功
      message : "提示的信息，上传成功或上传失败及错误信息等。",
      url     : "图片地址"        // 上传成功时才返回
  }
  ```



##### django中使用如果不显示 查看console页面,.`mdeditor in a frame because it set 'X-Frame-Options' to 'deny'.

`<https://blog.csdn.net/weixin_41861301/article/details/111691039>`

``` python
Refused to display 'url' in a frame because it set 'X-Frame-Options' to 'deny'根据提示信息发现是因为X-Frame-Options=deny导致的。


from django.views.decorators.clickjacking import xframe_options_exempt

给函数添加上装饰器
@xframe_options_exempt
@csrf_exempt



```









​		


​	

​	

