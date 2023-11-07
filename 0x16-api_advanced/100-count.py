#!/usr/bin/python3
""" Functions to adcquire info from API Reddit"""
import praw

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    # Initialize the Reddit API client
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         user_agent='YOUR_USER_AGENT')

    # Check if the subreddit is valid
    try:
        reddit.subreddits.search_by_name(subreddit, exact=True)
    except prawcore.NotFound:
        return

    # Query the API for hot articles in the subreddit
    hot_articles = reddit.subreddit(subreddit).hot(limit=25, params={'after': after})

    # Iterate through the hot articles
    for article in hot_articles:
        title = article.title.lower()
        for word in word_list:
            # Check if the word is in the title and not part of a larger word
            if title.count(f" {word} ") + title.startswith(word) + title.endswith(word) > 0:
                counts[word] = counts.get(word, 0) + 1

    # Check if there are more pages of results
    if hot_articles._after:
        return count_words(subreddit, word_list, after=hot_articles._after, counts=counts)
    else:
        # Sort the results by count and then alphabetically
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit_name = sys.argv[1]
        keyword_list = sys.argv[2].split()
        count_words(subreddit_name, keyword_list)
    
