from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_template("""
You are a strict resume evaluator.

Based on the matched data below, return ONLY a number between 0 and 100.

Do NOT add explanations. Do NOT add text.

Matched Data:
{matched_data}
""")

scoring_chain = prompt | llm