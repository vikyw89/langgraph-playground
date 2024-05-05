import json
from typing import Annotated
from pydantic import BaseModel, Field
from .state import AgentState
from src.utils.text import text_to_class


async def arun(state: AgentState):
    class Task(BaseModel):
        id: Annotated[int, Field(description="Task id", examples=[1])]
        title: Annotated[str, Field(description="Task title")]
        input: Annotated[
            list[int],
            Field(description="list of input id / dependency id", examples=[[1]]),
        ]
        needed_skills: Annotated[list[str],Field(description="Assign to which professionals ?")]
        estimated_hours: Annotated[int, Field(description="Estimated hours to finish the task")]
        output: Annotated[str, Field(description="Expected output of this task")]

    class Plan(BaseModel):
        tasks: Annotated[list[Task], Field(description="list of tasks")]

    output: Plan = await text_to_class.arun(
        text=f"""Let's think step by step, create a plan for: {state["input"]}""",
        output_class=Plan,
    )

    parsed_output = []
    for task in output.tasks:
        parsed_output.append(task.model_dump())

    state["output"] = json.dumps(parsed_output)
    state["output_stream"] = None

    return state
