from pydantic import BaseModel, Field
from .state import AgentState


async def arun(state: AgentState):
    # will review the output of the planner
    from src.utils import text_to_class

    class Review(BaseModel):
        plan_accuracy: int = Field(description="The accuracy of the plan", ge=0, le=5)
        dependency_accuracy: int = Field(
            description="The accuracy of the dependency", ge=0, le=5
        )
        review: str = Field(description="The review of the plan")

    output = await text_to_class.arun(
        text=f"""Given the input: {state["input"]}, evaluate and review this output plan: {state["output"]}""",
        output_class=Review,
    )

    # if review score is 5, we don't need to revise
    overal_output_score = (output.plan_accuracy + output.dependency_accuracy) / 2

    if overal_output_score == 5:
        state["final_output"] = state["output"]
    else:
        state["output"] = output.json()

    state["output_stream"] = None

    return state
