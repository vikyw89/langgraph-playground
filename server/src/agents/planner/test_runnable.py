from src.agents.planner.state import AgentState
from src.agents.planner.index import runnable
from langchain_core.messages import BaseMessageChunk

async def test_runnable():
    
    stream = runnable.astream(input=AgentState(input="write an article about supabase"), debug=True)
    
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
                    print("chunk", chunk)
                    # final_content += chunk.content
                    # do something with the stream
                print("final_content", final_content)

