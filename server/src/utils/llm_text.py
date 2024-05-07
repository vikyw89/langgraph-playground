from typing import Annotated, TypeVar
from pydantic import BaseModel, Field
from src.configs.index import GOOGLE_API_KEY, OPENAI_API_KEY
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI
from src.utils.chunks.types import Chunk

T = TypeVar("T", bound=BaseModel)


class LlmText:
    def __init__(self, object: str) -> None:
        self.object = object
        pass

    async def arun_to_class(
        self,
        output_class: T,
        query: str = "",
        model=ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY,name="arun_to_class"),
    ) -> T:

        parser = PydanticOutputParser(pydantic_object=output_class, name="arun_to_class_parser")

        prompt = PromptTemplate(
            template="Let's think step by step. Answer the user query.\n{format_instructions}\n{query}\n",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        chain = prompt | model | parser

        output: output_class = await chain.ainvoke(
            {"query": f"{query}\n{self.object}"}
        )

        return output

    async def arun_to_summary(self, query: str = "Summarize this text") -> str:

        class Summary(BaseModel):
            summary: Annotated[str, Field(description="Summary")]

        output: Summary = await self.arun_to_class(query=query, output_class=Summary)

        return output.summary

    async def arun_to_embeddings(
        self,
        model=GoogleGenerativeAIEmbeddings(
            model="textembedding-gecko@003", google_api_key=GOOGLE_API_KEY
        ),
    ) -> list[float]:
        embedding = await model.aembed_query(text=self.object)
        return embedding

    async def arun_to_chunks(self) -> list[Chunk]:
        text_list = self.object.splitlines()
        count = 0
        output = []
        for value in text_list:
            count += 1
            output.append(Chunk(text=value, start_line=count, end_line=count))
        return output

    async def arun_to_triplets(
        self,
        query: str = "Generate triplets from the following text",
        model=ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY),
        # model=ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY),
    ) -> list[tuple[str, str, str]]:
        class Triplet(BaseModel):
            subject: Annotated[str, Field(description="Subject")]
            predicate: Annotated[str, Field(description="Predicate")]
            object: Annotated[str, Field(description="Object")]

        class Output(BaseModel):
            triplets: Annotated[list[Triplet], Field(description="List of triplets")]

        output: Output = await self.arun_to_class(
            query=query,
            output_class=Output,
            model=model,
        )
        return output.triplets
