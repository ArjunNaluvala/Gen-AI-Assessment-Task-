from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_template(
    "Compare resume data:\n{resume_data}\n\nwith job description:\n{job_description}\n\nReturn matching skills and gaps."
)

matching_chain = prompt | llm