from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, DirectoryReadTool, FileWriterTool, FileReadTool, ArxivPaperTool
from marketing.tools.custom_tool import LinkedInPostAnalyzer, ResearchTopicAnalyzer, ResumeOptimizer, InnovationTracker, ResearchPaperAnalyzer
import yaml
from pathlib import Path
from crewai.project import CrewBase,agent,task,crew
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class Marketing:
    agents: list[BaseAgent]
    tasks: list[Task]
    
    @agent
    def ai_ml_research_scientist(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_ml_research_scientist'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool('resources/drafts'),
                FileWriterTool(),
                FileReadTool(),
                ArxivPaperTool(),
                LinkedInPostAnalyzer(),
                ResearchTopicAnalyzer(),
                ResumeOptimizer(),
                InnovationTracker(),
                ResearchPaperAnalyzer()
            ],
            max_rpm=3,
            max_iter=3,
            reasoning=True,
            inject_date=True,
            allow_delegation=True,
            verbose=True
        )
    
    @agent
    def research_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['research_content_creator'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool('resources/drafts'),
                FileWriterTool(),
                FileReadTool(),
                ArxivPaperTool(),
                LinkedInPostAnalyzer(),
                ResearchTopicAnalyzer(),
                ResumeOptimizer(),
                InnovationTracker(),
                ResearchPaperAnalyzer()
            ],
            inject_date=True,
            allow_delegation=True,
            max_rpm=3,
            max_iter=3,
            verbose=True
        )
    
    @agent
    def research_blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['research_blog_writer'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool('resources/drafts'),
                FileWriterTool(),
                FileReadTool(),
                ArxivPaperTool(),
                LinkedInPostAnalyzer(),
                ResearchTopicAnalyzer(),
                ResumeOptimizer(),
                InnovationTracker(),
                ResearchPaperAnalyzer()
            ],
            max_rpm=3,
            max_iter=2,
            allow_delegation=True,
            inject_date=True,
            verbose=True
        )
    
    @agent
    def content_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_optimizer'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool('resources/drafts'),
                FileWriterTool(),
                FileReadTool(),
                ArxivPaperTool(),
                LinkedInPostAnalyzer(),
                ResearchTopicAnalyzer(),
                ResumeOptimizer(),
                InnovationTracker(),
                ResearchPaperAnalyzer()
            ],
            verbose=True,
            allow_delegation=True,
            max_rpm=3,
            max_iter=2,
            reasoning=False
        )
    
    @agent
    def content_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_summarizer'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool('resources/drafts'),
                FileWriterTool(),
                FileReadTool(),
                ArxivPaperTool(),
                LinkedInPostAnalyzer(),
                ResearchTopicAnalyzer(),
                ResumeOptimizer(),
                InnovationTracker(),
                ResearchPaperAnalyzer()
            ],
            verbose=True,
            allow_delegation=True,
            max_rpm=3,
            max_iter=2,
            reasoning=False
        )
    
    # Task definitions
    @task
    def research_market_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['research_market_analysis'],
            agent=self.ai_ml_research_scientist()
        )
    
    @task
    def summarize_market_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_market_analysis'],
            agent=self.content_summarizer()
        )
    
    @task
    def develop_research_strategy(self) -> Task:
        return Task(
            config=self.tasks_config['develop_research_strategy'],
            agent=self.ai_ml_research_scientist()
        )
    
    @task
    def summarize_research_strategy(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_research_strategy'],
            agent=self.content_summarizer()
        )
    
    @task
    def create_research_content_calendar(self) -> Task:
        return Task(
            config=self.tasks_config['create_research_content_calendar'],
            agent=self.research_content_creator()
        )
    
    @task
    def prepare_research_linkedin_posts(self) -> Task:
        return Task(
            config=self.tasks_config['prepare_research_linkedin_posts'],
            agent=self.research_content_creator(),
            output_file='resources/outputs/research_linkedin_posts.md'
        )
    
    @task
    def summarize_linkedin_posts(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_linkedin_posts'],
            agent=self.content_summarizer()
        )
    
    @task
    def research_topic_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['research_topic_analysis'],
            agent=self.research_blog_writer()
        )
    
    @task
    def draft_research_blogs(self) -> Task:
        return Task(
            config=self.tasks_config['draft_research_blogs'],
            agent=self.research_blog_writer(),
            output_file='resources/outputs/research_blogs.md'
        )
    
    @task
    def optimize_research_content(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_research_content'],
            agent=self.content_optimizer(),
            output_file='resources/drafts/optimized_research_content.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the AI/ML Research Scientist LinkedIn Marketing and Research Publication crew"""
        return Crew(
            agents=[
                self.ai_ml_research_scientist(),
                self.research_content_creator(),
                self.research_blog_writer(),
                self.content_optimizer(),
                self.content_summarizer()
            ],
            tasks=[
                self.research_market_analysis(),
                self.summarize_market_analysis(),
                self.develop_research_strategy(),
                self.summarize_research_strategy(),
                self.create_research_content_calendar(),
                self.prepare_research_linkedin_posts(),
                self.summarize_linkedin_posts(),
                self.research_topic_analysis(),
                self.draft_research_blogs(),
                self.optimize_research_content()
            ],
            process=Process.sequential,
            verbose=True
        )
