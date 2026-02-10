import requests
import os

SCRAPIN_API_KEY = os.getenv("SCRAPIN_API_KEY")

def fetch_linkedin_profile(linkedin_url: str) -> dict:
    """
    Fetch structured LinkedIn profile data using ScrapIn.io Enrichment API
    """
    endpoint = "https://api.scrapin.io/enrichment/profile"
    headers = {
        "Authorization": f"Bearer {SCRAPIN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "linkedInUrl": linkedin_url
    }

    response = requests.post(endpoint, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()
