#!/usr/bin/python3
"""Count words in subreddit."""
from collections import Counter
import re
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """Count number of times words in list appears."""
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
        api_url += f"?after={after}"

    if response.status_code != 200:
        return

    if word_count is None:
        word_count = Counter()

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        title = post['data']['title']
        title_words = re.findall(r'\b\w+\b', title.lower())
        for word in word_list:
            word_count[word] += title_words.count(word.lower())

    after = data['data']['after']

    if after is None:
        sorted_word_count = sorted([(k, v) for k, v in word_count.items()
                                   if v > 0], key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, after, word_count)
