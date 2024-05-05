async def test_arun():
    from src.utils import text_to_summary

    output = await text_to_summary.arun(text="""How to move a line of code up or down on a Mac?
With your caret on a line, you can press ⌥⇧↑ (macOS) / Ctrl+Alt+Shift+Up Arrow (Windows/Linux), to move a line up. Alternatively, you can move a line down with ⌥⇧↓ (macOS) / Ctrl+Alt+Shift+Down Arrow (Windows/Linux).Sep 20, 2021""")
    
    print("output", output)