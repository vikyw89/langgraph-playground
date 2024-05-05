
from src.utils.types import Chunk


async def arun(text: str, max_token=4000) -> list[Chunk]:
    from src.utils import text_to_chunks, auto_merge_chunks
    chunks = await text_to_chunks.arun(text=text)
    print("chunks", chunks)
    merged_chunks = await auto_merge_chunks.arun(chunks=chunks, max_token=max_token)

    return merged_chunks