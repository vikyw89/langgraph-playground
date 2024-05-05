
from src.utils.chunks import chunks_automerge
from src.utils.chunks.types import Chunk
from src.utils.text import text_to_chunks


async def arun(text: str, max_token=4000) -> list[Chunk]:
    chunks = await text_to_chunks.arun(text=text)
    print("chunks", chunks)
    merged_chunks = await chunks_automerge.arun(chunks=chunks, max_token=max_token)

    return merged_chunks