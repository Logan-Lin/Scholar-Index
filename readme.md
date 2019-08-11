# 学者首页框架

## [示例](http://loganlin.top:8080)

## 特点

- 仅需修改JSON文件和Markdown文件即可实现内容的更新
- 使用Docker轻松部署

## 使用方法

姓名、网页标题、论文列表等信息存储在`/index_app/static/data/data.json`文件中。个人照片的位置由`photo`字段指定。

大段的文本内容，如个人简介、研究兴趣、新闻、获奖列表等存储在`/index_app/static/markdown`文件夹下的Markdown文件中。新闻和获奖内容的Markdown需要注意一下格式。

初次运行时，在安装有docker-ce的服务器上执行命令行代码：

    bash build.sh

将自动构建docker image，并启动名为`scholar_index`的容器。

修改内容后，需要更新页面，只需在命令行中运行：

    docker container restart scholar_index

即可。

## 特别声明

- 使用了[MDUI](https://www.mdui.org)前端框架。
- 示例内容摘自[魏云超博士的学者首页](https://weiyc.github.io/)。