# -*- coding: utf-8 -*-

from elasticsearch_dsl import DocType, Nested, Keyword, Text, Integer, Date, Completion
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

connections.create_connection(hosts=["localhost"])


# elasticsearch源码的问题，直接用suggest = Completion(analyzer="ik_max_word")会报错
# 需要自行定义analyzer
class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}

ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])


class ArticleType(DocType):
    suggests = Completion(analyzer=ik_analyzer)     # 存放搜索建议字段
    title = Text(analyzer="ik_max_word")
    created_time = Date()
    url = Keyword()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "jobbole"       # 索引名必须全小写
        doc_type = "article"


class QuestionType(DocType):
    suggests = Completion(analyzer=ik_analyzer)
    title = Text(analyzer="ik_max_word")
    url = Keyword()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "zhihu"
        doc_type = "question"


class JobType(DocType):
    suggests = Completion(analyzer=ik_analyzer)
    title = Text(analyzer="ik_max_word")
    url = Keyword()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "lagou"
        doc_type = "job"

if __name__ == "__main__":
    ArticleType.init()      # 避免import时误执行初始化



