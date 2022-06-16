#!/usr/bin/python3
"""
module - 0-subs.py
contains a function with prototype
def number_of_subscribers(subreddit)
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number ofsubscribers
    (not active users, total subscribers) for a given subreddit.
    """
    if not subreddit:
        return 0
    if type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'nehe-browser/1.1.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get('data', {})
    subscribers = data.get('subscribers', 0)
    return subscribers
