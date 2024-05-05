import json
from typing import Annotated, Literal
from pydantic import BaseModel, Field
from .state import AgentState
from langchain_core.pydantic_v1 import BaseModel
from src.utils import text_to_class


async def arun(state: AgentState):
    class Task(BaseModel):
        id: Annotated[str, Field(description="Task id", examples=["1"])]
        title: Annotated[str, Field(description="Task title")]
        input: Annotated[
            list[str],
            Field(description="list of input id / dependency id", examples=["1"]),
        ]
        assigned_to: Annotated[Literal["code_writter", "code_executor","researcher", "email_writter"],Field(description="Assign to which professionals ?")]
        output: Annotated[str, Field(description="Expected output of this task")]

    class Plan(BaseModel):
        tasks: Annotated[list[Task], Field(description="list of tasks")]

    output: Plan = await text_to_class.arun(
        text=f"""Let's think step by step, create a plan for: {state["input"]}""",
        output_class=Plan,
    )

    print("output", output)
    parsed_output = []
    for task in output.tasks:
        parsed_output.append(task.dict())

    state["output"] = json.dumps(parsed_output)
    state["output_stream"] = None

    return state
