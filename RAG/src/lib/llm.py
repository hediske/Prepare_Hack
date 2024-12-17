from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY


def get_llm(api_key = OPENAI_API_KEY,  temperature = 0.1 , model = "gpt-3.5-turbo" , max_tokens = 512):
    llm = ChatOpenAI(
        temperature=temperature,
        max_tokens=max_tokens,
        model= model
        )
    return llm
