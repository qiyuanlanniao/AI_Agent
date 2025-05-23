import json

import requests
from langchain.agents import tool
# 工具
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.vectorstores import Qdrant
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI, OpenAI
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient

YUANFENJU_API_KEY = "xgVEfCeHkoCwUaUAOERCePbT6"


@tool
def test():
    """Test tool"""
    return "test"


@tool
def search(query: str):
    """只有需要了解实时信息或不知道的事情的时候才会使用这个工具。"""
    serp = SerpAPIWrapper()
    result = serp.run(query)
    print("实时搜索结果:", result)
    return result


@tool
def get_info_from_local_db(query: str):
    """只有回答与2024年运势或者龙年运势相关的问题的时候，会使用这个工具，必须输入用户的生日."""
    client = Qdrant(
        QdrantClient(path=r"E:\Documents\PycharmProjects\HM\AI_Agent\Virtual_project\bot\local_qdrand"),
        "local_documents",
        OpenAIEmbeddings(model="text-embedding-3-small"),
    )
    # 检索优化
    retriever = client.as_retriever(search_type="mmr")
    result = retriever.get_relevant_documents(query)
    return result


@tool
def bazi_cesuan(query: str):
    """只有做八字测算的时候才会使用这个工具,需要输入用户姓名和出生年月日时，如果缺少用户姓名和出生年月日时则不可用."""
    url = f"https://api.yuanfenju.com/index.php/v1/Bazi/cesuan"
    prompt = ChatPromptTemplate.from_template(
        """你是一个参数查询助手，根据用户输入内容找出相关的参数并按json格式返回。JSON字段如下： - "api_key":"xgVEfCeHkoCwUaUAOERCePbT6",
         - "name":"姓名", - "sex":"性别，0表示男，1表示女，根据姓名判断", - "type":"日历类型，0农历，1公里，默认1"，- "year":"出生年份 
         例：1998", - "month":"出生月份 例 8", - "day":"出生日期，例：8", - "hours":"出生小时 例 14", - "minute":"0"，
         如果没有找到相关参数，则需要提醒用户告诉你这些内容，只返回数据结构，不要有其他的评论，用户输入:{query}""")
    parser = JsonOutputParser()
    prompt = prompt.partial(format_instructions=parser.get_format_instructions())
    chain = prompt | ChatOpenAI(temperature=0) | parser
    data = chain.invoke({"query": query})
    print("八字查询结果:", data)
    result = requests.post(url, data=data)
    if result.status_code == 200:
        print("====返回数据=====")
        print(result.json())
        try:
            json = result.json()
            returnstring = "八字为:" + json["data"]["bazi_info"]["bazi"]
            return returnstring
        except Exception as e:
            return "八字查询失败,可能你忘记询问用户姓名或者出生年月日时了。"
    else:
        return "技术错误，请告诉用户稍后再试。"


@tool
def yaoyigua():
    """只有用户想要占卜抽签的时候才会使用这个工具。"""
    api_key = YUANFENJU_API_KEY
    url = f"https://api.yuanfenju.com/index.php/v1/Zhanbu/yaogua"
    result = requests.post(url, data={"api_key": api_key})
    if result.status_code == 200:
        print("====返回数据=====")
        print(result.json())
        returnstring = json.loads(result.text)
        image = returnstring["data"]["image"]
        print("卦图片:", image)
        return returnstring
    else:
        return "技术错误，请告诉用户稍后再试。"


@tool
def jiemeng(query: str):
    """只有用户想要解梦的时候才会使用这个工具,需要输入用户梦境的内容，如果缺少用户梦境的内容则不可用。"""
    api_key = YUANFENJU_API_KEY
    url = f"https://api.yuanfenju.com/index.php/v1/Gongju/zhougong"
    LLM = OpenAI(temperature=0)
    prompt = PromptTemplate.from_template("根据内容提取1个关键词，只返回关键词，内容为:{topic}")
    prompt_value = prompt.invoke({"topic": query})
    keyword = LLM.invoke(prompt_value)
    print("提取的关键词:", keyword)
    result = requests.post(url, data={"api_key": api_key, "title_zhougong": keyword})
    if result.status_code == 200:
        print("====返回数据=====")
        print(result.json())
        returnstring = json.loads(result.text)
        return returnstring
    else:
        return "技术错误，请告诉用户稍后再试。"
