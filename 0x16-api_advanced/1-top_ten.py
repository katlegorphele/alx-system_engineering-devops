#!/usr/bin/python3
"""
Function that queries the Reddit API
validates a subreddit and
retrieves the top 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Get top ten posts"""
    # Get url
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # Get headers
    headers = {"User-Agent": "My User Agent 1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data").get("children")
    for post in posts[:10]:
        print(post.get("data").get("title"))
