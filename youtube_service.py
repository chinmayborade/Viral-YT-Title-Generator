import requests
import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY=os.getenv("YOUTUBE_API_KEY")
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

def fetch_titles(query, max_results=20):
    params = {
        "part": "snippet",
        "q": query,
        "maxResults": max_results,
        "type": "video",
        "key": YOUTUBE_API_KEY,
    }
    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    # print("STATUS:", response.status_code)
    # print("RESPONSE:", response.json())  # <-- add this
    response.raise_for_status()
    data = response.json()
    titles = [item["snippet"]["title"] for item in data.get("items", [])]
    return titles