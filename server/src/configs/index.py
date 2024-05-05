import os
from dotenv import load_dotenv
from nest_asyncio import apply
apply()
load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
GOOGLE_API_KEY= os.environ["GOOGLE_API_KEY"]