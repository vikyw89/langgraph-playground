import asyncio
from langchain_core.messages import HumanMessage


def test_gemini_agent():
    async def run():
        from src.agents.gemini_agent.index import runnable

        stream = runnable.astream_events(
            input={
                "messages": [HumanMessage(content="write an article about AI agents")]
            },
            version="v1",
        )

        async for event in stream:
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

    asyncio.run(run())
