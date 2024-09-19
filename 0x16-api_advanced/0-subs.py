#!/usr/bin/python3
import requests
"""Number of subscribers check"""


def number_of_subscribers(subreddit):
    """Gets the number of subscribers in a subreddit

    Args:
        subreddit: Subreddit name

    Returns:
        subscriber count if subreddit exists,
        0, otherwise
    """
    api_url = f"https://www.reddit.com//r/{subreddit}/top.json"
    params = {
        'limit': 10,
        't': 'month'
    }

    response = requests.get(api_url, params,
                            headers={
                                'User-Agent': 'BadBunnyN47WhoLikedNikky'
                                }, allow_redirects=False)
    if response.status_code != 200:
        return 0

    response_data = response.json()
    sub = response_data['data']['children'][0]['data']['subreddit_subscribers']
    return sub
