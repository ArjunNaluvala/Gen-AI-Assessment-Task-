from dotenv import load_dotenv
import os

# Load API keys from .env
load_dotenv()

from chains.extract_chain import extraction_chain
from chains.match_chain import matching_chain
from chains.score_chain import scoring_chain
from chains.explain_chain import explanation_chain


print("\n= RESUME SCREENING SYSTEM =\n")


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def run_resume_screening(resume_text, job_description):

    # 1. Extract structured info
    extracted = extraction_chain.invoke({
        "resume": resume_text,
        "job_description": job_description
    })

    # 2. Match resume vs job
    matched = matching_chain.invoke({
        "resume_data": extracted,
        "job_description": job_description
    })

    # 3. Score
    score = scoring_chain.invoke({
        "matched_data": matched
    }).content

    # 4. Explanation
    explanation = explanation_chain.invoke({
    "score": score,
    "matched_data": matched
    }).content

    return score, explanation


# - MAIN EXECUTION

job_description = read_file("data/job_description.txt")

resumes = {
    "Strong Resume": "data/resume_strong.txt",
    "Average Resume": "data/resume_average.txt",
    "Weak Resume": "data/resume_weak.txt"
}

for name, path in resumes.items():

    print(f"= {name} =")

    resume_text = read_file(path)

    score, explanation = run_resume_screening(resume_text, job_description)

    print("\n Final Score:\n", score)
    print("\n Explanation:\n", explanation)