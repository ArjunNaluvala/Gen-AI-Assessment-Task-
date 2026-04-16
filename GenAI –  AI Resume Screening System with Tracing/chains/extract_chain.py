from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_template("""
Extract key information from this resume.

Return:
- Skills
- Experience
- Education

Resume:
{resume}
""")

extraction_chain = prompt | llm