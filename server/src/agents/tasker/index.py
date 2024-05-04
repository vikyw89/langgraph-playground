from langgraph.graph import StateGraph, END
from . import resolver_agent, planner_agent, reviewer_agent
from .state import AgentState

CONDITIONAL_EDGES_MAPPING = {
    "planner": "planner",
    "resolver": "resolver",
    "reviewer": "reviewer",
    "end": END,
}

# Define a new graph
graph = StateGraph(AgentState)
graph.add_node("planner", planner_agent.astream)
# graph.add_node("resolver", resolver_agent.astream)
# graph.add_node("reviewer", reviewer_agent.astream)

graph.set_entry_point("planner")


graph.add_edge("planner", END)

# graph.add_conditional_edges(
#     start_key="resolver",
#     condition=router,
#     conditional_edge_mapping={
#         "resolver": "resolver",
#         "reviewer": "reviewer",
#     },
# )

# graph.add_conditional_edges(
#     start_key="reviewer",
#     condition=router,
#     conditional_edge_mapping={
#         "planner": "planner",
#         "end": END,
#     },
# )

runnable = graph.compile()
