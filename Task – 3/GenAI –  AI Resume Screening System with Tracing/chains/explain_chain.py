from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_template("""
You are a strict resume evaluator.

Explain the score in ONLY short sentences in paragraphs.

Rules:
- No bullet points
- No numbering
- No headings
- No extra details
- No suggestions
- No repetition
- Keep it between 5600-650 words

Score: {score}

Matched Data:
{matched_data}

Final Answer:
""")

explanation_chain = prompt | llm