# search-engine
上接爬虫项目 [first-spider](https://github.com/yipwinghong/FirstSpider)：采集伯乐在线、知乎和拉勾网的数据，使用 Django 实现搜索网站的搭建，利用开源搜索引擎 ElasticSearch 完成高级搜索任务。

搜索推荐：基于 AJAX Jquery 完成前后端交互。     

在项目中查询结果分页的逻辑已改用模板语言控制。

## 运行效果
![SearchEngine](https://ywh-oss.oss-cn-shenzhen.aliyuncs.com/SearchEngine-1.gif)

## 开发环境
环境 | 版本
---|---
开发语言 | Python 3.5.3
后端框架 | Django 1.11
搜索引擎 | ElasticSearch 5.1.1
IDE | PyCharm 2017.1 x64


## 使用方法

安装环境依赖包

```shell
pip install -r requirements.txt
```

下载并安装 ElasticSearch-rtf 5.1.1（方法见最后），进入 ES 根目录，命令行下启动 ES：
```shell
./bin/elasticsearch.bat
```

使用 FirstSpider 的爬虫爬取数据并写入 ES，数据管理可以使用 Elasticsearch-head

![](https://ywh-oss.oss-cn-shenzhen.aliyuncs.com/Elasticsearch-Head.jpg)

项目目录下运行

```shell
python manage.py runserver
```

浏览器下访问

```
http://127.0.0.1:8000
```

![Alt text](https://ywh-oss.oss-cn-shenzhen.aliyuncs.com/SearchEngine.jpg)

![Alt text](https://ywh-oss.oss-cn-shenzhen.aliyuncs.com/SearchEngine-2.jpg)



## Windows 环境下使用 ElasticSearch

[ElasticSearch](https://www.elastic.co/cn/) 是一个基于 Lucene（较难使用）的搜索服务器。它提供了一个分布式多用户能力的全文搜索引擎，基于 RESTful web 接口（http 交互）。

Elasticsearch 是用 Java 开发的，并作为 Apache 许可条款下的开放源码发布，是当前流行的企业级搜索引擎。设计用于云计算中，能够达到实时搜索，稳定，可靠，快速，安装使用方便（其他搜索引擎：solr、sphinx）。      

- 随着 ELK 日志分析系统而逐渐流行；     
- 使用效果类似 NoSQL 数据库（但重点在搜索而非数据存储）。

由于 ElasticSearch 是由 Java 编写的，首先需要安装 JDK8，确保版本在 1.8 以上。        

```shell
PS C:\Users\yipwi> java -version
openjdk version "1.8.0_41"
OpenJDK Runtime Environment (build 1.8.0_41-b04)
OpenJDK Client VM (build 25.40-b25, mixed mode)
```


安装 [ElasticSearch-RTF](https://github.com/medcl/elasticsearch-rtf)（集成中文分词以及各种插件）：

```shell
git clone https://github.com/EagleChen/docker_elasticsearch_rtf.git
```

修改配置文件 `config/elasticsearch.yml`：

```yaml
http.cors.enabled: true
http.cors.allow-origin: "*"
http.cors.allow-methods: OPTIONS, HEAD, GET, POST, PUT, DELETE
http.cors.allow-headers: "X-Requested-With, Content-Type, Content-Length, X-User"
```


进入 ES 根目录，命令行下启动：
```
./bin/elasticsearch.bat
```

成功启动后在浏览器访问可见：
```
http://127.0.0.1:9200
```

```json
{
  "name" : "pcl-131",
  "cluster_name" : "es-cluster",
  "cluster_uuid" : "_vT3TNP5Sjy3gK8uhmMPug",
  "version" : {
    "number" : "6.8.7",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "c63e621",
    "build_date" : "2020-02-26T14:38:01.193138Z",
    "build_snapshot" : false,
    "lucene_version" : "7.7.2",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```



