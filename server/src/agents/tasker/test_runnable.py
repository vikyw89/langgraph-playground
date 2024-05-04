from src.agents.tasker.state import AgentState


def test_runnable():
    from src.agents.tasker.index import runnable
    
    stream = runnable.astream(input=AgentState(input="write an article about supabase"))
    