

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


## 配置消息弹框的效果

1. 在`plugins` 的`element.js` 中导入`Message`组件

2. 挂载Vue下,设置全局组件

   `Vue.prototype.$message = Message`

![1579056933075](assets/1579056933075.png)



## 把`token` 放到`sessionStroage` 中

``` html
// 1. 将登录成功之后的token,保存到客户端的sessionStorage 中
// 1.1 项目中除了登录之外的其他API接口,必须在登录之后才能访问
// 1.2 token 只应在当前网站打开期间生效, 所有将token保存在sessionStorage中
window.sessionStorage.setItem('token', res.token)
// 2. 通过编程式导航跳转到后台主页, 路由地址是/hone
this.$router.push('/home')
```



## 登录 - 路由导航守卫控制权限

![1579058951212](assets/1579058951212.png)

`router.js`

``` javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/components/Login.vue'
import Home from '@/components/Home.vue'

Vue.use(VueRouter)

/*
const router = new VueRouter({
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', redirect: Login },
    { path: '/home', redirect: Home }
  ]
})

// 挂载路由导航守卫
router.beforeEach((to, from, next) => {
  // to 将要访问的路径
  // from 代表从哪个路径跳转而来
  // next 是一个函数, 表示方形
  // next() 放行, next('/login')  强制跳转到url
  if (to.path === '/login') return next()
  // 获取token
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  next()
})

export default router
*/

const routes = [
  {
    redirect: '/login',
    path: '/'
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/Home',
    component: Home
  }
]

const router = new VueRouter({
  routes
})

// 挂载路由导航守卫
router.beforeEach((to, from, next) => {
  // to 将要访问的路径
  // from 代表从哪个路径跳转而来
  // next 是一个函数, 表示方形
  // next() 放行, next('/login')  强制跳转到url
  if (to.path === '/login') return next()
  // 获取token
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  next()
})

export default router

```



## 退出

清空 token .

![1579067462538](assets/1579067462538.png)



## 解决语法错误

1. 不能使用双引号
2. 默认后面要添加分号

新添加文件

![1579068697843](assets/1579068697843.png)



函数名后面必须要添加空格

![1579068753917](assets/1579068753917.png)



# 主页布局

![1579069763391](assets/1579069763391.png)



## 使用element-ui 的container 布局要先导入

![1579070613223](assets/1579070613223.png)



## 左侧菜单

![1579071115677](assets/1579071115677.png)



![1579071822146](assets/1579071822146.png)



请求必须携带token, 预处理过程.



![1579072228477](assets/1579072228477.png)

main.js

添加请求头.`headers.Authorization`

``` javascript
import axios from 'axios'
//
import '@/assets/css/global.css'

axios.defaults.baseURL = 'http://127.0.0.1:8888/api/private/v1'
axios.interceptors.request.use(config => {
  // console.log(config)
  config.headers.Authorization = window.sessionStorage.getItem('token')
  return config
})
Vue.prototype.$http = axios
```





