# SearchEngine
上接爬虫项目[FirstSpider](https://github.com/yipwinghong/FirstSpider)：采集伯乐在线、知乎和拉勾网的数据，使用Django实现搜索网站的搭建，利用开源搜索引擎ElasticSearch完成高级搜索任务。    
    
搜索推荐：基于AJAX Jquery完成前后端交互。     
   
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

2、[下载并安装ElasticSearch-rtf 5.1.1](#ES)，其中启动前需要<span id="config">修改配置文件config/elasticsearch.yml</span>：
<pre><code>http.cors.enabled: true
http.cors.allow-origin: "*"
http.cors.allow-methods: OPTIONS, HEAD, GET, POST, PUT, DELETE
http.cors.allow-headers: "X-Requested-With, Content-Type, Content-Length, X-User"</code></pre>
进入ES根目录，命令行下启动ES：
<pre><code>./bin/elasticsearch.bat</code></pre>

3、使用FirstSpider的爬虫爬取数据并写入ES，数据管理可以使用Elasticsearch-head（具体使用方法见官方文档）：      

![Alt text](https://github.com/yipwinghong/SearchEngine/blob/master/Screenshots/1.jpg)
![Alt text](https://github.com/yipwinghong/SearchEngine/blob/master/Screenshots/2.jpg)
 
4、项目目录下运行：<pre><code>python manage.py runserver</code></pre>

5、浏览器下访问：<pre><code>127.0.0.1:8000</code></pre>
![Alt text](https://github.com/yipwinghong/SearchEngine/blob/master/Screenshots/3.jpg)
![Alt text](https://github.com/yipwinghong/SearchEngine/blob/master/Screenshots/4.jpg)
 
 
## <span id="ES">Windows环境下使用ElasticSearch</span>
[ElasticSearch](https://www.elastic.co/cn/)是一个基于Lucene（较难使用）的搜索服务器。它提供了一个分布式多用户能力的全文搜索引擎，基于RESTful web接口（http交互）。Elasticsearch是用Java开发的，并作为Apache许可条款下的开放源码发布，是当前流行的企业级搜索引擎。设计用于云计算中，能够达到实时搜索，稳定，可靠，快速，安装使用方便（其他搜索引擎：solr、sphinx）。      
- 随着ELK日志分析系统而逐渐流行；     
- 使用效果类似NoSQL数据库（但重点在搜索而非数据存储）；     
        
1、由于ElasticSearch是由Java编写的，首先需要安装[JDK8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)，确保版本在1.8以上。        
<pre><code>java -version</code></pre>
![java-version](http://ooaovpott.bkt.clouddn.com/java-vers.jpg)
    
2、安装[ElasticSearch-RTF](https://github.com/medcl/elasticsearch-rtf)（集成中文分词以及各种插件）：
<pre><code>git clone https://github.com/EagleChen/docker_elasticsearch_rtf.git</code></pre>

3、[修改配置文件，启动](#config)后在浏览器下访问可见：
<pre><code>127.0.0.1:9200</code></pre>
![ES-launch](http://ooaovpott.bkt.clouddn.com/ES-launch.png)

4、为了更方便地使用ES，推荐几个工具（注意版本要与ES一致）：        
- [Kibana](https://www.elastic.co/downloads/kibana)：分析及可视化平台        
- [ElasticSearch Head](https://github.com/mobz/elasticsearch-head)：集群管理工具
