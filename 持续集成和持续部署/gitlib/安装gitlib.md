## 下载包

​	wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ee/yum/el7/gitlab-ee-12.0.0-ee.0.el7.x86_64.rpm

安装Postfix以发送通知电子邮件，依次执行命令：

```
sudo yum install postfix
sudo systemctl enable postfix
sudo systemctl start postfix
```

安装包安装，我是把安装包下载在/usr/local/git下，直接安装：

```
rpm -i gitlab-ee-12.0.0-ee.0.el7.x86_64.rpm
```



如果出现 No match for argument: policycoreutils-python 说明版本不对 确定系统版本是不是centos8

下载centos8

https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el8/



wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el8/gitlab-ce-12.10.1-ce.0.el8.x86_64.rpm



配置url和端口号：
url配置：

执行命令：vim  /etc/gitlab/gitlab.rb 
找到 external_url 'http://gitlab.example.com'
替换成你的Linux服务器的地址比如说：external_url 'http://192.168.1.1'

端口号配置：

```
和url同一个文件，找到 # unicorn['port'] = 8080
替换成 ：unicorn['port'] = 10000 //随便一个端口号
```



重置并启动，依次执行

```
gitlab-ctl reconfigure
gitlab-ctl restart
```







## docker 安装gitlib





docker search gitlab



**1.****下载****镜像****文件**

docker pull beginor/gitlab-ce:11.0.1-ce.0



**2.创建GitLab 的配置 (etc) 、 日志 (log) 、数据 (data) 放到容器之外， 便于日后升级**

mkdir -p /data/docker/gitlab/{etc,data,log}





3.运行GitLab容器

进入/mnt/gitlab/etc目录，运行一下命令



```shell
docker run \
 -d --name gitlab-meng \
 --hostname 49.232.70.33 \
 --restart always \
 -p 8080:80 \
 -p 8443:443 \
 -v /data/gitlab/etc:/etc/gitlab \
 -v /data/gitlab/data:/var/opt/gitlab \ 
 -v /data/gitlab/log:/var/log/gitlab \
 gitlab/gitlab-ce

```
-d(–detach)：后台运行；
–name：设置容器的名字；
–hostname：服务器的ip地址。如果端口是80可以只配置IP,但如果-p 9090:9090，则hostname也需要设置成：49.232.70.33:9090
-p 9090:9090，这两个端口映射需要保持一致，如果不一致会导致无法克隆项目代码；
–hostname：设置容器内主机的名字,就是clone代码时的地址；
如果服务器ip发生了变化，导致无法pull/push代码，我们只需要通过：vi /data/docker/gitlab/etc/gitlab.rb命令编辑配置文件中的external_url,将其设置为：http://当前服务器ip,然后用：docker restart qz-gitlab(或容器ID)重启gitlab容器即可;
–restart：设置容器的重启策略，可选项： no | on-failure[:max-retries] | always | unless-stopped ；
-v(–volume)：挂载目录，形式：[HOST-DIR:]CONTAINER-DIR；

firewall-cmd --list-ports

firewall-cmd --permanent --zone=public --add-port=9090/tcp

firewall-cmd --reload





4.修改/mnt/gitlab/etc/gitlab.rb

把external_url改成部署机器的域名或者IP地址

vi /mnt/gitlab/etc/gitlab.rb

将external_url 'http://192.168.125.126'

5.修改/mnt/gitlab/data/gitlab-rails/etc/gitlab.yml

vi /mnt/gitlab/data/gitlab-rails/etc/gitlab.yml

找到关键字 * ## Web server settings *

将host的值改成映射的外部主机ip地址和端口

6.重启docker容器

先停止该容器，删掉该容器信息，重启完docke之后，重新运行GitLab容器
