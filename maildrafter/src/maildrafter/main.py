#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from maildrafter.crew import Maildrafter

import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs  = {
        'job_title': 'Data Scientist',           # Specify job title
        'location': 'Bangalore',   
                              # Specify job location
        'skills': [
    "Python",
    "PySpark",
    "SQL",
    "Machine Learning",
    "Generative AI",
    "Large Language Models (LLMs)",
    "Prompt Engineering",
    "Retrieval-Augmented Generation (RAG)",
    "Agentic AI",
    "Langchain",
    "Data Preprocessing",
    "Exploratory Data Analysis (EDA)",
    "Feature Engineering",
    "Natural Language Processing (NLP)",
    "Text Analytics",
    "Sentiment Analysis",
    "Power BI",
    "Microsoft Azure",
    "Google Cloud Platform (GCP)",
    "Azure OpenAI",
    "Git",
    "Jupyter Notebook",
    "Streamlit"
],
  # Specify required skills
        'experience_level': '1+ years',              # Specify experience level (e.g., Mid, Senior, Junior)
        'job_type': 'Full-time',                # Specify job type (e.g., Full-time, Part-time, Contract)
        'current_year': str(datetime.now().year)  # Current year
    }
    
    try:
        Maildrafter().crew().kickoff(inputs=inputs)
        print("✅ Email drafts saved to: email_drafts.xlsx")

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Maildrafter().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Maildrafter().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        Maildrafter().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
