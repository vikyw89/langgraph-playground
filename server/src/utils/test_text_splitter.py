async def test_arun():
    from src.utils import auto_merge_chunks

    await auto_merge_chunks.arun(text="""hello
                             test
                             line""")