[链接地址](https://mp.weixin.qq.com/s/Pw_a5heUgyIkuJrXF4HCVg)
**goproxy.cn**

### 使用方法
`go env-w GOPROXY=https://goproxy.cn,direct`

在Mac/linux下执行：

```bash
Copyexport GO111MODULE=on
```

Windows平台执行：

```bash
CopySET GO111MODULE=on
```

2019.6.10更新:[goproxy.cn](https://github.com/goproxy/goproxy.cn)

我们这里以`https://goproxy.cn`为例：

在Mac/linux下可以执行以下命令来设置：

```bash
Copyexport GOPROXY=https://goproxy.cn
```

Windows平台在`cmd`执行以下命令来设置：

```bash
CopySET GOPROXY="https://goproxy.cn"
```

或者在`PowerShell`中执行：

```bash
CopyC:\> $env:GOPROXY = "https://goproxy.cn"
```

