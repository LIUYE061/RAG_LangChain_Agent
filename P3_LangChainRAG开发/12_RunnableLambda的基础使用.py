from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import  RunnableLambda

# 创建所需的解析器
str_parser = StrOutputParser()

# 模型创建
model = ChatTongyi(model="qwen-max")

# 第一个提示词模板
first_prompt = PromptTemplate.from_template(
    "我邻居姓: {lastname}, 刚生了{gender}, 请起名, 仅告知我名字, 不要额外信息."

)

# 第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "姓名: {name}, 请帮我解析含义"
)

# 函数的入参: AIMessage -> dict  ({"name": "xxx"})
my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

chain = first_prompt | model | my_func | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
    print(chunk, end="", flush=True)