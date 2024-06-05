#!/usr/bin/python3
"""script queries Reddit API returns list containing
titles of all hot articles passed subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """script queries Reddit API returns list containing
    titles of all hot articles passed subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyRedditApp/0.1)'}
    params = {'limit': 100}

    if after:
        params['after'] = after
    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            # Add titles of hot posts
            for post in posts:
                hot_list.append(post['data']['title'])

            # Check for a next page
            if data['data']['after']:
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
