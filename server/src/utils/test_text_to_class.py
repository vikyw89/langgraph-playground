from typing import Annotated

from pydantic import BaseModel, Field
from src.configs.index import OPENAI_API_KEY


def test_arun():
    from src.utils.text_to_class import arun
    import asyncio

    class Task(BaseModel):
        id: Annotated[str, Field(description="Task id", examples=["1"])]
        title: Annotated[str, Field(description="Task title")]
        input: Annotated[
            list[str],
            Field(description="list of input id / dependency id", examples=["1"]),
        ]
        expected_output: Annotated[
            str, Field(description="Expected output of this task")
        ]

    class Plan(BaseModel):
        tasks: Annotated[list[Task], Field(description="list of tasks")]

    res = asyncio.run(
        arun(
            text="Let's think step by step. Create a plan for a wedding",
            output_class=Plan,
        )
    )

    print("res", res)
