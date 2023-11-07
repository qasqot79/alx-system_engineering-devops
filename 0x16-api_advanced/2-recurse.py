#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

import praw

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    # Initialize the Reddit API client
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         user_agent='YOUR_USER_AGENT')

    # Check if the subreddit is valid
    try:
        reddit.subreddits.search_by_name(subreddit, exact=True)
    except prawcore.NotFound:
        return None

    # Query the API for hot articles in the subreddit
    hot_articles = reddit.subreddit(subreddit).hot(limit=25, params={'after': after})

    # Accumulate titles
    hot_list += [article.title for article in hot_articles]

    # Check if there are more pages of results
    if hot_articles._after:
        return recurse(subreddit, hot_list, after=hot_articles._after)
    else:
        return hot_list

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        hot_titles = recurse(subreddit_name)
        if hot_titles is not None:
            print(len(hot_titles))
        else:
            print("None")
