from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# Imported from the https://github.com/langchain-ai/langgraph/tree/main/examples/plan-and-execute repo
from src.compiler.math_tools import get_math_tool

from src.configs.index import ENV


calculate = get_math_tool(ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=ENV["OPENAI_API_KEY"]),)
search = TavilySearchResults(
    max_results=1,
    description='tavily_search_results_json(query="the search query") - a search engine.',
)

tools = [search, calculate]

res= calculate.invoke(
    {
        "problem": "What's the temp of sf + 5?",
        "context": ["Thet empreature of sf is 32 degrees"],
    }
)