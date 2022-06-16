#!/usr/bin/python3
"""
module - 1-top_ten
contains a function with
prototype: def top_ten(subreddit)
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    if not subreddit:
        print(None)
        return
    if type(subreddit) is not str:
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {'user-agent': 'nehe-browser/1.1.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get('data', {})
    for item in data.get('children'):
        print(item.get('data').get('title'))
