#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses hot article titles, and prints a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}
    
    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}'
    
    headers = {'User-Agent': 'MyRedditBot/1.0'}  # Set a custom User-Agent to avoid issues

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title']
        title_words = [word.lower() for word in title.split()]
        
        for word in word_list:
            if word.lower() in title_words:
                count_dict[word.lower()] = count_dict.get(word.lower(), 0) + title_words.count(word.lower())

    after = data['data']['after']
    if after is not None:
        return count_words(subreddit, word_list, after, count_dict)
    else
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Example: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        result = count_words(subreddit, word_list)
        if result is None:
            print("Invalid subreddit or no matching posts.")
