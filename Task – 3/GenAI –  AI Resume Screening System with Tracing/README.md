#  AI Resume Screening System with LangChain + Groq + LangSmith

##  Project Overview
This project is an AI-powered Resume Screening System that evaluates candidates based on a given job description.

It uses LangChain to build a modular pipeline and LangSmith for tracing, debugging, and monitoring.

##  Objective
- Automate resume evaluation using AI
- Match candidate skills with job requirements
- Provide a score (0–100)
- Generate explainable feedback

##  Tech Stack
- Python
- LangChain
- OpenAI API
- Groq (LLM - LLaMA 3.1)
- LangSmith (Tracing & Debugging)

##  Project Structure

ai-resume-screening/
│
├── prompts/
│   ├── extract_prompt.py
│   ├── match_prompt.py
│   ├── score_prompt.py
│   └── explain_prompt.py
│
├── chains/
│   ├── extract_chain.py
│   ├── match_chain.py
│   ├── score_chain.py
│   └── explain_chain.py
│
├── data/
│   ├── resume_strong.txt
│   ├── resume_average.txt
│   ├── resume_weak.txt
│   └── job_description.txt
│
├── main.py
├── requirements.txt
└── README.md

##  Pipeline Flow

Resume → Skill Extraction → Matching → Scoring → Explanation

##  Features

✔ Skill Extraction (Skills, Tools, Experience)  
✔ Resume vs Job Matching  
✔ Candidate Scoring (0–100)  
✔ Explainable AI Output  
✔ Modular LangChain Pipeline  
✔ LangSmith Tracing  

##  Installation & Setup

### Step 1: Clone Repository
git clone <your-repo-link>
cd ai-resume-screening

### Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### Step 3: Install Dependencies
pip install -r requirements.txt

##  Environment Setup

Create a `.env` file:

OPENAI_API_KEY=sk-your_openai_key  
LANGCHAIN_TRACING_V2=true  
LANGCHAIN_API_KEY=your_langsmith_key  
LANGCHAIN_PROJECT=resume-screening  

##  Run the Project

python main.py

##  Sample Output

- Extracted Skills  
- Matching Skills & Missing Skills  
- Score (0–100)  
- Explanation (Strengths & Weaknesses)  

##  LangSmith Tracing

- Tracks each pipeline step  
- Helps debug incorrect outputs  
- Shows execution flow for:
  - Strong Candidate
  - Average Candidate
  - Weak Candidate  

##  Testing

The system is tested with:
- Strong Resume  
- Average Resume  
- Weak Resume  

##  Challenges Faced

- Handling API key issues  
- Updating LangChain imports (v1 changes)  
- Avoiding hallucination in outputs  
- Debugging using LangSmith traces  

##  Key Learnings

- Building modular LLM pipelines  
- Prompt engineering techniques  
- Debugging AI workflows  
- Using LangSmith for monitoring  
