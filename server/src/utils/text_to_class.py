from typing import AsyncIterable, TypeVar
from pydantic import BaseModel
from src.configs.index import GOOGLE_API_KEY
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI

T = TypeVar("T", bound=BaseModel)



async def arun(
    text: str,
    output_class: T,
    model=ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY),
) -> T:
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
    parser = PydanticOutputParser(pydantic_object=output_class)

    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | model | parser

    output = await chain.ainvoke({"query": text})

    return output
