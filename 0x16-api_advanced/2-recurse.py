#!/usr/bin/python3
"""task 3"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """function that queries the Reddit API"""
    res = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
              headers={"User-Agent": "Klich from Holberton"},
              allow_redirects=False,
              params={"after": after, "limit": 10})
    # print(res, hot_list, after)
    if res.status_code == 200:
        search = res.json().get('data').get('children')
        # print(hot)
        if search:
            hot_list += search
            after = res.json().get('data').get('after')
            # print("hot_list =", hot_list)
            # print("*"*100)
            # print("after =", after)
            if after is None:
                return hot_list
            return recurse(subreddit, hot_list, after)
        else:
            return None
    else:
        return None
