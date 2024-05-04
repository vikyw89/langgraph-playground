from typing import Annotated

from pydantic import BaseModel, Field


def test_arun():
    from src.utils.text_to_class import arun
    import asyncio

    class Person(BaseModel):
        name: str = Field(description="Person name")
        age: int = Field(description="Person age")
        
    class Output(BaseModel):
        persons: Annotated[list[Person], Field(description="Extracted names")]

    res = asyncio.run(arun(text="irene 23years, irenelle 25years, irena 4 years", output_class=Output))
    print("res", res)
