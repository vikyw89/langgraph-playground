from .state import AgentState
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.language_models import LanguageModelInput
from langchain_core.messages import HumanMessage, AIMessage
import os


async def astream(state: AgentState):
    model = ChatGoogleGenerativeAI(
        model="gemini-pro", api_key=os.environ["GOOGLE_API_KEY"]
    )

    input = [
        HumanMessage(
            content="Given a text, generate a comprehensive plan. Complete with dependencies, and id in json format"
        ),
        AIMessage(content="understood"),
        HumanMessage(content=state["input"]),
    ]

    stream = model.astream(input=input)

    state["output_stream"] = stream

    return state
