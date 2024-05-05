async def test_arun():
    from src.utils import text_to_embeddings

    res = await text_to_embeddings.arun(text="hello")

    print("output", res)