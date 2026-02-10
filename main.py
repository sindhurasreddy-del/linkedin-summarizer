import os
from dotenv import load_dotenv
from agent import create_linkedin_agent

load_dotenv()

def main():
    agent = create_linkedin_agent()

    linkedin_url = input("Enter LinkedIn profile URL: ")

    prompt = f"""
    Fetch the LinkedIn profile data for the given URL.
    Analyze the professional background.
    Generate a concise, recruiter-friendly professional summary
    highlighting skills, experience, and career focus.
    """

    result = agent.run(f"{prompt}\nLinkedIn URL: {linkedin_url}")
    print("\n--- AI-Generated LinkedIn Summary ---\n")
    print(result)

if __name__ == "__main__":
    main()
