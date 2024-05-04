import asyncio


def test_arun():
    from src.agents.planner import planner_agent
    from src.agents.planner.state import AgentState
    from langchain_core.messages import BaseMessageChunk
    
    async def arun():
        state = await planner_agent.arun(state=AgentState(input="write an article about supabase"))

        print("state",state["output"])

    asyncio.run(arun())