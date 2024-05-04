from langgraph.graph import StateGraph, END
from src.agents.planner.router import router
from . import  planner_agent, reviewer_agent
from .state import AgentState

CONDITIONAL_EDGES_MAPPING = {
    "planner": "planner",
    "resolver": "resolver",
    "reviewer": "reviewer",
    "end": END,
}

# Define a new graph
graph = StateGraph(AgentState)
graph.add_node("planner", planner_agent.arun)
graph.add_node("reviewer", reviewer_agent.arun)

# define edges
graph.set_entry_point("planner")
graph.add_edge("planner", "reviewer")


graph.add_conditional_edges(
    start_key="reviewer",
    condition=router,
    conditional_edge_mapping={
        "planner": "planner",
        "end": END,
    },
)

runnable = graph.compile()
