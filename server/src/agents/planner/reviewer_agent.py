from typing import Annotated
from pydantic import BaseModel, Field
from .state import AgentState
from src.utils.llm_text import LlmText


async def arun(state: AgentState):
    # will review the output of the planner

    class Review(BaseModel):
        plan_accuracy: Annotated[
            int, Field(description="The accuracy of the plan", ge=0, le=5)
        ]
        input_accuracy: Annotated[
            int, Field(description="The accuracy of the dependency", ge=0, le=5)
        ]
        review: Annotated[
            str, Field(description="Suggest are of improvement based on above score")
        ]

    text = LlmText(
        object=f"""Given the input: {state["input"]}, evaluate and review this output plan: {state["output"]}"""
    )

    output: Review = await text.arun_to_class(output_class=Review)

    # if review score is 5, we don't need to revise
    overal_output_score = (output.plan_accuracy + output.input_accuracy) / 2

    if overal_output_score >= 4:
        state["is_final"] = True

    return state
