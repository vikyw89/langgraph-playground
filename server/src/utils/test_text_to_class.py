from typing import Annotated

from pydantic import BaseModel, Field
from src.configs.index import OPENAI_API_KEY


async def test_arun():
    from src.utils.text_to_class import arun

    class Task(BaseModel):
        id: Annotated[int, Field(description="Task id", examples=[1])]
        title: Annotated[str, Field(description="Task title")]
        input: Annotated[
            list[int],
            Field(description="list of input id / dependency id", examples=[1]),
        ]
        expected_output: Annotated[
            str, Field(description="Expected output of this task")
        ]

    class Plan(BaseModel):
        tasks: Annotated[list[Task], Field(description="list of tasks")]

    res = arun(
            text="Let's think step by step. Create a plan for a wedding",
            output_class=Plan,
        )

    print("res", res)