import asyncio
from dotenv import load_dotenv
from src.agents.planner.state import AgentState
from langchain_core.messages import BaseMessageChunk

load_dotenv()


async def main():
    from src.agents.planner.index import runnable

    stream = await runnable.ainvoke(input=AgentState(input="go to moon"), debug=True)

    # async for node in stream:
    #     for key, value in node.items():
    #         print("------------------")
    #         print(key)
    #         print("------------------")
    #         value: AgentState
    #         print(value)
    #         if value["output_stream"] is not None:
    #             final_content = ""
    #             async for chunk in value["output_stream"]:
    #                 chunk: BaseMessageChunk
    #                 print("chunk", chunk)
    #                 # final_content += chunk.content
    #                 # do something with the stream
    #             print("final_content", final_content)


if __name__ == "__main__":
    asyncio.run(main())
