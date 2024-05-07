import asyncio
import json
import pytest


def test_arun():
    from src.utils.terminal import terminal_write

    async def run():
        res = await terminal_write.arun(text=f"""poetry env infos""")

        print("res", res)

    asyncio.run(run())
