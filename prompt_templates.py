from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv 
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    temperature = 0.2
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "you are a {profession}" ),
    ("human",  "what is {question} in one sentence" ),
])

formatted_messages = prompt_template.invoke({
    "profession" : "physicist",
    "question": "one mole of atom",       
})

response = llm.invoke(formatted_messages)

print(response.content)
