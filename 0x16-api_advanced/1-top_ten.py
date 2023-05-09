#!/usr/bin/python3
"""task 1"""
import requests


def top_ten(subreddit):
    """Write a function that queries the Reddit API"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    req = requests.get(url)

    if (req.status_code != 200):
        print(None)
        return

    try:
        childrens = req.json().get('data').get('children')
        for children in childrens:
            print(children.get('data').get('title'))
    except Exception:
        pass
