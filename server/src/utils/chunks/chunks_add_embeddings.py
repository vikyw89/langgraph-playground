from src.utils.chunks.types import Chunk


async def arun(chunks:list[Chunk]):
    from src.utils.text import text_to_embeddings

    for chunk in chunks:
        embeddings_text = chunk.text_for_embeddings if chunk.text_for_embeddings else chunk.text
        chunk.embeddings = await text_to_embeddings.arun(text=embeddings_text)

    return chunks