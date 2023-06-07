#!/usr/bin/python3

"""
Function that queries the Reddit API
validates a subreddit and
retrieves the top 10 hot posts
"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if len(posts) > 0:
            print(f"Top 10 hot posts in /r/{subreddit}:")
            for post in posts:
                print(post["data"]["title"])
        else:
            print(f"No hot posts found in /r/{subreddit}.")
    else:
        print("None")
