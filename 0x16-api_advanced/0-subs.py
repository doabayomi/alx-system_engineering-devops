#!/usr/bin/python3
"""Number of subscribers check"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'BadBunnyN47WhoLikedNikky'}
    api_url = f"https://www.reddit.com//r/{subreddit}/about.json"

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        res_data = response.json()
        return res_data['data']['subscribers']
    else:
        return 0

