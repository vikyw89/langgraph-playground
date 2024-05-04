import json
from typing import TypeVar
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage
from src.configs.index import GOOGLE_API_KEY

T = TypeVar("T", bound=BaseModel)


async def arun(text: str, output_class: T) -> T:
    from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
    """
    Asynchronously runs the given text through a chat model and extracts data from it using the specified output class.

    Args:
        text (str): The text to be processed.
        output_class (Type[T]): The class to be used for extracting data from the text.

    Returns:
        T: An instance of the output class, initialized with the extracted data.

    Raises:
        KeyError: If the function call arguments in the model's response are missing.

    Example:
        >>> output_class = MyOutputClass
        >>> text = "Some text to process"
        >>> result = await arun(text, output_class)
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

    model_with_tools = model.bind_tools([output_class])

    input = [
        HumanMessage(content="Call tool to extract data from text"),
        AIMessage(content="understood"),
        HumanMessage(content=text),
    ]

    res = await model_with_tools.ainvoke(input=input)
    raw_output = json.loads(res.additional_kwargs["function_call"]["arguments"])
    return output_class(**raw_output)
