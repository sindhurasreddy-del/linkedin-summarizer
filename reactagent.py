from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from tools import fetch_linkedin_profile
import json

def create_linkedin_agent():
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0
    )

    tools = [
        Tool(
            name="LinkedIn Profile Fetcher",
            func=lambda url: json.dumps(fetch_linkedin_profile(url)),
            description="Fetches structured LinkedIn profile data using ScrapIn.io"
        )
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
