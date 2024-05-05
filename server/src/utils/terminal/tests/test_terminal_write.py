import json


async def test_arun():
    from src.utils.terminal import terminal_write

    res = await terminal_write.arun(text=f"""poetry env infos""")

    print("res", res)