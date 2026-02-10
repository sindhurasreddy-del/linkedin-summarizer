LinkedIn AI Agent: ReAct Summarizer
An autonomous AI agent that uses the ReAct (Reasoning + Acting) pattern to scrape, analyze, and summarize LinkedIn profiles. Built with LangChain, ScrapIn.io, and OpenAI.

 Overview
Traditional scrapers often fail due to LinkedIn's complex anti-bot measures. This project solves that by using ScrapIn.io's Enrichment API combined with a LangChain ReAct Agent.

Instead of a linear script, the agent "thinks" about the user's request, decides which tools to use, observes the JSON data returned, and generates a context-aware summary.

Key Features
Autonomous Reasoning: Uses a Thought/Action/Observation loop to process profile data.

Anti-Bot Resilience: Powered by ScrapIn.io to ensure high success rates without Selenium overhead.

Structured Output: Converts messy profile data into clean, categorized professional summaries.

Extensible Tooling: Easy to add new tools like Google Search, Email finders, or CRM integrators.

 Tech Stack
Orchestration: LangChain

LLM: OpenAI GPT-4o / GPT-4

Data Sourcing: ScrapIn.io

Environment: Python 3.9+

 Getting Started
1. Prerequisites
You will need:

An OpenAI API Key

A ScrapIn.io API Key

2. Installation
Bash
git clone https://github.com/YOUR_USERNAME/linkedin-ai-summarizer.git
cd linkedin-ai-summarizer
pip install -r requirements.txt
3. Configuration
Create a .env file in the root directory:

Code snippet
OPENAI_API_KEY=your_openai_key_here
SCRAPIN_API_KEY=your_scrapin_key_here
4. Run the Agent
Bash
python app.py
 Project Structure
Plaintext
├── app.py              # Agent initialization and execution loop
├── tools.py            # Custom tool definitions (ScrapIn.io integration)
├── requirements.txt    # Project dependencies
├── .env.example        # Template for environment variables
└── README.md           # Documentation
 Contributing
Contributions are what make the open-source community an amazing place to learn, inspire, and create.


Open a Pull Request
