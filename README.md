# SearchEngine
上接爬虫项目[FirstSpider](https://github.com/yipwinghong/FirstSpider)
 
爬取伯乐在线、知乎和拉勾网的信息，把数据写入ElasticSearch后，使用Django实现搜索网站的搭建。
 
在项目中查询结果分页的逻辑已改用模板语言控制。
 
## 运行效果
![SearchEngine](https://github.com/yipwinghong/SearchEngine/blob/master/Screenshots/SearchEngine.gif)
 
## 开发环境
环境 | 版本
---|---
开发语言 | Python 3.5.3
后端框架 | Django 1.11
搜索引擎 | ElasticSearch 5.1.1
IDE | PyCharm 2017.1 x64


## 使用方法

 1、安装环境依赖包（不同版本操作系统安装方法有差异，见网上具体解决方案）：<pre><code>pip install -r requirements.txt</code></pre>

 2、下载ElasticSearch-rtf 5.1.1
 其中启动前需要修改配置文件config/elasticsearch.yml：
 <pre><code>http.cors.enabled: true
http.cors.allow-origin: "*"
http.cors.allow-methods: OPTIONS, HEAD, GET, POST, PUT, DELETE
http.cors.allow-headers: "X-Requested-With, Content-Type, Content-Length, X-User"
</code></pre>
 
 3、使用FirstSpider的爬虫爬取数据并写入ES，数据管理可以使用Elasticsearch-head（具体使用方法见官方文档）：
 ![Alt text](https://github.com/yipwinghong/SearchEngine/blob/master/Screenshots/1.jpg)
 ![Alt text](https://github.com/yipwinghong/SearchEngine/blob/master/Screenshots/2.jpg)
 
 4、项目目录下运行：<pre><code>python manage.py runserver</code></pre>

 5、浏览器下访问：<pre><code>127.0.0.1:8000</code></pre>
 ![Alt text](https://github.com/yipwinghong/SearchEngine/blob/master/Screenshots/3.jpg)
 ![Alt text](https://github.com/yipwinghong/SearchEngine/blob/master/Screenshots/4.jpg)
