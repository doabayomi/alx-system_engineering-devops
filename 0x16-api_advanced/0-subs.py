#!/usr/bin/python3
"""Number of subscribers check"""
import requests


def number_of_subscribers(subreddit):
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
    api_url = f"https://oauth.reddit.com//r/{subreddit}/about.json"

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
