from typing import AsyncIterable, TypedDict
from langchain_core.messages import BaseMessageChunk


class AgentState(TypedDict):
    input: str | bytes
    output_stream: AsyncIterable[BaseMessageChunk]
    output: str
    review: str | None = None
    
