import threading
import requests
import json

comments = []
lock = threading.Lock()

def fetch_comments(after_timestamp=None):
    url = "https://api.pushshift.io/reddit/comment/search/"
    parameters = {
        "subreddit": "choose_your_subreddit_here",
        "sort_type": "created_utc",
        "sort": "asc",
        "size": 500,
    }
    if after_timestamp:
        parameters["after"] = after_timestamp

    response = requests.get(url, params=parameters)
    data = response.json().get("data")
    with lock:
        comments.extend(data)
        next_timestamp = data[-1]["created_utc"] if data else None
    return next_timestamp

def worker():
    timestamp = None
    while True:
        timestamp = fetch_comments(timestamp)
        if timestamp is None:
            break

threads = []
for _ in range(10):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

with open("comments.json", "w") as f:
    json.dump(comments, f)