from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

from .tools.custom_tool import EstimarPrecio
from .config import Variable



@CrewBase
class Crewhackathon():
    """Crewhackathon crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def empresa(self) -> Agent:
        return Agent(
            config=self.agents_config['empresa'], # type: ignore[index]
            verbose=True
        )

    @agent
    def consumidor(self) -> Agent:
        return Agent(
            config=self.agents_config['consumidor'], # type: ignore[index]
            verbose=True,
            tools=[EstimarPrecio()]
        )

    @agent
    def estado(self) -> Agent:
        return Agent(
            config=self.agents_config['estado'],  # type: ignore[index]
            verbose=True,
            tools = [EstimarPrecio()]
        )

    @agent
    def inversores(self) -> Agent:
        return Agent(
            config=self.agents_config['inversores'],  # type: ignore[index]
            verbose=True,
            tools=[EstimarPrecio()]
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def tarea_empresa(self) -> Task:
        return Task(
            config=self.tasks_config['tarea_empresa'], # type: ignore[index]
        )

    @task
    def tarea_consumidor(self) -> Task:
        return Task(
            config=self.tasks_config['tarea_consumidor'], # type: ignore[index]
            #output_file='report.md'
        )

    @task
    def tarea_estado(self) -> Task:
        return Task(
            config=self.tasks_config['tarea_estado'], # type: ignore[index]
            #output_file='report.md'
        )

    @task
    def tarea_inversor(self) -> Task:
        return Task(
            config=self.tasks_config['tarea_inversor'], # type: ignore[index]
            #output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Crewhackathon crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
