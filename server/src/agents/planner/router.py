from src.agents.planner.state import AgentState


async def router(state:AgentState):
    if state["is_final"]:
        return "end"
    else:
        return "planner"