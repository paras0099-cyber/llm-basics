from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv 
from langchain_core.messages import SystemMessage , HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    temperature = 0.2
)

messages = [
    SystemMessage(content = "you are a professional coder"),
    HumanMessage(content = "Tell me what is python language in one sentence"),
    
]

response = llm.invoke(messages)

print(response.content)
