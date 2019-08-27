[示例](http://huaiyu.loganlin.top)

# 特点

- 直观的管理后台，无需任何编程知识即可完全自定义内容
- 使用Docker轻松部署

# 使用方法

初次运行时，在安装有docker-ce的服务器上执行命令行代码：

    bash build.sh <附加ID> <服务端口号>

将自动构建docker image，并启动名为`scholar_index_<附加ID>`的容器。此时访问`localhost:<服务端口号>`应该能够看到页面。

页面底端有`Admin`链接可进入管理后台。初始密码为`admin`，进入后台后可重设密码。

# 特别声明

- 使用了[MDUI](https://www.mdui.org)前端框架。