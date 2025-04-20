from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from maildrafter.tools.custom_tool import InternetSearchTool

from crewai import Agent
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from dotenv import load_dotenv
import os

load_dotenv()

# Set API keys
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
from crewai_tools import LinkupSearchTool

# Initialize the tool with your API key
linkup_tool = LinkupSearchTool(api_key=os.getenv("LINKUP_API_KEY"))
gemini_llm = LLM(
    api_key=os.getenv("GEMINI_API_KEY"),
    model="gemini/gemini-2.0-flash"
)

embedder_config = {
    "provider": "google",
    "config": {
        "model": "models/text-embedding-004",
        "api_key": os.getenv("GEMINI_API_KEY")
    }
}

# Define the PDF knowledge source
pdf_source = PDFKnowledgeSource(
    file_paths=["Suggula_Jyothsna_07_04_v5.pdf"],
    embedder=embedder_config
)

@CrewBase
class Maildrafter:
    """Chunni crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def job_sourcing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['job_sourcing_agent'],
            verbose=True,
            tools=[InternetSearchTool(),linkup_tool],
            llm=gemini_llm  # <--- use actual LLM object
        )


    @agent
    def company_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['company_research_agent'],
            verbose=True,
            tools=[InternetSearchTool(),linkup_tool],
            llm=gemini_llm
        )

    @agent
    def resume_tailoring_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_tailoring_agent'],
            verbose=True,
            knowledge_sources=[pdf_source],
            llm=gemini_llm
        )

    @agent
    def email_drafting_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['email_drafting_agent'],
            verbose=True,
            llm=gemini_llm
        )

    # --- Tasks ---
    @task
    def job_links_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_links_task'],
        )

    @task
    def company_contacts_task(self) -> Task:
        return Task(
            config=self.tasks_config['company_contacts_task'],
        )

    @task
    def resume_tailoring_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_tailoring_task'],
              output_file='matters.pdf',  # Save as Excel file
            output_format='pdf' 
        )

    @task
    def email_draft_task(self) -> Task:
        return Task(
            config=self.tasks_config['email_draft_task'],
            output_file='email_drafts.xlsx',  # Save as Excel file
            output_format='excel'  # Specify output format explicitly
        )
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.job_sourcing_agent(),
                self.company_research_agent(),
                self.resume_tailoring_agent(),
                self.email_drafting_agent()
            ],
            tasks=[
                self.job_links_task(),
                self.company_contacts_task(),
                self.resume_tailoring_task(),
                self.email_draft_task()
            ],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_source],
            embedder=embedder_config
        )

