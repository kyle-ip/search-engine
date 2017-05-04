from django.shortcuts import render
from django.views.generic.base import View
from search.models import ArticleType, QuestionType, JobType
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from pure_pagination import Paginator, PageNotAnInteger
import redis

import json
from datetime import datetime

client = Elasticsearch(hosts=["127.0.0.1"])
# redis_cli = redis.StrictRedis()
#
# class IndexView(View):
#     def get(self, request):
#         topn_search = redis_cli.zrevrangebyscore("search_keywords_set", "+inf", "-inf", start=0, num=5)
#         return render(request, "index.html", {"topn_search":topn_search})


# 搜索建议
class SearchSuggestView(View):
    def get(self, request):
        s_type = request.GET.get("s_type", "article")
        index_dict = {
            "article": ArticleType,
            "question": QuestionType,
            "job": JobType,
        }
        key_words = request.GET.get('s', '')                # 从url中接收搜索关键词参数
        re_datas = []
        if key_words:
            s = index_dict[s_type].search()
            s = s.suggest(
                'my_suggest', key_words, completion={
                    "field": "suggests",
                    "fuzzy": {
                        "fuzziness": 2      # 编辑距离为2
                    },
                    "size": 5               # 取5个元素
                }
            )
            suggestions = s.execute_suggest()               # 返回的数据同kibana上执行代码的结果
            for match in suggestions.my_suggest[0].options:
                re_datas.append(match._source["title"])
        return HttpResponse(json.dumps(re_datas), content_type="application/json")


class SearchView(View):
    def get(self, request):
        results_per_page = 10

        key_words = request.GET.get("q", "")                # 从url中接收搜索关键词、类型参数
        s_type = request.GET.get("s_type", "article")

        index_dict = {
            "article": ["jobbole", "伯乐在线"],
            "question": ["zhihu", "知乎社区"],
            "job": ["lagou", "拉勾网"]
        }

        page = int(request.GET.get("page", "1"))            # 获取请求页码

        # redis_cli = redis.StrictRedis()
        # jobbole_count = redis_cli.get("jobbole_count")

        jobbole_count = client.search(
            index="jobbole",
            body={
                "query": {},
            }
        )["hits"]["total"]

        lagou_count = client.search(
            index="lagou",
            body={
                "query": {},
            }
        )["hits"]["total"]

        start = datetime.now()                              # 计算搜索用时
        response = client.search(                           # 在ES中搜索结果（body部分与kibana中执行代码相同）
            index=index_dict[s_type][0],                       # 返回结果在“hits”
            body={
                "query": {
                    "multi_match": {                        # 对多个字段搜索
                        "query": key_words,
                        "fields": ["tags", "title", "content"]
                    }
                },
                "from": (page - 1) * results_per_page,      # 例如第二页为1*10即下标为10开始，取10个
                "size": results_per_page,
                "highlight": {                              # 关键词在title、content中做高亮处理（前后加上html标签）
                    "pre_tags": ['<span class="keyWord">'],
                    "post_tags": ['</span>'],
                    "fields": {
                        "title": {},    #
                        "content": {},
                    }
                }
            }
        )
        end = datetime.now()
        last_seconds = (end - start).total_seconds()

        total_nums = response["hits"]["total"]              # 匹配结果总数并计算约有多少页
        page_nums = int(total_nums / 10) + 1 if (page % 10) > 0 else int(total_nums / 10)

        hit_list = []
        for hit in response["hits"]["hits"]:
            hit_dict = {}                                   # 取高亮处理后的标题和内容，取不到则从source中取
            if "title" in hit.get("highlight", ""):
                hit_dict["title"] = "".join(hit["highlight"]["title"])
            else:
                hit_dict["title"] = hit["_source"]["title"]
            if "content" in hit.get("highlight", ""):       # 只取前500个字符
                hit_dict["content"] = "".join(hit["highlight"]["content"])[:500]
            else:
                hit_dict["content"] = hit["_source"]["content"][:500]

            hit_dict["created_time"] = hit["_source"].get("created_time", "")
            hit_dict["url"] = hit["_source"]["url"]
            hit_dict["score"] = hit["_score"]

            hit_list.append(hit_dict)

        page_list = [
            i for i in range(page-4, page+5) if 0 < i <= page_nums      # 分页页码列表
        ]

        return render(
            request,
            "result.html",
            {
                "page": page,
                "all_hits": hit_list,
                "key_words": key_words,
                "total_nums": total_nums,
                "page_nums": page_nums,
                "last_seconds": last_seconds,
                "page_list": page_list,
                "jobbole_count": jobbole_count,
                "lagou_count": lagou_count,
                "website": index_dict[s_type][1],
                "s_type": s_type,
            }
        )


