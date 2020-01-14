

[视频地址](<https://www.bilibili.com/video/av74592164?p=22>)

## vue_shop

1. 终端vue ui 打开web界面 
2. 创建项目. 参见<https://www.bilibili.com/video/av74592164?p=5>
3. 插件 ->  添加插件 -> element
4. 依赖 -> 安装依赖 -> 运行依赖 axios



源码链接https://pan.baidu.com/s/1z60ej714UHIZqFL4lzjIpg 里面有两个项目源码，这套视频用的“20-21vue  

  17-21 Vue.js项目实战开发\20-21vue电商\3.vue-项目实战day1\素材里面有个压缩包







## 前端项目初始化步骤

1. 安装vue 脚手架
2. 通过vue脚手架创建项目
3. 配置vue路由
4. 配置emement-ui组件库
5. 配置axios库
6. 初始化git远程仓库
7. 将本地项目托管到github





## token

![1578900457993](assets/1578900457993.png)



## 登录

![1578900572290](assets/1578900572290.png)



``` vue
// 路由重定向
const routes = [
  {
    path: '/',
    redirect: '/login'

  },
  {
    path: '/login',
    component: Login
  }
]

// 路由占位符
<router-view></router-view>
```







## login

###  为表单添加验证

1. 为form 加一个rules

   ` <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">`

2. 在data中添加规则

   ``` html
           rules: {
             name: [
               { required: true, message: '请输入活动名称', trigger: 'blur' },
               { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
             ],
             region: [
               { required: true, message: '请选择活动区域', trigger: 'change' }
             ],
             date1: [
               { type: 'date', required: true, message: '请选择日期', trigger: 'change' }
             ],
             date2: [
               { type: 'date', required: true, message: '请选择时间', trigger: 'change' }
             ],
             type: [
               { type: 'array', required: true, message: '请至少选择一个活动性质', trigger: 'change' }
             ],
             resource: [
               { required: true, message: '请选择活动资源', trigger: 'change' }
             ],
             desc: [
               { required: true, message: '请填写活动形式', trigger: 'blur' }
             ]
           }
   ```

3. 在 `el-form-item` 中添加`prop` 属性

   ``` html
     <el-form-item label="活动名称" prop="name">
       <el-input v-model="ruleForm.name"></el-input>
     </el-form-item>
   ```






