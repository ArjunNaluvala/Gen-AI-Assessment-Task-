from langchain.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["skills", "job"],
    template="""
Compare candidate skills with job requirements.

Skills:
{skills}

Job Description:
{job}

Rules:
- Give partial credit if skills are related
- Do not penalize missing "preferred" skills heavily
- Focus more on overall alignment than exact matches

Output:
- Matching Skills
- Missing Skills
"""
)