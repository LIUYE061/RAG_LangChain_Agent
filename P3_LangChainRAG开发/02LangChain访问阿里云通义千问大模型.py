from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

# invoke调用     一次性返回完整结果
# res = model.invoke(input="你是谁?")
# print(res)

# stream        逐段返回结果, 流式输出
res = model.stream(input="你是谁?")

for chunk in res:
    print(chunk, end="", flush=True)