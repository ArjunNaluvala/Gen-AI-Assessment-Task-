from langchain.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume", "job_description"],
    template="""
Extract important information.

Resume:
{resume}

Job Description:
{job_description}
"""
)