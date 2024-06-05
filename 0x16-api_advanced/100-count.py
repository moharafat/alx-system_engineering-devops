#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles
and prints a sorted count of given keywords"""
import requests
from collections import Counter
import re


def count_words(subreddit, word_list, after=None, word_count=None):
    """script queries Reddit API returns list containing
    titles of all hot articles passed subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyRedditApp/0.1)'}
    params = {'limit': 100}

    # adding 'after' param.
    if after:
        params['after'] = after

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            # counting occurrences of each keyword
            for post in posts:
                title = post['data']['title'].lower()
                words_in_title = re.findall(r'\b\w+\b', title)
                for word in word_list:
                    word_lower = word.lower()
                    word_count[word_lower] += words_in_title.count(word_lower)

            # Check for a next page
            if data['data']['after']:
                return count_words(
                    subreddit, word_list, data['data']['after'], word_count)
            else:
                # Sort
                sorted_word_count = sorted(
                    word_count.items(), key=lambda item: (-item[1], item[0]))
                for word, count in sorted_word_count:
                    if count > 0:
                        print('{}: {}'.format(word[0], word[1]))
                return
        else:
            return None
    except requests.RequestException:
        return None
