from src.utils.types import Chunk
from langchain_text_splitters.sentence_transformers import SentenceTransformersTokenTextSplitter

async def arun(chunks:list[Chunk], max_token=4000) -> list[Chunk]:

    splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0)

    total_token = 0
    output : list[Chunk]= []
    for chunk in chunks:
        chunk_token = splitter.count_tokens(text=chunk.text)
        total_token += chunk_token
        prev_chunk = output[-1] if len(output) > 0 else None

        # create new chunk
        if not prev_chunk  or total_token > max_token:
            output.append(chunk)
            total_token = chunk_token
        else:
            # merge the chunk
            prev_chunk.text += f"\n{chunk.text}"
            prev_chunk.end_line = chunk.end_line

    return output

