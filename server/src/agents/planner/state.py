from typing import AsyncIterable, TypedDict
from langchain_core.messages import BaseMessageChunk


class AgentState(TypedDict):
    input: str | bytes
    output_stream: AsyncIterable[BaseMessageChunk] | None = None
    output: str | None = None
    final_output: str | None = None
    
