from typing import Annotated
from pydantic import BaseModel, Field
from uuid import uuid4


    
async def arun(text:str) -> list[Chunk]:
    text_list = text.splitlines()
    count = 0
    output = []
    for value in text_list:
        count += 1
        output.append(Chunk(text=value, start_line=count, end_line=count))
    return output
