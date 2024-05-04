from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import END, MessageGraph
from src.configs.index import ENV


model = ChatOpenAI(temperature=0, api_key=ENV["OPENAI_API_KEY"],streaming=True,verbose=True)

graph = MessageGraph()

graph.add_node("oracle", model)
graph.add_edge("oracle", END)

graph.set_entry_point("oracle")

runnable = graph.compile(debug=True)
res = runnable.invoke(HumanMessage("What is 1 + 1?"))

print("res", res)