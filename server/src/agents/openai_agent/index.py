from langgraph.prebuilt.chat_agent_executor import create_tool_calling_executor
from langchain_openai.chat_models import ChatOpenAI
from src.configs.index import OPENAI_API_KEY
from langchain.tools.ddg_search import DuckDuckGoSearchRun

model = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
runnable = create_tool_calling_executor(model=model, tools=[DuckDuckGoSearchRun()])
