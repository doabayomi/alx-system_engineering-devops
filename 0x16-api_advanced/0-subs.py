#!/usr/bin/python3
"""Number of subscribers check"""
import requests

def number_of_subscribers(subreddit):
    with open('reddit_token.txt', 'r') as file:
        token = file.read().strip()

    headers = {
        'Authorization': f"bearer {token}",
        'User-Agent': 'alx:api-advanced-project (by /u/Bad_Bunny_D)'
        }
    api_url = f"https://oauth.reddit.com//r/{subreddit}/about.json"

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

