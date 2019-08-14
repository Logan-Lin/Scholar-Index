[示例](http://loganlin.top:8080)

# 特点

- 仅需修改JSON文件和Markdown文件即可实现内容的更新
- 使用Docker轻松部署

# 使用方法

姓名、网页标题、论文列表等信息存储在`/index_app/static/data/data.json`文件中。个人照片的位置由`photo`字段指定。

大段的文本内容，如个人简介、研究兴趣、新闻、获奖列表等存储在`/index_app/static/markdown`文件夹下的Markdown文件中。新闻和获奖内容的Markdown需要注意一下格式。

初次运行时，在安装有docker-ce的服务器上执行命令行代码：

    bash build.sh

将自动构建docker image，并启动名为`scholar_index`的容器。

修改内容后，需要更新页面，只需在命令行中运行：

    docker container restart scholar_index

即可。

# 详细说明

`data.json`文件存储了网站一系列的参数与元数据。

### 个人基本信息

- `title`标签代表网站的标题，此标题将显示在浏览器的标签页标题中。
- `name`标签记录了您的姓名，其中`cn_name`为中文名，`en_name`为英文名。
- `photo`标签记录了您个人照片的路径。您可以将`/index_app/static/image`文件夹下的照片替换后，将此标签的内容修改为您照片文件的名称。
- `intro-links`标签包含了您个人的相关连接，包括邮箱、谷歌学术页面等。可用于拓展任意多的链接，按照`[名称，网址]`的格式向列表中添加项目即可。

### 出版物列表

`publications`记录了您的出版物/论文。此标签下的一级字标签为出版物的分类/年份，每个类别标签下为一个列表，其中每项的格式如下：

      {
        "title": "按照'作者.论文标题.发表刊物/会议'格式排列的论文信息",
        "links": [相关链接，按照[名称，网址]的格式添加项目],
      }

其中`links`标签是非必须的。

### 内容卡片列表

除了个人基本信息卡片和出版物卡片一定会在首页显示外，其他卡片均可根据您的需求自由添加/删除。`contents`标签记录了所有额外卡片的标题、内容的存储位置和唯一ID。每项的格式如下：

    {
      "title": "卡片的标题",
      "file_name": "存储内容的Markdown文档名称，\
        所有Markdown文档均在/index_app/static/markdown文件夹下。",
      "id": "唯一ID"
    }

若您需要添加卡片，只需在`contents`标签下按照上述格式添加项目，并在`/index_app/static/markdown/`文件夹下添加对应的markdown文件作为卡片的内容即可。

# 特别声明

- 使用了[MDUI](https://www.mdui.org)前端框架。