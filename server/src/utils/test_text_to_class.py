from typing import Annotated

from pydantic import BaseModel, Field


def test_arun():
    from src.utils.text_to_class import arun
    import asyncio

    class Output(BaseModel):
        """Extracted names"""
        names: Annotated[list[str], Field(description="Extracted names")]

    res = asyncio.run(arun(text="irene, irenelle, irena", output_class=Output))
    print("res", res)
