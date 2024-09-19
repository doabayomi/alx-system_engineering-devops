#!/usr/bin/python3
"""Top ten posts Reddit API."""
import requests


def top_ten(subreddit):
    """Gets top ten hot posts for a subreddit."""
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
    api_url = f"https://oauth.reddit.com//r/{subreddit}/hot.json?limit=10"

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
