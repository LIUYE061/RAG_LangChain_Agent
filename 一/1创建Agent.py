from langchain.agents import create_agent

def get_weather(city: str) -> str:
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="qwen-max",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in henan"}]}
)