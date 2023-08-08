#!/usr/bin/python3

'''
Recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
'''

import requests


def count_words(subreddit, word_list, after=None, count_dict={}):

    # Get url
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # Get headers
    headers = {"User-Agent": "My User Agent 1.0"}

    # Get response
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check status code
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if len(posts) > 0:
            for post in posts:
                title = post['data']['title']
                for word in word_list:
                    if word.lower() in title.lower():
                        if word in count_dict:
                            count_dict[word] += 1
                        else:
                            count_dict[word] = 1

            after = data['data']['after']

            if after is not None:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                if len(count_dict) > 0:
                    for key, value in sorted(count_dict.items(),
                                             key=lambda x: (-x[1], x[0])):
                        print("{}: {}".format(key.lower(), value))
                else:
                    print("")
    else:
        return None
