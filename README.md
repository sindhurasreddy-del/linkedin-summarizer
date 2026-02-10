# linkedin-summarizer
AI agent built langchain and scrapIn.io that uses a React logic to scrape, analyze and summarize LinkedIn profiles
# LinkedIn AI Profiler (ReAct Agent)

An intelligent LinkedIn profile summarizer that uses **LangChain**, a **ReAct Agent** framework, and **ScrapIn.io** to transform raw LinkedIn data into concise, actionable professional summaries.

## Features
- **Agentic Reasoning:** Uses the ReAct (Reasoning + Acting) pattern to decide how to process profile data.
- **Clean Data:** Integrates with **ScrapIn.io Enrichment API** to bypass LinkedIn's anti-scraping measures and get structured JSON.
- **Customizable:** Easily extendable to add Google Search or Email discovery tools.

##  Tech Stack
- **Framework:** LangChain
- **LLM:** OpenAI GPT-4
- **Scraper:** ScrapIn.io (Enrichment API)
- **Language:** Python 3.9+

##  Setup
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/linkedin-ai-summarizer.git](https://github.com/YOUR_USERNAME/linkedin-ai-summarizer.git)
   cd linkedin-ai-summarizer
