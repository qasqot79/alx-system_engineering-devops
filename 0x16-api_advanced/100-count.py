#!/usr/bin/python3
""" Functions to adcquire info from API Reddit"""
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my_script/1.0"}
    params = {"after": after, "limit": 100}

    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title", "")
        for word in word_list:
            word = word.lower()
            title_lower = title.lower()
            if title_lower.count(word) > 0:
                if word in word_count:
                    word_count[word] += title_lower.count(word)
                else:
                    word_count[word] = title_lower.count(word)

    next_page = data.get("data", {}).get("after")
    if next_page:
        count_words(subreddit, word_list, next_page, word_count)
    else:
        sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count
            print("{}: {}".format(word, count))

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = sys.argv[2].split()
        count_words(subreddit, keywords)
