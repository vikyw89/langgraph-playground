from langchain.tools import StructuredTool

async def arun(text: str):
    from src.utils.terminal import terminal_write

    return await terminal_write.arun(text=text)


terminal = StructuredTool.from_function(
    name="unix_terminal",
    description="useful to write code in the terminal",
    coroutine=arun
)