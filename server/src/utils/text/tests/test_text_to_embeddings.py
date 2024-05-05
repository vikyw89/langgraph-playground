from src.utils.text import text_to_embeddings

import pytest


async def test_arun():

    res = await text_to_embeddings.arun(text="hello")

    print("output", res)