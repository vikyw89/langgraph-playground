import asyncio
from dotenv import load_dotenv
from .agents.tasker.state import AgentState
from langchain_core.messages import BaseMessageChunk

load_dotenv()


async def main():
    from .agents.tasker.index import runnable

    stream = runnable.astream(input=AgentState(input="write an article about supabase"))

    async for node in stream:
        for key, value in node.items():
            print("------------------")
            print(key)
            print("------------------")
            value: AgentState
            if value["output_stream"] is not None:
                final_content = ""
                async for chunk in value["output_stream"]:
                    chunk: BaseMessageChunk
                    final_content += chunk.content
                    # do something with the stream
                print("final_content", final_content)


if __name__ == "__main__":
    asyncio.run(main())
