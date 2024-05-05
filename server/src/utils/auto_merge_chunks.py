from src.utils.types import Chunk

async def arun(chunks:list[Chunk], max_token=4000) -> list[Chunk]:
    from langchain_text_splitters.sentence_transformers import SentenceTransformersTokenTextSplitter

    splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0)

    total_token = 0
    output = []
    for chunk in chunks:
        chunk_token = splitter.count_tokens(chunk.text)
        total_token += chunk_token
        prev_chunk = output[-1] if len(output) > 0 else None

        # create new chunk
        if not prev_chunk  or total_token > max_token:
            output.append(chunk)
            total_token = chunk_token
        
    return output

