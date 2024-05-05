from src.configs.index import OPENAI_API_KEY


async def arun(text:str):
    from litellm import aembedding

    embedding = await aembedding(model="text-embedding-3-small", api_key=OPENAI_API_KEY, input=[text])
    return embedding.data[0]["embedding"]