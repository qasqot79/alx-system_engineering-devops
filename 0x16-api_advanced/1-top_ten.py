#!/usr/bin/python3
"""API Reddit"""
import requests

def top_ten(subreddit):
    # Define the Reddit API URL for the "hot" posts in the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom user-agent to avoid being blocked by Reddit
    headers = {"User-Agent": "MyRedditBot"}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the subreddit is valid
    if response.status_code != 200:
        print("None")
        return

    # Parse the JSON response
    data = response.json()

    # Extract and print the titles of the first 10 hot posts
    for i, post in enumerate(data['data']['children']):
        print(f"{i + 1}. {post['data']['title']}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
