#!/usr/bin/python3
"""
module - 2-recurse
contains a function with
prototype: def recurse(subreddit, hot_list=[], after='')
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    returns a list containing the titles of all
    hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    """
    # To stop recursion when pagination ends
    if after is None:
        return hot_list

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'user-agent': 'nehe-browser/1.1.1'}
    params = {'limit': 50, 'after': after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data")
    after = data.get("after")

    for item in data.get("children"):
        post = item.get('data')
        hot_list.append(post.get("title"))
    return recurse(subreddit, hot_list, after)
