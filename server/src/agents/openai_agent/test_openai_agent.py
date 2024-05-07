import asyncio
from langchain_core.messages import HumanMessage
from langchain_community.chat_message_histories import RedisChatMessageHistory
from src.configs.index import REDIS_URL

def test_openai_agent():
    async def run():
        from src.agents.openai_agent.index import runnable
        
        stream = runnable.astream_events(input={"messages":[HumanMessage(content="write an article about AI agents",id="12345")]}, version='v1')
        history = RedisChatMessageHistory(session_id="foo", url=REDIS_URL)

        async for event in stream:
            kind = event["event"]
            if kind == "on_chat_model_stream":
                content = event["data"]["chunk"].content
                if content:
                    # Empty content in the context of OpenAI means
                    # that the model is asking for a tool to be invoked.
                    # So we only print non-empty content
                    # print(content, end="|")
                    print(event["data"]["chunk"])
            elif kind == "on_tool_start":
                print("--")
                print(
                    f"Starting tool: {event['name']} with inputs: {event['data'].get('input')}"
                )
            elif kind == "on_tool_end":
                print(f"Done tool: {event['name']}")
                print(f"Tool output was: {event['data'].get('output')}")
                print("--")

    asyncio.run(run())