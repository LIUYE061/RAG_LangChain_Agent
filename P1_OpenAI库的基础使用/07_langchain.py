import os

from langchain.chat_models import init_chat_model
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_openai import ChatOpenAI

# langchain访问大模型LLM

# 方式1: ChatTongyi

# client = ChatTongyi(
#     api_key=os.getenv("DASHSCOPE_API_KEY"),
#     model_name = "qwen-max"
# )
#
# response = client.invoke("你是谁?")    # invoke调用
# print(response.content)


# 方式2: 创建模型对象, 基于OpenAI  规范

# client = ChatOpenAI(
#     api_key=os.getenv("DASHSCOPE_API_KEY"),
#     model_name = "qwen-max",
#     base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
# )
#
# response = client.invoke("你是谁?")
# print(response.content)


# 方式3: init_chat_model: 对于不兼容OpenAI的模型, 可以使用
#     参数1: model模型名称
#     参数2: model_provider模型提供者

# client = init_chat_model("deepseek_chat", model_provider="deepseek")
# response = client.invoke("你是谁?")
# print(response.content)




agent_v1 = create_agent("qwen-max")
response = agent_v1.invoke({"message": [{"role": "user", "content": "元旦节是几号?"}]})
print(response)