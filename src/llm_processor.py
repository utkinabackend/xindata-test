from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pydantic import SecretStr


class LLMProcessor:
    def __init__(self):
        load_dotenv()
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("Добавьте ключ OpenAI в .env: OPENAI_API_KEY=")
        self.model = ChatOpenAI(api_key=SecretStr(os.getenv("OPENAI_API_KEY")), model="gpt-4o-mini")

    def process_query(self, query, data_context):
        prompt = f"Контекст: {data_context}\nЗапрос: {query}\nОтветь кратко."
        return self.model.invoke(prompt).content
