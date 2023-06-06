#!/usr/bin/python3

"""
Function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    """
    # Set the URL
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set the headers
    headers = {"User-Agent": "My User Agent 1.0"}

    # Make the request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the status code is 200, return the number of subscribers
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
