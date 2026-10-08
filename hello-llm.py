from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv 

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    temperature = 0.2,
)

prompt_text = "tell what is an ai in one sentence"

response = llm.invoke(prompt_text)

print (response.content)
