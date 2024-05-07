from langgraph.prebuilt.chat_agent_executor import create_function_calling_executor
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from src.configs.index import GOOGLE_API_KEY
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun

model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

runnable = create_function_calling_executor(model=model, tools=[DuckDuckGoSearchRun()])
