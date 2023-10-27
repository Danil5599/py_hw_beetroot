import asyncio
import aiohttp
import json

async def fetch_comments(subreddit):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&limit=500"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    subreddit = 'YOUR_CHOICE_OF_SUBREDDIT'  # Replace with your choice
    data = await fetch_comments(subreddit)
    with open("comments.json", "w") as file:
        json.dump(data, file)

asyncio.run(main())