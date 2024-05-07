import asyncio
import pytest
from src.agents.planner.state import AgentState
from src.agents.planner.index import runnable
from langchain_core.messages import BaseMessageChunk
    

# def test_runnable():
    
#     stream = runnable.astream(input=AgentState(input="write an article about AI agents"))
    
#     async def run():
#         async for node in stream:
#             for key, value in node.items():
#                 print("------------------")
#                 print(key)
#                 print("------------------")
#                 value: AgentState
#                 if value["output_stream"] is not None:
#                     final_content = ""
#                     async for chunk in value["output_stream"]:
#                         chunk: BaseMessageChunk
#                         print("chunk", chunk)
#                         # final_content += chunk.content
#                         # do something with the stream
#                     print("final_content", final_content)

#     asyncio.run(run())

import asyncio
from langchain_core.messages import HumanMessage, AIMessage
from src.configs.index import REDIS_URL

def test_planner_agent():

    
    async def run():
        from langchain_community.chat_message_histories import RedisChatMessageHistory
        from src.agents.planner.index import runnable
        
        history = RedisChatMessageHistory(session_id="foo", url=REDIS_URL)
        await history.aadd_messages(messages=[HumanMessage(content="write an article about AI agents")])
        stream = runnable.astream_events(
            input={"input": "write an article about AI agents","id":"foo"},
            version="v1",
        )

        async for event in stream:
            # print("event", event)
            kind = event["event"]
            if kind == "on_chat_model_stream":
                content = event["data"]["chunk"].content
                if content:
                    # Empty content in the context of OpenAI means
                    # that the model is asking for a tool to be invoked.
                    # So we only print non-empty content
                    print(content, end="|")
            elif kind == "on_tool_start":
                print("--")
                print(
                    f"Starting tool: {event['name']} with inputs: {event['data'].get('input')}"
                )
            elif kind == "on_tool_end":
                print(f"Done tool: {event['name']}")
                print(f"Tool output was: {event['data'].get('output')}")
                print("--")
            elif kind == "on_chat_model_end":
                print("--")
                print(f"{kind}: {event["name"]}")
                content = event["data"]["output"]
                print(content["generations"][0][0]["text"])
                await history.aadd_messages(messages=[AIMessage(content=content["generations"][0][0]["text"])])
                print("--")
                
        print(await history.aget_messages())
    asyncio.run(run())
