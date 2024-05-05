from src.agents.planner.state import AgentState


async def router(state:AgentState):
    if state["final_output"] is not None:
        return "end"
    else:
        return "planner"