from crewai import Agent
import re
import streamlit as st
from crewai import LLM
# from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools

import os
os.environ["OPENAI_API_KEY"] = "NA"

# Initialize Ollama LLM
llm = LLM(
    model="ollama/crewai-llama31",
    base_url="http://localhost:11434",
    stop=["Result"]
    # stream=True
)

class TripAgents():
    def __init__(self):
        self.llm = llm

    def city_selection_agent(self):
        return Agent(
            role='City Selection Expert',
            goal='Select the best city based on weather, season, and prices',
            backstory='An expert in analyzing travel data to pick ideal destinations',
            tools=[
                SearchTools.search_internet
                # BrowserTools.scrape_and_summarize_website,
            ],
            llm=self.llm,
            verbose=True,
        )

    def local_expert(self):
        return Agent(
            role='Local Expert at this city',
            goal='Provide the BEST insights about the selected city',
            backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
            tools=[
                SearchTools.search_internet
                # BrowserTools.scrape_and_summarize_website,
            ],
            llm=self.llm,
            verbose=True
        )

    def travel_concierge(self):
        return Agent(
            role='Amazing Travel Concierge',
            goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
            backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
            tools=[
                SearchTools.search_internet,
                # BrowserTools.scrape_and_summarize_website,
                CalculatorTools.calculate
            ],
            llm=self.llm,
            verbose=True
        )
