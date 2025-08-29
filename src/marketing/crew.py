from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool,FileWriterTool, FileReadTool, DirectoryReadTool, ScrapeWebsiteTool
from dotenv import load_dotenv
from pydantic import BaseModel, Field

_=load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

class Content(BaseModel):
    content_type: str = Field(...,
                              description="The type of content to be created (e.g., blog post, social media post, video)")
    topic: str = Field(..., description="The topic of the content")
    target_audience: str = Field(..., description="The target audience for the content")
    tags: List[str] = Field(..., description="Tags to be used for the content")
    content: str = Field(..., description="The content itself")


@CrewBase
class Marketing():
    """Marketing crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def head_of_marketing(self) -> Agent:
        return Agent(
            config=self.agents_config['head_of_marketing'], # type: ignore[index]
            tools=[SerperDevTool(),FileWriterTool(), FileReadTool(), DirectoryReadTool('src/marketing/resources/drafts'), ScrapeWebsiteTool()],
            max_rpm=3,
            reasoning=True,
            inject_date=True,
            allow_delegation=True,
            verbose=True
        )

    @agent
    def content_creator_social_media(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator_social_media'], # type: ignore[index]
            tools=[FileWriterTool(), FileReadTool(), DirectoryReadTool('src/marketing/resources/drafts'), ScrapeWebsiteTool()],
            inject_date=True,
            allow_delegation=True,
            max_rpm=3,
            max_iter=30,
            verbose=True
        )

    @agent
    def content_writer_blogs(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer_blogs'], # type: ignore[index]
            tools=[FileWriterTool(), FileReadTool(), DirectoryReadTool('src/marketing/resources/drafts'), ScrapeWebsiteTool()],
            max_rpm=3,
            max_iter=5,
            allow_delegation=True,
            inject_date=True,
            verbose=True
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_specialist'], # type: ignore[index]
            tools=[FileWriterTool(), FileReadTool(), DirectoryReadTool('src/marketing/resources/drafts'), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=True,
            max_rpm=3,
            max_iter=3,
            reasoning=True,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def market_research(self) -> Task:
        return Task(
            config=self.tasks_config['market_research'], # type: ignore[index]
            agent=self.head_of_marketing()
        )

    @task
    def prepare_post_drafts(self) -> Task:
        return Task(
            config=self.tasks_config['prepare_post_drafts'], # type: ignore[index]
            agent=self.content_creator_social_media(),
            output_file='report.md'
        )

    @task
    def draft_blogs(self) -> Task:
        return Task(
            config=self.tasks_config['draft_blogs'], # type: ignore[index]
            agent=self.content_writer_blogs(),
            output_file='blog.md'
        )

    @task
    def seo_optimization(self) -> Task:
        return Task(
            config=self.tasks_config['seo_optimization'], # type: ignore[index]
            agent=self.seo_specialist(),
            output_file='seo_optimized_blog.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Marketing crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
