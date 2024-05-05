from typing import Annotated
from pydantic import BaseModel, Field


async def arun(text:str)-> str:
    from src.utils import text_to_class

    class Summary(BaseModel):
        summary: Annotated[str, Field(description="Summary")]

    output : Summary = await text_to_class.arun(text=f"Summarize this text: {text}", output_class=Summary)

    return output.summary