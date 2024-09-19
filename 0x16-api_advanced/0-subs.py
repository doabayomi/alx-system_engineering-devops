#!/usr/bin/python3
"""Number of subscribers check"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers in a subreddit

    Args:
        subreddit: Subreddit name

    Returns:
        subscriber count if subreddit exists,
        0, otherwise
    """
    headers = {'User-Agent': 'BadBunnyN47WhoLikedNikky'}
    api_url = f"https://www.reddit.com//r/{subreddit}/about.json"

    response = requests.get(api_url, headers=headers, allow_redirects=False)
    res = response.json()
    if response.status_code == 200:
        return (res['data']['subscribers'])
    return (0)

