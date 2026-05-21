from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),

    # FAST MODEL
    model_name="llama-3.1-8b-instant",

    temperature=0.7
)