#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
    
    if not word_list:
        return counts

    headers = {'User-Agent': 'realqasqot79.tech'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json', headers=headers, params=params)

    if response.status_code != 200:
        print("Invalid subreddit or an error occurred. Exiting.")
        return

    data = response.json().get('data', {})
    children = data.get('children', [])
    for child in children:
        title = child['data']['title']
        for word in word_list:
            word_lower = word.lower()
            title_lower = title.lower()
            count = title_lower.count(word_lower)
            if count > 0:
                if word_lower in counts:
                    counts[word_lower] += count
                else:
                    counts[word_lower] = count

    after = data.get('after')
    if after:
        return count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")

if __name__ == "__main":
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, word_list)

