import requests
import json
from concurrent.futures import ThreadPoolExecutor

URL = "https://api.pushshift.io/reddit/comment/search/"
PARAMS = {"subreddit": "your_subreddit_here", "size": 100}

comments = []

def fetch_comments():
    response = requests.get(URL, params=PARAMS)
    data = response.json().get("data")
    comments.extend([comment['body'] for comment in data])

with ThreadPoolExecutor() as executor:
    executor.map(fetch_comments, [PARAMS for _ in range(10)])  # Adjust range as needed

with open('comments.json', 'w') as f:
    json.dump(comments, f)

