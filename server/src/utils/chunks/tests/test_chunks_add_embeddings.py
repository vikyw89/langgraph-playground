import pytest
from src.utils.chunks import chunks_add_embeddings
from src.utils.chunks.types import Chunk

@pytest.mark.asyncio
async def test_arun():

    chunks = [Chunk(text="hellooooo", start_line=1, end_line=1)]

    chunks_with_embeddings = await chunks_add_embeddings.arun(chunks=chunks)

    print("chunks with embeddings", chunks_with_embeddings)
