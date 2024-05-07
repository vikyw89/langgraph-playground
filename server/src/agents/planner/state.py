from typing import AsyncIterable, TypedDict
from langchain_core.messages import BaseMessageChunk, BaseMessage


class AgentState(TypedDict):
    input: str
    id: str
    output: str | None = None
    is_final: bool = False
