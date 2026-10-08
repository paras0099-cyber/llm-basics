from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    temperature = 0.2,
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "you are a {profession}" ),
    ("human",  "what is {question} in one sentence" ),
])

parser = StrOutputParser()

chain = prompt_template | llm | parser

response = chain.invoke(
    {
        "profession": "chemist",
        "question": "which medicine have to be taken in fever",
    }
)


print(response)
