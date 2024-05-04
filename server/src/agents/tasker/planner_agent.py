from typing import Annotated

from pydantic import BaseModel, Field
from src.configs.index import GOOGLE_API_KEY
from .state import AgentState
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel


async def astream(state: AgentState):
    model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

    class Task(BaseModel):
        id: int = Field(description="Task id")
        title: str = Field(description="Task title")
        input: Annotated[
            list[int], Field(description="list of input id / dependency id")
        ]
        output: None = Field(description="output, leave None", default=None)

    class Plan(BaseModel):
        tasks: list[Task] = Field(description="List of tasks")

    parser = PydanticOutputParser(pydantic_object=Plan)

    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | model | parser

    stream = chain.astream({"query": f"Generate task plan for this : {state['input']}"})
    
    print("restream", stream)

    state["output_stream"] = stream

    return state
