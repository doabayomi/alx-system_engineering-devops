#!/usr/bin/python3
"""Recursively get data for articles in a sub reddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    file_id = '1egbAidc-mCcvii7TRZSSWpduxQVs2BcS'
    download_url = f'https://drive.google.com/uc?id={file_id}'

    # Send a request to the download URL
    response = requests.get(download_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Read the content of the file (token)
        token = response.text.strip()
    else:
        print(f"Failed to download file: {response.status_code}")

    headers = {
        'Authorization': f"bearer {token}",
        'User-Agent': 'alx:api-advanced-project (by /u/Bad_Bunny_D)'
        }
    api_url = f"https://oauth.reddit.com//r/{subreddit}/hot.json"

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if after:
        url += f"?after={after}"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    hot_list += [post['data']['title'] for post in data['data']['children']]
    after = data['data']['after']

    # If 'after' is None, we have reached the
    # end of the list and return the hot_list
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
