from langchain.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match"],
    template="""
You are an AI resume evaluator.

Based on the match details, assign a score from 0 to 100.

Be fair:
- Do NOT penalize heavily for 1–2 missing skills
- Reward transferable skills

Scoring Guidelines:
- Strong match with most required skills → 80–95
- Moderate match with some missing skills → 55–80
- Partial match with few relevant skills → 30–55
- Very weak or irrelevant → 0–30

Score the resume based on:

1. Skill match (50%)
2. Experience relevance (40%)
3. Education relevance (10%)

Important:
- Do NOT be overly strict
- Consider overall potential, not just missing skills
- Give partial credit for related skills and experience

Match Details:
{match}

Return ONLY the final score (number).
"""
)