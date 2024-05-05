from typing import Annotated
from uuid import uuid4
from pydantic import BaseModel, Field


class Chunk(BaseModel):
    id: Annotated[str, Field(description="Id", default_factory=lambda: uuid4().hex)]
    text: Annotated[str | None, Field(description="Text content")] = None
    start_line: Annotated[int | None, Field(description="Start line of the text")] = None
    end_line: Annotated[int | None, Field(description="End line of the text")] = None
    summary: Annotated[str | None, Field(description="Summary of the context")] = None
    file: Annotated[str | None, Field(description="File path and name in the system")] = None
    text_for_embeddings: Annotated[str | None, Field(description="Text to be used for embeddings")] = None
    embeddings: Annotated[list[float] | None, Field(description="Embeddings")] = None