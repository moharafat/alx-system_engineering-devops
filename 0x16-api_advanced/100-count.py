#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles
and prints a sorted count of given keywords"""
import requests

def count_words(subreddit, word_list):
    """script queries Reddit API returns list containing
    titles of all hot articles passed subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyRedditApp/0.1)'}
    params = {'limit': 100}