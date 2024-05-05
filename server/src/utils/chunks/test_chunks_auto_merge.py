from src.utils.chunks import chunks_automerge
from src.utils.text import text_to_chunks


async def test_arun():

    text = """from litellm import embedding
import os
os.environ['OPENAI_API_KEY'] = ""
response = embedding(
    model="text-embedding-3-small",
    input=["good morning from litellm", "this is another item"],
    metadata={"anything": "good day"},
    dimensions=5 # Only supported in text-embedding-3 and later models.
)"""

    chunks = await text_to_chunks.arun(text=text)
    
    assert len(chunks) == 9

    merged_chunks = await chunks_automerge.arun(chunks=chunks)

    assert len(merged_chunks) == 1