import json
from typing import Annotated
from pydantic import BaseModel, Field
from .state import AgentState
from src.utils.llm_text import LlmText


async def arun(state: AgentState):
    class Task(BaseModel):
        id: Annotated[int, Field(description="Task id", examples=[1])]
        title: Annotated[str, Field(description="Task title")]
        input: Annotated[
            list[int],
            Field(description="list of input id / dependency id", examples=[[1]]),
        ]
        needed_skills: Annotated[
            list[str], Field(description="Assign to which professionals ?")
        ]
        estimated_hours: Annotated[
            int, Field(description="Estimated hours to finish the task")
        ]
        output: Annotated[str, Field(description="Expected output of this task")]

    class Plan(BaseModel):
        tasks: Annotated[list[Task], Field(description="list of tasks")]

    text = LlmText(
        object=f"""{state["input"]}"""
    )

    output: Plan = await text.arun_to_class(output_class=Plan, query=f"""Create a plan based on the text.""")

    print("output", output)
    parsed_output = []
    for task in output.tasks:
        parsed_output.append(task.model_dump())

    state["output"] = json.dumps(parsed_output)

    return state
