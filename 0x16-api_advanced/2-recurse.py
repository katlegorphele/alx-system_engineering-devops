#!/usr/bin/python3

'''
Recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit
'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    # Set the URL
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    # Set the headers
    headers = {'User-Agent': 'My User Agent 1.0'}

    # Make the request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the status code is 200, return the number of subscribers
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        # If there are posts, add them to the list
        if len(posts) > 0:
            for post in posts:
                hot_list.append(post["data"]["title"])
                # If there are more posts, recurse
            after = data["data"]["after"]
            # If there are no more posts, return the list
            if after is not None:
                # Recurse
                return recurse(subreddit, hot_list, after)
            else:
                # Return the list
                return hot_list
        else:
            # If there are no posts, return None
            return None
    else: 
        # If the status code is not 200, return None
        return None
